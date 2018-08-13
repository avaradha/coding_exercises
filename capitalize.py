import unittest

def capitalize(string=None):
    return ' '.join([item[0].upper() + item[1:] for item in string.split()])

def capitalize2(string=None):
    result = string[0].upper()
    for i in range(1, len(string), 1):
        if string[i-1] == ' ':
            result += string[i].upper()
        else:
            result += string[i]
    return result


class test_capitalize(unittest.TestCase):
    def test(self):
        self.assertEqual(capitalize('hi there how are you'), 'Hi There How Are You')
        self.assertEqual(capitalize2('hi there how are you'), 'Hi There How Are You')

if __name__ == '__main__':
    unittest.main()