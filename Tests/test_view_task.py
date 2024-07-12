import unittest
from io import StringIO
import sys
from directory import direct

direct()
from task import view_task


class TestViewTask(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_case_1(self):
        # Test case for viewing tasks of the first subject with multiple tasks
        subject_list = ["Math", "Science", "English"]
        task_list = [
            ["Homework 1", "Homework 2"],
            ["Lab Report", "Project"],
            ["Essay", "Reading"]
        ]
        index = 1
        # Expected output lists tasks for "Math"
        expected_output = """Math
    1. Homework 1
    2. Homework 2
"""
        view_task(subject_list, task_list, index)
        self.assertEqual(self.held_stdout.getvalue(), expected_output)

    def test_case_2(self):
        # Test case for viewing tasks of the second subject with multiple tasks
        subject_list = ["Math", "Science", "English"]
        task_list = [
            ["Homework 1", "Homework 2"],
            ["Lab Report", "Project"],
            ["Essay", "Reading"]
        ]
        index = 2
        # Expected output lists tasks for "Science"
        expected_output = """Science
    1. Lab Report
    2. Project
"""
        view_task(subject_list, task_list, index)
        self.assertEqual(self.held_stdout.getvalue(), expected_output)

    def test_case_3(self):
        # Test case for viewing tasks of the third subject with multiple tasks
        subject_list = ["Math", "Science", "English"]
        task_list = [
            ["Homework 1", "Homework 2"],
            ["Lab Report", "Project"],
            ["Essay", "Reading"]
        ]
        index = 3
        # Expected output lists tasks for "English"
        expected_output = """English
    1. Essay
    2. Reading
"""
        view_task(subject_list, task_list, index)
        self.assertEqual(self.held_stdout.getvalue(), expected_output)

    def test_case_4(self):
        # Test case for viewing tasks of a subject with no tasks
        subject_list = ["Math", "Science", "English"]
        task_list = [
            [],
            ["Lab Report", "Project"],
            []
        ]
        index = 1
        # Expected output shows no tasks for "Math"
        expected_output = """Math
"""
        view_task(subject_list, task_list, index)
        self.assertEqual(self.held_stdout.getvalue(), expected_output)

    def test_case_5(self):
        # Test case for viewing tasks of a single subject with one task
        subject_list = ["History"]
        task_list = [
            ["Term Paper"]
        ]
        index = 1
        # Expected output lists the single task for "History"
        expected_output = """History
    1. Term Paper
"""
        view_task(subject_list, task_list, index)
        self.assertEqual(self.held_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
