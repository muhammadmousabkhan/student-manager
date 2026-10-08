import unittest

from student_manager import (
    add_student,
    get_students,
    search_student
)


class TestStudentManager(unittest.TestCase):

    def setUp(self):
        get_students().clear()

    def test_add_student(self):
        add_student("Ali", 20)

        self.assertEqual(
            get_students(),
            [{"name": "Ali", "age": 20}]
        )

    def test_search_student(self):
        add_student("Ali", 20)

        result = search_student("Ali")

        self.assertEqual(
            result,
            {"name": "Ali", "age": 20}
        )


if __name__ == "__main__":
    unittest.main()