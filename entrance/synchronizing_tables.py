def SynchronizingTables(length: int, ids: list, salary: list) -> list:
    sorted_ids = sorted(ids)
    sorted_salary = sorted(salary)

    ids_and_salary = {}
    for i, id in enumerate(sorted_ids):
        ids_and_salary[id] = sorted_salary[i]

    ordered_salary = []
    for i, id in enumerate(ids):
        ordered_salary.append(ids_and_salary[id])

    return ordered_salary
