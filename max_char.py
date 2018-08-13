import unittest
def max_char(string=None):
    char_count={}
    for i in range(128):
        char_count[chr(i)] = 0
    for i in string:
        char_count[i] += 1
    _, k = max((v, k) for k, v in char_count.items())
    return k

def max_char2(string=None):
    char_count = {}
    for i in string:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    print(char_count)
    _, k = max((v, k) for k, v in char_count.items())
    return k

class test_max_char(unittest.TestCase):
    def test(self):
        self.assertEqual(max_char('Hello there'), 'e')
        self.assertEqual(max_char2('Hello there'), 'e')

if __name__ == '__main__':
    unittest.main()