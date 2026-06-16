from graph import app

initial_state = {
    "user_goal": "Give me React interview questions",

    "jobs_found": "",
    "skill_gap_analysis": "",
    "learning_plan": "",
    "interview_questions": "",
    "next_step": "",

    "tasks": [],
    "task_index": 0
}

result = app.invoke(initial_state)

print("\nFINAL STATE\n")
print(result)