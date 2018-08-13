import unittest

def convert_to_dict(string=None):
    _dict = {}
    for i in string:
        if i in _dict:
            _dict[i] += 1
        else:
            _dict[i] = 1
    print(_dict)
    return _dict

def is_anagram(string1=None, string2=None):
    _dict1 = convert_to_dict(string1)
    _dict2 = convert_to_dict(string2)
    if cmp(_dict1, _dict2) == 0:
        return True
    else:
        return False


class test_is_anagram(unittest.TestCase):
    def test(self):
        self.assertTrue(is_anagram('test', 'estt'))

if __name__ == '__main__':
    unittest.main()