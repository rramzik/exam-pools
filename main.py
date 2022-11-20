import os
import random

def create_exam(fname):
    arr = os.listdir('pools')
    exam = open(fname,"w")
    for patch in arr:
        ddd = os.listdir('pools/'+patch)
        file_name = random.choice(ddd)
        f = open("pools/"+patch+"/"+file_name,"r")
        #print(f.read())
        exam.write(f.read())
        exam.write("\n")
        exam.write("\n")
    exam.close()

j=int(input())
for i in range(j):
    create_exam("exam"+str(i)+".txt")
