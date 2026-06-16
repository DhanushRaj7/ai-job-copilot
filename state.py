from typing import TypedDict, List


class AgentState(TypedDict):
    user_goal: str
    jobs_found: str
    skill_gap_analysis: str
    learning_plan: str
    interview_questions: str
    next_step: str

    tasks: List[str]
    task_index: int