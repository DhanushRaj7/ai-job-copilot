from graph import app

initial_state = {
    "user_goal": "Python Developer jobs in Chennai",
    "jobs_found": "",
    "skill_gap_analysis": "",
    "learning_plan": ""
}

result = app.invoke(initial_state)

print("\nFINAL STATE\n")
print(result)