import unittest

def test_palindrome(string=None):
    reverse=[]
    for i in range(len(string)-1, -1, -1):
        reverse.append(string[i])
    return ''.join(reverse)

def test_palindrome2(string=None):
    len_string = len(string)
    if len_string // 2 != 0:
        start = 0
        end = len_string - 1
        while start < end:
            if string[start] != string[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
    else:
        return False

class test_palindromes(unittest.TestCase):
    def test(self):
        self.assertEqual(test_palindrome('malayalam'), 'malayalam')
        self.assertTrue(test_palindrome2('malayalam'), True)


if __name__ == '__main__':
    unittest.main()
