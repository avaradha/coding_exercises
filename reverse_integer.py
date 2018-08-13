import unittest

def reverse_int(num=None):
    reversed = []
    negative = False
    if num < 0:
        negative = True
        num = abs(num)
    while num // 10 > 0:
        reversed.append(num % 10)
        num = num // 10
    reversed.append(num)
    reversed_integer = int(''.join(map(str, reversed)))
    if negative:
        return reversed_integer * -1
    else:
        return reversed_integer

class test_reversed_int(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_int(981), 189)
        self.assertEqual(reverse_int(-500), -5)

if __name__ == '__main__':
    unittest.main()