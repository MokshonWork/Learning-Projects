import unittest
from unittest.mock import patch, call
import io
import sys

# Assuming project1.py is refactored and in the same directory or accessible via PYTHONPATH
from project1 import determine_winner, get_user_choice_value, get_choice_name, play_round, youdict, reversedict

class TestSnakeWaterGun(unittest.TestCase):

    def test_get_user_choice_value(self):
        self.assertEqual(get_user_choice_value("s"), 1)
        self.assertEqual(get_user_choice_value("S"), 1)
        self.assertEqual(get_user_choice_value("w"), -1)
        self.assertEqual(get_user_choice_value("W"), -1)
        self.assertEqual(get_user_choice_value("g"), 0)
        self.assertEqual(get_user_choice_value("G"), 0)
        self.assertIsNone(get_user_choice_value("x")) # Invalid input

    def test_get_choice_name(self):
        self.assertEqual(get_choice_name(1), "snake")
        self.assertEqual(get_choice_name(-1), "water")
        self.assertEqual(get_choice_name(0), "gun")
        self.assertIsNone(get_choice_name(5)) # Invalid value

    def test_determine_winner(self):
        # Constants for choices for clarity
        SNAKE = 1
        WATER = -1
        GUN = 0

        # Test Draw conditions
        self.assertEqual(determine_winner(SNAKE, SNAKE), "Draws")
        self.assertEqual(determine_winner(WATER, WATER), "Draws")
        self.assertEqual(determine_winner(GUN, GUN), "Draws")

        # Test "You win!" conditions (user wins)
        # (computer - user) == 1  OR (computer - user) == -2
        # User: Water (-1) vs Computer: Gun (0) -> comp - user = 0 - (-1) = 1
        self.assertEqual(determine_winner(GUN, WATER), "You win!")
        # User: Gun (0) vs Computer: Snake (1) -> comp - user = 1 - 0 = 1
        self.assertEqual(determine_winner(SNAKE, GUN), "You win!")
        # User: Snake (1) vs Computer: Water (-1) -> comp - user = -1 - 1 = -2
        self.assertEqual(determine_winner(WATER, SNAKE), "You win!")

        # Test "You lose!" conditions (user loses)
        # User: Snake (1) vs Computer: Gun (0) -> comp - user = 0 - 1 = -1
        self.assertEqual(determine_winner(GUN, SNAKE), "You lose!")
        # User: Water (-1) vs Computer: Snake (1) -> comp - user = 1 - (-1) = 2
        self.assertEqual(determine_winner(SNAKE, WATER), "You lose!")
        # User: Gun (0) vs Computer: Water (-1) -> comp - user = -1 - 0 = -1
        self.assertEqual(determine_winner(WATER, GUN), "You lose!")

    @patch('project1.random.choice')
    @patch('builtins.input')
    def test_play_round_user_wins(self, mock_input, mock_random_choice):
        # Scenario: User picks Snake ('s'), Computer picks Water (-1) -> User wins
        mock_input.return_value = 's' # User chooses Snake
        mock_random_choice.return_value = -1 # Computer chooses Water

        # Capture print statements
        captured_output = io.StringIO()
        sys.stdout = captured_output

        result, user_choice_name, computer_choice_name = play_round()

        sys.stdout = sys.__stdout__  # Reset redirect.

        self.assertEqual(result, "You win!")
        self.assertEqual(user_choice_name, "snake")
        self.assertEqual(computer_choice_name, "water")
        
        output_str = captured_output.getvalue()
        self.assertIn("You choose: snake", output_str)
        self.assertIn("Computer choose: water", output_str)
        self.assertIn("You win!", output_str)

    @patch('project1.random.choice')
    @patch('builtins.input')
    def test_play_round_draw(self, mock_input, mock_random_choice):
        # Scenario: User picks Gun ('g'), Computer picks Gun (0) -> Draw
        mock_input.return_value = 'g' 
        mock_random_choice.return_value = 0 

        captured_output = io.StringIO()
        sys.stdout = captured_output
        result, user_choice_name, computer_choice_name = play_round()
        sys.stdout = sys.__stdout__

        self.assertEqual(result, "Draws")
        self.assertEqual(user_choice_name, "gun")
        self.assertEqual(computer_choice_name, "gun")
        self.assertIn("You choose: gun", captured_output.getvalue())
        self.assertIn("Computer choose: gun", captured_output.getvalue())
        self.assertIn("Draws", captured_output.getvalue())

    @patch('project1.random.choice')
    @patch('builtins.input')
    def test_play_round_user_loses_with_invalid_then_valid_input(self, mock_input, mock_random_choice):
        # Scenario: User first enters invalid, then picks Snake ('s'), Computer picks Gun (0) -> User loses
        mock_input.side_effect = ['x', 's'] # Invalid input, then valid input
        mock_random_choice.return_value = 0 # Computer chooses Gun

        captured_output = io.StringIO()
        sys.stdout = captured_output
        result, user_choice_name, computer_choice_name = play_round()
        sys.stdout = sys.__stdout__

        self.assertEqual(result, "You lose!")
        self.assertEqual(user_choice_name, "snake")
        self.assertEqual(computer_choice_name, "gun")
        self.assertIn("Invalid input. Please enter 's', 'w', or 'g'.", captured_output.getvalue())
        self.assertIn("You choose: snake", captured_output.getvalue())
        self.assertIn("Computer choose: gun", captured_output.getvalue())
        self.assertIn("You lose!", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()