import os
import random

def create_exam(fname):
    arr = os.listdir('pools')
    exam = open(fname,"w")
    for patch in arr:
        ddd = os.listdir('pools/'+patch)
        file_name = random.choice(ddd)
        f = open("pools/"+patch+"/"+file_name,"r",encoding='utf-8')
        read = f.read()
        exam.write(read)
        exam.write("\n")
        exam.write("\n")
    exam.close()

j=int(input("Количество билетов "))

for i in range(j):
    create_exam("exam"+str(i)+".txt")
    print(i)
print("Билеты ищите в папке exam")
print("Перед повторным созданием билетов удалите/переместите старые")