# QUESTION

# Class Record 
# You are given a dataset of N students belonging to the same class.
# The data contains name of the student followed by marks they scored in five subjects which are Physics, Chemsistry, Maths, English, Hindi.
# Your task is find the average marks of the class for each individual subject.

# Input Format
# First line will contain an Integer N, denoting  the number of students in the class.
# Each of the Next N lines will contain a string S denoting the student name, followed by five integers m1, m2, m3, m4, m5 denoting the marks scored in each subject.

# Constraints
# 1 <= N <= 10^3
# 1 <= S <= 10^2
# 0 <= m1, m2, m3, m4, m5 <= 100

# Output Format
# You have to print average marks upto two decimal places for each subject followed by a space. 

# SOLUTION

cases=int(input())
if 1<=cases<=1000:
    the_list=[]
    for i in range(cases):
        z=list(map(str,input().strip().split()))
        if 1<=len(z[0])<=100:
            the_list.append(z)
        else:   exit()
    a=b=c=d=e=float(0)
    for i in the_list:
        try:
            if 0.0 <= float(i[1])<= 100.0 and 0.0 <= float(i[2])<= 100.0 and 0.0 <= float(i[3])<= 100.0 and 0.0 <=float(i[4])<= 100.0 and 0.0 <= float(i[5])<= 100.0:
                a+=float(i[1])
                b+=float(i[2])
                c+=float(i[3])
                d+=float(i[4])
                e+=float(i[5])
        except:
            exit()
    print("%0.2f %0.2f %0.2f %0.2f %0.2f"%(a/len(the_list),b/len(the_list),c/len(the_list),d/len(the_list),e/len(the_list)))



