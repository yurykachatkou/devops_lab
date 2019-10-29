import unittest
import task2


class TestNum(unittest.TestCase):

    def test_task2largest(self):
        self.assertEqual(task2.largest(1234567890), 9876543210)
        self.assertEqual(task2.largest(-9876543210), -1023456789)
        self.assertEqual(task2.largest(0), 0)

    def test_task2smallest(self):
        self.assertEqual(task2.smallest(9876543210), 1023456789)
        self.assertEqual(task2.smallest(-1234567890), -9876543210)
        self.assertEqual(task2.smallest(0), 0)


if __name__ == "__main__":
    unittest.main()
