import unittest
import puzzle

class TestDay2(unittest.TestCase):
    def test_part_one(self):
        f = open("test_input.txt", "r")
        data = puzzle.parse(f.read())
        answer = puzzle.solvePartOne(data)
        self.assertEqual(30, answer)
        f.close()

if __name__ == '__main__':
    unittest.main()