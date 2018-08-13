import unittest

def array_chunk(array=None, size=None):
    return [array[i:i+size] for i in range(0, len(array), size)]

class test_array_chunk(unittest.TestCase):
    def test(self):
        self.assertEqual(array_chunk([1,2,3,4,5,6,7,8,9,10], 3), [[1,2,3],[4,5,6],[7,8,9],[10]])
        self.assertEqual(array_chunk([1,2,3,4,5], 10), [[1,2,3,4,5]])

if __name__ == '__main__':
    unittest.main()