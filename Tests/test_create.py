import sys
import unittest
from unittest.mock import patch

sys.path.insert(1, '/home/bleachly/Desktop/tasks')

import create

class TestCreate(unittest.TestCase):

    # Initialise mock input
    def setUp(self):
        self.subject_list = []
    
    
    # @Path replaces real object in code with mock instances
    # Test the input of 1 subject
    @patch('builtins.input', side_effect=["Math", "yes"])
    def test_add_subject(self, mock_input):
        create.list_subject(self.subject_list)
        self.assertEqual(self.subject_list, ["Math"])
    
    # Test if user decided to rename subject
    @patch('builtins.input', side_effect=["", "no", "English", "yes"])
    def test_redo_subject(self, mock_input):
        create.list_subject(self.subject_list)
        self.assertEqual(self.subject_list, ["English"])

    # Test if user exits function before making any changed
    @patch('builtins.input', side_effect=["back"])
    def test_user_back(self, mock_input):
        create.list_subject(self.subject_list)
        self.assertEqual(self.subject_list, [])

    
