import unittest
from unittest.mock import patch
from io import StringIO
import sys
from directory import direct  

direct()  

from subject import remove_subject

class TestRemoveSubject(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_stdout = StringIO()
        sys.stdout = self.held_stdout

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_remove_subject_valid_removal(self):
        # Test case for valid removal of a subject
        subject_list = ["Math", "Science", "English"]
        input_values = ['2', 'yes', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list = remove_subject(subject_list)
            self.assertEqual(updated_subject_list, ["Math", "English"])

    def test_remove_subject_cancel_removal(self):
        # Test case for cancelling removal of a subject
        subject_list = ["Math", "Science", "English"]
        input_values = ['2', 'no', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list = remove_subject(subject_list)
            self.assertEqual(updated_subject_list, ["Math", "Science", "English"])

    def test_remove_subject_invalid_index(self):
        # Test case for attempting removal with an invalid index
        subject_list = ["Math", "Science", "English"]
        input_values = ['5', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list = remove_subject(subject_list)
            self.assertEqual(updated_subject_list, ["Math", "Science", "English"])
            self.assertIn("ERROR: Index out of range", self.held_stdout.getvalue())

    def test_remove_subject_no_subjects(self):
        # Test case for attempting removal when there are no subjects
        subject_list = []
        input_values = ['--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list = remove_subject(subject_list)
            self.assertEqual(updated_subject_list, [])
            self.assertIn("ERROR: No subjects in the list", self.held_stdout.getvalue())
    
    def test_remove_subject_empty_input(self):
        # Test case for empty input
        subject_list = ["Math", "Science", "English"]
        input_values = ['', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list = remove_subject(subject_list)
            self.assertEqual(updated_subject_list, ["Math", "Science", "English"])
            self.assertIn("ERROR: Index out of range", self.held_stdout.getvalue())

    def test_remove_subject_non_numeric_input(self):
        # Test case for non-numeric input
        subject_list = ["Math", "Science", "English"]
        input_values = ['abc', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list = remove_subject(subject_list)
            self.assertEqual(updated_subject_list, ["Math", "Science", "English"])
            self.assertIn("ERROR: Index out of range", self.held_stdout.getvalue())

    def test_remove_subject_out_of_bounds_high(self):
        # Test case for index out of bounds (high)
        subject_list = ["Math", "Science", "English"]
        input_values = ['10', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list = remove_subject(subject_list)
            self.assertEqual(updated_subject_list, ["Math", "Science", "English"])
            self.assertIn("ERROR: Index out of range", self.held_stdout.getvalue())

    def test_remove_subject_out_of_bounds_low(self):
        # Test case for index out of bounds (low)
        subject_list = ["Math", "Science", "English"]
        input_values = ['-1', '--']
        with patch('builtins.input', side_effect=input_values):
            updated_subject_list = remove_subject(subject_list)
            self.assertEqual(updated_subject_list, ["Math", "Science", "English"])
            self.assertIn("ERROR: Index out of range", self.held_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()

