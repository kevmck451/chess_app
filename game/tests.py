from django.test import TestCase, Client
from django.urls import reverse
from .engine import MiniMax
import math

class EngineTestCase(TestCase):
    def test_evaluate_initial_position(self):
        # Initial board setup
        board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]


        # Call the evaluate function for white
        eval_white = evaluate(board, True)
        # Call the evaluate function for black
        eval_black = evaluate(board, False)
        
        # The initial evaluation should be 0 since both sides have parity in material
        self.assertEqual(eval_white, 0)
        self.assertEqual(eval_black, 0)



class MiniMaxTestCase(TestCase):
    def setUp(self):
        # Set up a board state
        self.board = [
            # board state here
        ]
        self.depth = 3
        self.alpha = -math.inf
        self.beta = math.inf
        self.color = True  # or False, depending on the test

    def test_minimax(self):
        # Run the MiniMax function
        score, best_move, counter = MiniMax(self.board, self.depth, self.alpha, self.beta, self.color)
        
        # replace 'expected_score' and 'expected_move' with
        # actual values expected for the given board state.
        expected_score = # score you expect
        expected_move = # move you expect

        self.assertEqual(score, expected_score)
        self.assertEqual(best_move, expected_move)


class BoardViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_board_state_on_load(self):
        response = self.client.get(reverse('board'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('board', response.context)

    def test_ajax_move(self):
        # set up session variables and then make an AJAX request.
        # Simulate an AJAX request by sending the appropriate headers.
        response = self.client.post(reverse('board'), {
            'sqId': 'e2', 'newSqId': 'e4', 'oldSqId': 'e2'
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
    
    def test_reset_board(self):
        # Make a series of moves on the board
        self.client.post(reverse('board'), {'sqId': 'e2', 'newSqId': 'e4', 'oldSqId': 'e2'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.client.post(reverse('board'), {'sqId': 'e7', 'newSqId': 'e5', 'oldSqId': 'e7'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        # Reset the board
        response = self.client.get(reverse('resetBoard'))
        self.assertEqual(response.status_code, 302)  # Check if the response is a redirect

        # Check if the board state is reset to the initial state
        response = self.client.get(reverse('board'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('board', response.context)
        self.assertEqual(response.context['board'], [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ])

        def test_invalid_move(self):
        # Make an invalid move by sending incorrect parameters
        response = self.client.post(reverse('board'), {'sqId': 'e2', 'newSqId': 'e4'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 400)  # Check if the response is a Bad Request
        # Check other parts of the response as needed.


