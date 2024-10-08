from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.testCases = {
            1: {'nums': [2,3,1,1,4], 'output': True},
            2: {'nums': [3,2,1,0,4], 'output': False}
        }

        self.obj = Solution()

        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        nums, output = self.testCases[1].values()
        result = self.obj.canJump(nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        nums, output = self.testCases[2].values()
        result = self.obj.canJump(nums)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()