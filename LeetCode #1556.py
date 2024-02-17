''' QUESTION:
1556. Thousand Separator
Easy
Topics
Companies
Hint
Given an integer n, add a dot (".") as the thousands separator and return it in string format.

 

Example 1:

Input: n = 987
Output: "987"
Example 2:

Input: n = 1234
Output: "1.234"
 

Constraints:

0 <= n <= 231 - 1

'''SOLUTION:'''

class Solution(object):
    def thousandSeparator(self, n):
        string = str(n)
        length = len(string)
        array = []
        if length >= 4:
            array = list(string)
            array.insert(1,".")
            return str("".join(array))
        else:
            return str(n)