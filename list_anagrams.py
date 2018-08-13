import unittest

def test_anagrams(word_list=None, pattern=None):
    list_pattern = list(pattern)
    list_pattern.sort()
    sol_list =[]
    for item in word_list:
        list_item = list(item)
        list_item.sort()
        if list_pattern == list_item:
            sol_list.append(item)
    return sol_list

class test_test_anagrams(unittest.TestCase):
    def test(self):
        words=['test', 'estt','ttst', 'pest']
        pattern = 'test'
        sol = ['test', 'estt']
        self.assertEqual(test_anagrams(words, pattern), sol)

if __name__ == '__main__':
    unittest.main()