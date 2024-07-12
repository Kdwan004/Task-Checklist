import unittest
from unittest.mock import patch
from io import StringIO
import sys
from directory import direct  

direct()  

from subject import add_subject

class TestAddSubject(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_add_subject_valid_input(self):
        # Test case for adding a subject successfully
        subject_list = []
        task_list = []
        input_values = ['Math', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list, updated_task_list = add_subject(subject_list, task_list)
            self.assertEqual(updated_subject_list, ['Math'])
            self.assertEqual(updated_task_list, [[]])

    def test_add_subject_multiple_subjects(self):
        # Test case for adding multiple subjects
        subject_list = []
        task_list = []
        input_values = ['Math', 'Science', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list, updated_task_list = add_subject(subject_list, task_list)
            self.assertEqual(updated_subject_list, ['Math', 'Science'])
            self.assertEqual(updated_task_list, [[], []])

    def test_add_subject_exit_without_adding(self):
        # Test case for exiting without adding any subjects
        subject_list = []
        task_list = []
        input_values = ['--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list, updated_task_list = add_subject(subject_list, task_list)
            self.assertEqual(updated_subject_list, [])
            self.assertEqual(updated_task_list, [])
    def test_add_subject_empty_input(self):
        # Test case for empty subject input
        subject_list = []
        task_list = []
        input_values = ['', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list, updated_task_list = add_subject(subject_list, task_list)
            self.assertEqual(updated_subject_list, [''])
            self.assertEqual(updated_task_list, [[]])

    def test_add_subject_special_characters(self):
        # Test case for special characters in subject input
        subject_list = []
        task_list = []
        input_values = ['@!#$', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list, updated_task_list = add_subject(subject_list, task_list)
            self.assertEqual(updated_subject_list, ['@!#$'])
            self.assertEqual(updated_task_list, [[]])

    def test_add_subject_numeric_input(self):
        # Test case for numeric subject input
        subject_list = []
        task_list = []
        input_values = ['1234', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list, updated_task_list = add_subject(subject_list, task_list)
            self.assertEqual(updated_subject_list, ['1234'])
            self.assertEqual(updated_task_list, [[]])

if __name__ == '__main__':
    unittest.main()

