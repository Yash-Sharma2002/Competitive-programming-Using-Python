# QUESTION
# Prime Game (100 Marks)
# Rax, a school student, was bored at home in the pandemic. He wanted to play but there was no one to play with. He was doing some mathematics questions including prime numbers and thought of creating a game using the same. After a few days of work, he was ready with his game. He wants to play the game with you.


# GAME:

# Rax will randomly provide you a range [ L , R ] (both inclusive) and you have to tell him the maximum difference between the prime numbers in the given range. There are three answers possible for the given range.

# There are two distinct prime numbers in the given range so the maximum difference can be found.

# There is only one distinct prime number in the given range. The maximum difference in this case would be 0.

# There are no prime numbers in the given range. The output for this case would be -1.


# To win the game, the participant should answer the prime difference correctly for the given range.


# Example:

# Range: [ 1, 10 ]

# The maximum difference between the prime numbers in the given range is 5.

# Difference = 7 - 2 = 5


# Range: [ 5, 5 ]

# There is only one distinct prime number so the maximum difference would be 0.


# Range: [ 8 , 10 ]

# There is no prime number in the given range so the output for the given range would be -1.


# Can you win the game?



# Input Format
# The first line of input consists of the number of test cases, T

# Next T lines each consists of two space-separated integers, L and R



# Constraints
# 1<= T <=10

# 2<= L<= R<=10^6

# SOLUTION
import math
def find_prime(a,b):
    prime = []
    for i in range(a,b+1):
        flag = 0
        max_div = math.floor(math.sqrt(i))
        for j in range(2,max_div+1):
            if i%j==0:
                flag=1
        if flag==0:
            prime.append(i)
    return prime

total_case = int(input())
if total_case<1 or total_case>10:
    exit()
for i in range(total_case):
    num1 = input()
    the_list = []
    for i in num1.split():
        z = i.strip(" ")
        the_list.append(int(z))
    u,v = the_list[0],the_list[1]
    if u<2 or u>100000 or v<2 or v>100000:
        print("Out of range")
    else:
        prime = find_prime(u,v)
        if prime==[]:
            print(-1)
        elif len(prime)==1:
            print(0)
        else:
            print(prime[-1]-prime[0])
# exit()