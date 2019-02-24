#!/usr/bin/env python3
list = []
input01 = float(input("Word Length"))
if input01 >= 1:
    input04 = (input("First Letter"))
    list.append(input01)
    input01 = input01-1
if input01 >= 1:
    input05 = (input("Second Letter"))
    list.append(input02)
    input01 = input01-1
if input01 >= 1:
    input05 = (input("Third Letter"))
    list.append(input03)
    input01 = input01-1
if input01 >= 1:
    input05 = (input("Fourth Letter"))
    list.append(input04)
    input01 = input01-1
if input01 >= 1:
    input05 = (input("Fifth Letter"))
    list.append(input05)
    input01 = input01-1
inputResponse01 = (input("Guess a letter"))
if inputResponse01 == list[1]:
    print ("correct")
else:
    print ("wrong")