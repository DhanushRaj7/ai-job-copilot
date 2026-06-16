from state import AgentState
from langgraph.graph import StateGraph, END

from llm import llm
from tools import search_jobs

def planner_node(state: AgentState):
    print("Planner Node Running")

    prompt = f"""
    User Request:
    {state['user_goal']}

    Available tasks:

    - search
    - analysis
    - roadmap
    - interview

    Return only a comma-separated list
    of tasks needed.

    Examples:

    User:
    Give me interview questions

    Output:
    interview

    User:
    Find Python jobs and create a roadmap

    Output:
    search,analysis,roadmap
    """

    response = llm.invoke(prompt)

    state["tasks"] = [
        task.strip().lower()
        for task in response.content.split(",")
    ]

    state["task_index"] = 0

    print("Planned Tasks:", state["tasks"])

    return state

def search_node(state: AgentState):
    print("Search Node Running")

    jobs = search_jobs(state["user_goal"])

    state["jobs_found"] = jobs

    state["task_index"] += 1

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

    state["task_index"] += 1

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

    state["task_index"] += 1

    return state

def interview_node(state: AgentState):
    print("Interview Node Running")

    prompt = f"""
    You are a senior technical interviewer.

    User Goal:
    {state['user_goal']}

    Job Requirements:
    {state.get('jobs_found', '')}

    Skill Gap Analysis:
    {state.get('skill_gap_analysis', '')}

    Learning Plan:
    {state.get('learning_plan', '')}

    Generate:

    1. 10 technical interview questions
    2. 5 behavioral interview questions
    3. 3 advanced follow-up questions

    Format the output clearly.
    """

    response = llm.invoke(prompt)

    state["interview_questions"] = response.content

    state["task_index"] += 1

    return state

def router_node(state: AgentState):
    print("Router Node Running")

    jobs = state["jobs_found"]

    if len(jobs.strip()) < 10:
        state["next_step"] = "search_again"
    else:
        state["next_step"] = "analysis"

    return state

def task_router_node(state: AgentState):
    print("Task Router Running")

    tasks = state["tasks"]
    idx = state["task_index"]

    if idx >= len(tasks):
        state["next_step"] = "end"
    else:
        state["next_step"] = tasks[idx]

    print("Next Task:", state["next_step"])

    return state

def task_route_decision(state: AgentState):
    return state["next_step"]

def route_decision(state: AgentState):
    return state["next_step"]

workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_node)
workflow.add_node("search", search_node)
workflow.add_node("analysis", analysis_node)
workflow.add_node("roadmap", roadmap_node)
workflow.add_node("interview", interview_node )
workflow.add_node("router", router_node)
workflow.add_node("task_router", task_router_node)

workflow.set_entry_point("planner")

workflow.add_edge("planner", "task_router")
workflow.add_edge("search", "task_router")
workflow.add_edge("analysis", "task_router")
workflow.add_edge("roadmap", "task_router")
workflow.add_edge("interview", "task_router")


workflow.add_conditional_edges(
    "task_router",
    task_route_decision,
    {
        "search": "search",
        "analysis": "analysis",
        "roadmap": "roadmap",
        "interview": "interview",
        "end": END
    }
)

app = workflow.compile()