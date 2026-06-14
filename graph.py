from state import AgentState
from langgraph.graph import StateGraph, END

from llm import llm

def planner_node(state : AgentState):
    print("Planner Node is Running")

    return state

def search_node(state: AgentState):
    print("Search Node Running")

    state["jobs_found"] = """
    Python
    SQL
    AWS
    REST APIs
    Docker
    """

    return state

def analysis_node(state: AgentState):
    print("Analysis Node Running")

    prompt = f"""
    You are a senior career coach.

    Analyze the following skills:

    {state['jobs_found']}

    Tell me:
    1. Skill gaps
    2. Important technologies
    3. Learning priorities

    Keep the response under 150 words.
    """

    response = llm.invoke(prompt)

    state["skill_gap_analysis"] = response.content

    return state

def roadmap_node(state: AgentState):
    print("Roadmap Node Running")

    prompt = f"""
    You are an experienced software engineering mentor.

    Based on the following skill gap analysis:

    {state["skill_gap_analysis"]}

    Create a structured 4-week learning roadmap.

    For each week include:
    1. Topics to learn
    2. Practical exercises
    3. Mini project ideas
    4. Interview questions to practice

    Keep the roadmap practical and focused on getting a job.
    """

    response = llm.invoke(prompt)

    state["learning_plan"] = response.content

    return state

def interview_node(state: AgentState):
    print("Interview question node is running")

    state["interview_questions"] = """
    Tell me about youself.
    where do you see yourself in 5 years?
    """
    
    return state

def router_node(state: AgentState):
    print("Router Node Running")

    jobs = state["jobs_found"]

    if len(jobs.strip()) < 10:
        state["next_step"] = "search_again"
    else:
        state["next_step"] = "analysis"

    return state

def route_decision(state: AgentState):
    return state["next_step"]

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_node)
workflow.add_node("search", search_node)
workflow.add_node("analysis", analysis_node)
workflow.add_node("roadmap", roadmap_node)
workflow.add_node("interview", interview_node )
workflow.add_node("router", router_node)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "search")
workflow.add_edge("search", "router")
workflow.add_edge("analysis", "roadmap")
workflow.add_edge("roadmap", "interview")
workflow.add_edge("interview", END)


workflow.add_conditional_edges(
    "router",
    route_decision,
    {
        "analysis": "analysis",
        "search_again": "search"
    }
)

app = workflow.compile()