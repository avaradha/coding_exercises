import unittest
import sys
 
# A utility function to print a
# substring str[low..high]
def printSubStr(st,low,high) :
    sys.stdout.write(st[low : high + 1])
    sys.stdout.flush()
    return ''

def longest_pal_substring(string=None):
    n = len(string)
    table =[[0 for x in range(n)] for y in range(n)]
    # print(table)

    # Check for string length of 1
    max_length = 1
    i = 0
    while i < n:
        table[i][i] = True
        i += 1
    # print(table)

    # Check for string of length 2
    start = 0
    i = 0
    while i < n - 1:
        if (string[i] == string[i + 1]):
            table[i][i + 1] = True
            start = i
            max_length = 2
        i = i + 1
    # print(table)

    # check for length greater than 2
    k = 3
    while k <=n:
        i = 0
        while i < (n - k + 1):
            # Get the ending index of 
            # substring from starting 
            # index i and length k
            j = i + k -1

            # checking for sub-string from
            # ith index to jth index iff 
            # st[i+1] to st[(j-1)] is a 
            # palindrome
            if (table[i + 1][j - 1] and string[i] == string[j]):
                table[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k
            i = i + 1
        k = k + 1
    for i in range(len(table)):
        print(table[i])
    print(start, start+max_length)
    print "Longest palindrome substring is: ", printSubStr(string, start, start + max_length - 1)
    return string[start:start+max_length]


class check_longestPalSubstring(unittest.TestCase):
    def test(self):
        # self.assertEqual(longest_pal_substring('aabbbaa'), 'aabbbaa')
        self.assertEqual(longest_pal_substring('forgeeksskeegfor'), 'geeksskeeg')


if __name__ == '__main__':
    unittest.main()