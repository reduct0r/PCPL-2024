import unittest

from Requests import findGroupsEndWithKey, DepartmentsSortedByAvgNumberOfStudents, findDepartmentsStartWithKey


class TestRequests(unittest.TestCase):
    def setUp(self):
        # Подготовка тестовых данных
        self.one_to_many = [
            ("Группа 101", 30, "Прикладная математика"),
            ("Группа 102", 25, "Информатика"),
            ("Группа 103", 28, "Прикладная математика"),
            ("Группа 104", 22, "Физика"),
            ("Группа 105", 27, "Астрономия"),
            ("Группа 1003", 20, "Астрономия"),
            ("Группа 104А", 21, "История"),
            ("Группа 105А", 24, "Археология"),
            ("Группа 1003А", 23, "Астрофизика"),
            ("Группа 104Б", 21, "История"),
            ("Группа 145Б", 20, "Астрономия"),
            ("Группа 1Б03", 19, "Астрофизика"),
        ]

        self.many_to_many = [
            ("Группа 101", "Прикладная математика"),
            ("Группа 102", "Информатика"),
            ("Группа 103", "Прикладная математика"),
            ("Группа 104", "Физика"),
            ("Группа 105", "Астрономия"),
            ("Группа 1003", "Астрономия"),
            ("Группа 104А", "История"),
            ("Группа 105А", "Археология"),
            ("Группа 1003А", "Астрофизика"),
            ("Группа 104Б", "История"),
            ("Группа 145Б", "Астрономия"),
            ("Группа 1Б03", "Астрофизика"),
        ]

    def test_findGroupsEndWithKey_existing_key(self):
        # Проверка существующего ключа "03"
        result = findGroupsEndWithKey(self.one_to_many, "03", debug=False)
        expected = [
            {"group_name": "Группа 103", "department_name": "Прикладная математика"},
            {"group_name": "Группа 1003", "department_name": "Астрономия"},
            {"group_name": "Группа 1Б03", "department_name": "Астрофизика"},
        ]
        self.assertEqual(result, expected)

    def test_DepartmentsSortedByAvgNumberOfStudents_correct_order(self):
        # Проверка сортировки кафедр по среднему количеству студентов
        result = DepartmentsSortedByAvgNumberOfStudents(self.one_to_many, debug=False)
        expected = [
            {"department_name": "Прикладная математика", "average_number_of_students": 29.0},
            {"department_name": "Информатика", "average_number_of_students": 25.0},
            {"department_name": "Астрономия", "average_number_of_students": 22.0},
            {"department_name": "Физика", "average_number_of_students": 22.0},
            {"department_name": "Археология", "average_number_of_students": 24.0},
            {"department_name": "Астрофизика", "average_number_of_students": 21.0},
            {"department_name": "История", "average_number_of_students": 20.5},
        ]
        # Прикладная математика: (30 + 28) / 2 = 29.0
        # Информатика: 25 / 1 = 25.0
        # Физика: 22 / 1 = 22.0
        # Астрономия: (27 + 20 + 20) / 3 ≈ 22.33
        # История: (21 + 21) / 2 = 21.0
        # Археология: 24 / 1 = 24.0
        # Астрофизика: (23 + 19) / 2 = 21.0

        expected_correct = [
            {"department_name": "Прикладная математика", "average_number_of_students": 29.0},
            {"department_name": "Информатика", "average_number_of_students": 25.0},
            {"department_name": "Археология", "average_number_of_students": 24.0},
            {"department_name": "Астрономия", "average_number_of_students": 22.33},
            {"department_name": "Физика", "average_number_of_students": 22.0},
            {"department_name": "История", "average_number_of_students": 21.0},
            {"department_name": "Астрофизика", "average_number_of_students": 21.0},
        ]

        # Используем округление до 2 знаков для сравнения
        for res, exp in zip(result, expected_correct):
            self.assertEqual(res["department_name"], exp["department_name"])
            self.assertAlmostEqual(res["average_number_of_students"], exp["average_number_of_students"], places=2)

    def test_findDepartmentsStartWithKey_no_matches(self):
        # Проверка ключа, для которого нет соответствий
        result = findDepartmentsStartWithKey(self.many_to_many, "Z", debug=False)
        expected = []
        self.assertEqual(result, expected)

    def test_findDepartmentsStartWithKey_existing_key(self):
        # Дополнительный тест для существующего ключа "А"
        result = findDepartmentsStartWithKey(self.many_to_many, "А", debug=False)
        expected = [
            {"department_name": "Астрономия", "student_groups": ["Группа 105", "Группа 1003", "Группа 145Б"]},
            {"department_name": "Археология", "student_groups": ["Группа 105А"]},
            {"department_name": "Астрофизика", "student_groups": ["Группа 1003А", "Группа 1Б03"]},
        ]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()