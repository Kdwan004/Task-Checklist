import sys
import unittest
from unittest.mock import patch

sys.path.insert(1, '/home/bleachly/Desktop/tasks')

import subject

class TestSubject(unittest.TestCase):

    # Initialise mock input
    def setUp(self):
        self.subject_list = []
    

    # @Path replaces real object in code with mock instances
    # Test the input of 1 subject
    @patch('builtins.input', side_effect=["Math", "yes"])
    def test_add_subject(self, mock_input):
        subject.list_subject(self.subject_list)
        self.assertEqual(self.subject_list, ["Math"])
    
    # Test if user decided to rename subject
    @patch('builtins.input', side_effect=["", "no", "English", "yes"])
    def test_redo_subject(self, mock_input):
        subject.list_subject(self.subject_list)
        self.assertEqual(self.subject_list, ["English"])


    
