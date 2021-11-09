# QUESTIONS

# CITIES 
# N applicants have applied for a job in XYZ company. They have a thing for a diversity and want to know the distinct number of cities from which applicants have applied.




# Input Format
# The first line of input consist of number of applicants, N

# Next N lines consist of the cities of applicants




# Constraints
# 1<= N <=25




# Output Format
# Print the distinct number of cities




# Sample TestCase 1
# Input
# 5
# DELHI
# DELHI
# CHENNAI
# BANGALORE
# AMRITSAR
# Output
# 3

# SOLUTIONS
cases = int(input())
count = {}
as_list = []
for j in range(cases):
    as_list.append(input())
for i in as_list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
the_list = []
for key,values in count.items():
    if count[key]==1:
        the_list.append(i)
print(len(the_list))
