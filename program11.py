# QUESTION
# Collections-NamedTuple
# Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
# You are given a data containing test results of class. The dataset consists of two columns namely : 'marks' and 'name'. These two Columns can be in any order i.e. ('name' followed by 'marks' or vice versa).
# You have to find the average marks for the whole class.


# Input Format
# First line will contain an Integer N, denoting the number of students.
# Next line will contain two string denoting the column heading.
# Next N lines will contain marks and name of the students respective of column headings.


# Constraints
# 1 <= N <= 10^3
# 0 <= Marks <= 100


# Output Format
# Output the average marks of the class rounded off to two decimal places.

# Sample TestCase 1
# Input
# 3
# marks names
# 10 arpit
# 20 anushka
# 35 rakshita
# Output
# 21.67

# SOLUTION

from collections import namedtuple
cases =int(input())
m = list(map(str,input().strip().split(" ")))
student = namedtuple('student',[m[0],m[1]])
d= 0
for i in range(cases):
    info = list(map(str,input().strip().split(" ")))
    sending = student(info[0],info[1])
    d+=int(sending.marks)
print("%0.2f"%(float(d/cases)))
