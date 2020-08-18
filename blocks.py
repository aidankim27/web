import webbrowser as wb
import smtplib
from schooltldr.models import User
from datetime import datetime


smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.ehlo()
smtp.login("botemailsender12345@gmail.com", "Abc!2345678")

dayslist = []
gradesgoing = []
rotation = []
print("Input day as month.day. example: 8.12")
day = float(input())
file = open("sched.txt", "r+")


def makelists(file, dayslist, gradesgoing, rotation):
    for i in range(20):
        currentline = file.readline()
        currentline = currentline.replace("Aug", "8")
        currentline = currentline.replace("Sep", "9")
        currentline = currentline.replace("Oct", "10")
        currentline = currentline.replace("Nov", "11")
        currentline = currentline.replace("Dec", "12")
        currentline = currentline.replace(" ", "")
        currentline = currentline.replace("\n", "")
        dayslist.append(currentline)
    for i in range(20):
        currentline = file.readline()
        currentline = currentline.replace(" & ", " ")
        currentline = currentline.replace("\n", "")
        currentline = currentline.replace("th", "")
        gradesgoing.append(currentline)
    for i in range(20):
        currentline = file.readline()
        currentline = currentline.replace(" ", "")
        currentline = currentline.replace("\n", "")
        if currentline != "Skinny" and len(currentline) > 1:
            currentline = currentline.split(",")
            rotation.append(currentline)
        else:
            rotation.append(currentline)


def check(dayslist, gradesgoing, day, grade, email, rotation):
    for i in range(len(dayslist)):
        if len(dayslist[i]) > 5:  # checking if it is a range
            if (
                float(dayslist[i][0 : dayslist[i].find("-")])
                <= day
                <= float(dayslist[i][dayslist[i].find("-") + 1 : len(dayslist) - 1])
            ):
                daygrades = gradesgoing[i]
                body = "Schedule: "
                break
        else:
            if float(dayslist[i]) == day:
                daygrades = gradesgoing[i]
                body = "Schedule: "
                body += rotation[i]
                break
    if int(daygrades[0]) == grade or int(daygrades[2]) == grade:
        print("working")
        subject = "You are going to school today"
    else:
        subject = "You are not going to school today"
    msg = f"Subject:{subject}\n\n{body}"
    smtp.sendmail("botemailsender12345@gmail.com", email, msg)
    print("Email Sent")


makelists(file, dayslist, gradesgoing, rotation)
print(rotation)
accs = open("accs.txt", "r")
line = accs.readline()
while len(line) > 0:
    line = line.replace("\n", "")
    linelist = line.split(",")
    check(dayslist, gradesgoing, day, int(linelist[1]), linelist[0], rotation)
    line = accs.readline()
