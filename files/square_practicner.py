from random import *
import time

print("A square practicner for you till 100")
print("Don't do wrong more than 2 times or it will stop")
print("Don't forget you have time limits")

right = 0
wrong = 0

def check(answer, square):
  if a == s:
    right += 1
    print("Bravo")
    print("The right answers", right)
    print("The wrong answers", wrong)

while True:
  n = randint(10, 100)
  global s
  s = n * n
  print(n)
  start = time.time()
  a = int(input("Tell the square: "))
  end = time.time()
  tt = int(end - start)
  print(tt, "seconds is the time took by you to give answer")
  if a == s:
    right += 1
    print("Bravo")
    print("The right answers", right)
    print("The wrong answers", wrong)
  else:
    wrong += 1
    print("You are wrong try again...")
    a = int(input("Tell the square again: "))
    
print("The number of times your answer was right =", right)
print("The number of times your answer was wrong =", wrong)
