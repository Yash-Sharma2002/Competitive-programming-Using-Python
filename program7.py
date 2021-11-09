# QUESTION

# Second Highest
# There are a total N students present in today's class. You are given student names and their respective height (in cms).
# You have to find names of all the second highest students (according to their heights).
# If there are multiple students , print each name on new line.

# Input Format
# First line will contain an Integer N, denoting the number of students.
# Next 2 * N lines contains description of each student. first line contains name of the student and second line contains height of the student.

# Constraints
# 1 <= N <= 100

# Output Format
# Print name of all the students having second highest height in alphabetical order.

# SOLUTION

cases = int(input())
the_dict = {}
for i in range(cases):
    x,y=input(),int(input())
    the_dict[x] = y
a=sorted(the_dict.values(),reverse=True)
s=0
for i in a:
    if i<max(a):
        s=i
        break
the_list =[]
for key,value in the_dict.items():
    if value==i:
        the_list.append(key)
the_list = sorted(the_list)
for i in the_list:
    print(i)