# QUESTIONS

# Python Lists 
# List is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that items in a list need not be of the same type.
# Your task is to maintain a list and perform two types of queries on it : 
# Query '1' : It will be given as 1 x  : Insert x into the list.
# Query '2' : It will be given as 2 : Print the contents of the list.

# Input Format
# First line will contain an Integer Q, denoting the number of Queries.
# Next Q lines contains an Integer denoting query type.
# Type 1 Query is followed by a data item (integer or a sting) which is to be inserted into the list.

# Constraints
# 1 <= Q <= 10^3

# Output Format
# For each type 2 query, print the contents of the list in new line.

# SOLUTION 

cases = int(input())
the_list = []
for i in range(cases):
    x=input()
    if x[0]=='1':
        the_list.append(x[2:].strip())
    elif x[0]=='2':
        print(the_list)
    
