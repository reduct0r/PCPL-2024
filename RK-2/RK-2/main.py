from Requests import findGroupsEndWithKey, DepartmentsSortedByAvgNumberOfStudents, findDepartmentsStartWithKey
from tests.data import get_departments, get_student_groups, get_student_group_departments


def prepare_relations(departments, student_groups, group_deps):
    # Отношение один-ко-многим
    one_to_many = [
        (g.group_name, g.number_of_students, d.name)
        for d in departments
        for g in student_groups
        if g.department_id == d.id
    ]

    # Отношение многие-ко-многим
    temp = [
        (group.group_name, group_dep.department_id)
        for group in student_groups
        for group_dep in group_deps
        if group.id == group_dep.student_group_id
    ]

    many_to_many = [
        (group_name, dept.name)
        for dept in departments
        for group_name, dep_id in temp
        if dep_id == dept.id
    ]

    return one_to_many, many_to_many

def main():
    departments = get_departments()
    student_groups = get_student_groups()
    group_deps = get_student_group_departments()

    one_to_many, many_to_many = prepare_relations(departments, student_groups, group_deps)

    # Выполнение запросов
    findGroupsEndWithKey(one_to_many, "03")
    DepartmentsSortedByAvgNumberOfStudents(one_to_many)
    findDepartmentsStartWithKey(many_to_many, "А")

if __name__ == '__main__':
    main()