#Weight Giver v2.0

#import os
#import os.path

#path = os.getcwd()

print "Number of students: "
numstud = raw_input()
print "Number of questions: "
numques = raw_input()
#g = {}
#for x in range(int(numstud)):
#    y = "student" + str(x + 1)
#    g[y] = []

question1 = []

print "Import grades from TextEdit [1]"
print "Enter grades manually       [2]"

gra = raw_input()

if gra == "1":

    print "Input TextEdit File In WeightGiver Folder"
    print
    print
    print "-----------------------------------------"
    print "-----NOTE: BE SURE THE FORMAT OF THE-----"
    print "---------------TextEDIT IS:--------------"
    print "(Student1Name)"
    print "(ScoreQuestion1)"
    print "(ScoreQuestion2)"
    print "(ScoreQuestion3)"
    print "(Student2Name)"
    print "-----------------------------------------"
    print "Input File Name: ",
    filename = raw_input()

    with open(filename, "r") as teacher:
        students = []
        for line in teacher:
            students.append(line)

    for x in range(numques):
        #Do another variable to count at what question you are at, therefore
        #knowing how much to add to the x to actually get the value of the
        #score that the student got.
        

if gra == "2":

    print
    



student1 = [.6, .7, .8]
student2 = [.9, .9, .5]
student3 = [.9, .4, .8]
student4 = [.6, .7, .6]

question1 = [student1[0], student2[0], student3[0], student4[0]]
question2 = [student1[1], student2[1], student3[1], student4[1]]
question3 = [student1[2], student2[2], student3[2], student4[2]]

av1 = (question1[0] + question1[1] + question1[2]) / 3

av2 = (question2[0] + question2[1] + question2[2]) / 3

av3 = (question3[0] + question3[1] + question3[2]) / 3

av = [av1, av2, av3]

w = [1, 1, 1, 1, 1, 1]

aver = (((w[0] * av[0]) + (w[1] * av[1]) + (w[2] * av[2]))/(w[0] + w[1]+ w[2])) * 100

averb = aver


#print aver

saver = aver


for s in range(3):

    T = True

    while T:
        w[s] = w[s] + 1
        aver = (((w[0] * av[0]) + (w[1] * av[1]) + (w[2] * av[2]))/(w[0] + w[1]+ w[2])) * 100
        #print w1
        #print aver
        if averb < aver:
            averb = aver

            w[s + 3] = w[s]
        if averb == aver:
            T = False
        if averb > aver:
            T = False
        #print averb



for s in range(3):

    T = True

    while T:
        if not w[s] == 1:
            w[s] = w[s] - 1
        aver = (((w[0] * av[0]) + (w[1] * av[1]) + (w[2] * av[2]))/(w[0] + w[1]+ w[2])) * 100
        #print w1
        #print aver
        if averb < aver:
            averb = aver
            w[s + 3] = w[s]
        if averb == aver:
            T = False
        if averb > aver:
            T = False
        #print averb
    



final1 = int(averb)
final2 = int(saver)
final = final1 - final2


print "Final class Average: " + str(int(averb))
print "Starting class Average: " + str(int(saver))
print "Percentage Increase: " + str(final)
print "Weight for question 1: " + str(w[3])
print "Weight for question 2: " + str(w[4])
print "Weight for question 3: " + str(w[5])

