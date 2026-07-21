DEPENDENCIES = {
    "search": [],
    "analysis": ["search"],
    "roadmap": ["analysis"],
    "interview": []
}


def resolve_task(task, resolved=None):
    if resolved is None:
        resolved = []

    for dependency in DEPENDENCIES.get(task, []):
        resolve_task(dependency, resolved)

    if task not in resolved:
        resolved.append(task)

    return resolved



def resolve_plan(tasks):
    final_tasks = []

    for task in tasks:
        dependencies = resolve_task(task)

        for dependency in dependencies:
            if dependency not in final_tasks:
                final_tasks.append(dependency)

    return final_tasks