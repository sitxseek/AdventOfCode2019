import unittest
import puzzle

class TestDay1(unittest.TestCase):
    def test_part_one(self):
        file = open("input.txt", "r")
        data = puzzle.parse(file.readlines())
        answer = puzzle.solvePartOne(data)
        self.assertEqual(3488702, answer)
        file.close()

    def test_part_two(self):
        file = open("input.txt", "r")
        data = puzzle.parse(file.readlines())
        answer = puzzle.solvePartTwo(data)
        self.assertEqual(5230169, answer)
        file.close()

    def test_basic(self):
        answer = puzzle.solvePartOne([12, 14, 1969])
        self.assertEqual(658, answer)
        answer = puzzle.solvePartTwo([100756])
        self.assertEqual(50346, answer)

if __name__ == '__main__':
    unittest.main()