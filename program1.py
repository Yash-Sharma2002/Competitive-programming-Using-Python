# QUESTION
# Asha is working as a teacher in a well known school. She wants to give some chocolates to the children in her class. All the children
# sit in a line (their positions are fixed), and each of them has a rating score according to his or her performance in the class. Asha wants to give at
# least 1 chocolate to each child. If two children sit next to each other, then the one with the higher rating must get more chocolates. Asha wants to save 
# money, so she needs to minimize the total number of chocolates given to the children.

# Input Format
# First line will tell the total number of rows N which denotes the total number of children in Asha's class.
# Next lines contains N integer that indicates the rating of each child.

# Constraints
# 1 <= N <= 10^5
# 1 <=  ratingi <= 10^5

# Output Format
# It will be an integer which contains the minimum number of chocolates Asha must buy.


# SOLUTION
def sum_dict(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
    return sum

num_student = int(input())
if  (1 > num_student or num_student >= 10^5):
    exit()

priority = input()
p_list = list(map(int,priority.split(" ")))
if (max(p_list) < 1 or max(p_list)>=10^5):
    exit()
p_list.append(1)
count = {}
for i in range(0,len(p_list)-1):
    if i%2 == 0:
        if p_list[i]>p_list[i+1]:
            count[i] = 2
        else:
            count[i] = 1
    else:
        if p_list[i]>p_list[i+1]:
            count[i] = 2
        else:
            count[i] = 1
sum = sum_dict(count)
p_list.pop()
print(sum)
exit()