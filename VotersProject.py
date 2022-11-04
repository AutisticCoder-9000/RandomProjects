'''Write a program in Python to create a file “VOTERS.csv” containing
VoterId, VoterName, VoterAge having comma as a delimiter. Later,
read the file and display those records where voter age is greater than
65.'''

import csv
n=int(input("enter the no.of voters"))
f=open("voters.csv","w",newline="")
w=csv.writer(f)

for i in range(n):
     vID=int(input("enter the Voter ID"))
     VName=input("enter the name")
     VAge=int(input("enter the Age"))
     w.writerow([vID,VName,VAge])

f.close()

f=open("voters.csv","r")
r=csv.reader(f)
l=list(r)
for i in l:
     if int(i[2])>65:
          print(i)
     else:
          pass

f.close()
