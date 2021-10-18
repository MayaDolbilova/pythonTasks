#!/usr/bin/env python
# coding: utf-8
def average_marks(li, k):
    count_rus = 0
    count = 0
    for i in li:
        count_rus += int(i[k])
        count += 1
    rus = str(int(count_rus / count))
    return rus

fileptr = open("For_final_task_2.txt", "r")
s = []
l = []
average=[]

for i in fileptr:
    a=i.split(";")
    s.append(a)


for i in s:
    resu=str(int((int(i[1])+int(i[2])+int(i[3]))/3))
    l.append(resu)
rus = average_marks(s, 1)
phisics = average_marks(s, 2)
math = average_marks(s, 3)
average.append("Total results:")
average.append(rus)
average.append(phisics)
average.append(math)
print(average)

k=0
while k<len(l):
    for i in s:
        i.append(l[k])
        i.append("\n")
        k+=1
s.append(average)
print(s)

for i in s:
    heh='/'.join(i)
    print(heh)
    write_to_f=open("For_final_task_2.txt", "a")
    write_to_f.write(heh)










