import unittest
from io import StringIO
import sys
from directory import direct

direct()
from task import view_all_tasks


class TestViewAllTasks(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_case_1(self):
        # Test case with multiple subjects, each having multiple tasks
        subject_list = ["Math", "Science", "English"]
        task_list = [
            ["Homework 1", "Homework 2"],
            ["Lab Report", "Project"],
            ["Essay", "Reading"]
        ]
        # Expected output lists all subjects with their respective tasks
        expected_output = """1. Math
    1. Homework 1
    2. Homework 2
2. Science
    1. Lab Report
    2. Project
3. English
    1. Essay
    2. Reading
"""
        view_all_tasks(subject_list, task_list)
        self.assertEqual(self.held_stdout.getvalue(), expected_output)

    def test_case_2(self):
        # Test case with some subjects having no tasks
        subject_list = ["Math", "Science", "English"]
        task_list = [
            [],
            ["Lab Report", "Project"],
            []
        ]
        # Expected output shows EMPTY for subjects with no tasks
        expected_output = """1. Math
    EMPTY
2. Science
    1. Lab Report
    2. Project
3. English
    EMPTY
"""
        view_all_tasks(subject_list, task_list)
        self.assertEqual(self.held_stdout.getvalue(), expected_output)

    def test_case_3(self):
        # Test case with a single subject having no tasks
        subject_list = ["History"]
        task_list = [
            []
        ]
        # Expected output shows EMPTY for the single subject
        expected_output = """1. History
    EMPTY
"""
        view_all_tasks(subject_list, task_list)
        self.assertEqual(self.held_stdout.getvalue(), expected_output)

    def test_case_4(self):
        # Test case with multiple subjects, some with tasks and some without
        subject_list = ["Geography", "Physics"]
        task_list = [
            ["Map Study"],
            []
        ]
        # Expected output lists tasks for the first subject and EMPTY for the second
        expected_output = """1. Geography
    1. Map Study
2. Physics
    EMPTY
"""
        view_all_tasks(subject_list, task_list)
        self.assertEqual(self.held_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
