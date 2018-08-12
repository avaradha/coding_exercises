import unittest

def reverse_string(string=None):
    reverse = []
    if len(string) > 2:
        for i in range(len(string)-1, -1, -1):
            reverse.append(string[i])
        return ''.join(reverse)
    else:
        return string
    pass

class test_reverse_string(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_string('apple'), 'elppa')


if __name__ == '__main__':
    unittest.main()