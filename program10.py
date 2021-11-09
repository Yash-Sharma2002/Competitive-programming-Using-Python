# QUESTIONS
# Collections-Counter
# Collections module implements specialized container datatypes providing alternatives to Python s general purpose built-in containers, dict, list, set, and tuple.
# A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.
# Your task is to find the top two most recurring characters in a given string using most_common() function of the module.

# Input Format
# First line will contain a string s.

# Constraints
# 1 <= |s| <= 10^3

# Output Format
# Output the two most recurring characters in the string along with their frequencies. 

# Sample TestCase 1
# Input
# asdasddds
# Output
# ('d', 4) ('s', 3)

# SOLUTION

from collections import Counter
case = list(input())
l =Counter(case).most_common(2)
l1=l[0][0] 
c1=l[0][1] 
l2=l[1][0] 
c2=l[1][1] 
if c1==c2: 
    t=l1 
    l1=l2 
    l2=t 
print("('{}', {}) ('{}', {})".format(l1,c1,l2,c2), end="")