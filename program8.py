# QUESTION

# Managing Bank
# You are working as a Manager in a bank. At the end of the day, You have to send a report to your supervisors which consists of count of distinct accounts that were operated upon on that particular day.
# You are given a list containing the account numbers of the customers of the bank according to their time of arrival in the bank.
# You have to tell the count of distinct accounts.

# Input Format
# First line will contain N, denoting the total number of entries in the list.
# Next line will contain N account numbers separated by space.

# Constraints
# 1 <= N <= 10^3
# 1 <= Account Number <= 10^2

# Output Format
# Output the count of distinct accounts for a particular day.

# Sample TestCase 1
# Input
# 5
# 1 2 3 1 3
# Output
# 3


# SOLUTION

cases = int(input())
the_list = list(map(int,input().strip().split()))
count = {}
for i in the_list:
    if i in count:
        count[i] +=1
    else:
        count[i]=1
d = 0
for key,value in count.items():
    d+=1
print(d)