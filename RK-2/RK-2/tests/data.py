from Department import Department
from StudentGroup import StudentGroup
from StudentGroupDepartment import StudentGroupDepartment

def get_departments():
    return [
        Department(id=1, name="Прикладная математика"),
        Department(id=2, name="Информатика"),
        Department(id=3, name="Физика"),
        Department(id=4, name="Астрономия"),
        Department(id=5, name="История"),
        Department(id=6, name="Археология"),
        Department(id=7, name="Астрофизика"),
    ]

def get_student_groups():
    return [
        StudentGroup(id=1, group_name="Группа 101", number_of_students=30, department_id=1),
        StudentGroup(id=2, group_name="Группа 102", number_of_students=25, department_id=2),
        StudentGroup(id=3, group_name="Группа 103", number_of_students=28, department_id=1),
        StudentGroup(id=4, group_name="Группа 104", number_of_students=22, department_id=3),
        StudentGroup(id=5, group_name="Группа 105", number_of_students=27, department_id=4),
        StudentGroup(id=6, group_name="Группа 1003", number_of_students=20, department_id=4),
        StudentGroup(id=7, group_name="Группа 104А", number_of_students=21, department_id=5),
        StudentGroup(id=8, group_name="Группа 105А", number_of_students=24, department_id=6),
        StudentGroup(id=9, group_name="Группа 1003А", number_of_students=23, department_id=7),
        StudentGroup(id=10, group_name="Группа 104Б", number_of_students=21, department_id=5),
        StudentGroup(id=11, group_name="Группа 145Б", number_of_students=20, department_id=4),
        StudentGroup(id=12, group_name="Группа 1Б03", number_of_students=19, department_id=7),
    ]

def get_student_group_departments():
    return [
        StudentGroupDepartment(student_group_id=1, department_id=1),
        StudentGroupDepartment(student_group_id=2, department_id=2),
        StudentGroupDepartment(student_group_id=3, department_id=1),
        StudentGroupDepartment(student_group_id=4, department_id=3),
        StudentGroupDepartment(student_group_id=5, department_id=4),
        StudentGroupDepartment(student_group_id=6, department_id=4),
        StudentGroupDepartment(student_group_id=7, department_id=5),
        StudentGroupDepartment(student_group_id=8, department_id=6),
        StudentGroupDepartment(student_group_id=9, department_id=7),
        StudentGroupDepartment(student_group_id=10, department_id=5),
        StudentGroupDepartment(student_group_id=11, department_id=4),
        StudentGroupDepartment(student_group_id=12, department_id=7),
    ]