import unittest
from student import Student
from datetime import date, timedelta
from unittest.mock import patch


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("John", "Doe")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def setUpClass(self):
        print("set-up class")

    @classmethod
    def tearDownClass(self):
        print("tear down class")

    def test_full_name(self):
        self.assertEqual(self.student.full_name, "John Doe")

    def test_alert_santa(self):
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_apply_extension(self):
        original_end_date = self.student.end_date
        self.student.apply_extension(21)
        self.assertEqual(self.student.end_date, original_end_date +
                         timedelta(days=21))

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_fail(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False
            mocked_get.return_value.text =\
                "Something went wrong with our request"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with our request")


if __name__ == "__main__":
    unittest.main()
