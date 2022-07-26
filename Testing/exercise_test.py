import unittest
import exercise


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = exercise.run_guess(answer, guess)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        answer = 5
        guess = 0
        result = exercise.run_guess(answer, guess)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        answer = 5
        guess = 11
        result = exercise.run_guess(answer, guess)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        answer = 5
        guess = '11'
        result = exercise.run_guess(answer, guess)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
