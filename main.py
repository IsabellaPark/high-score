# import random

# scores = []
# players = ["David", "Kaiden", "Rose", "Bella", "Alex"]

# def generate():
#   for i in range(len(players)):
#     scores.append(random.randint(1, 100)) 


# def swap(alist, i1, i2):
#   temp = alist[i1]
#   alist[i1] = alist[i2]
#   alist[i2] = temp

# def bubblesort(score_list, player_list):
#   for i in range(1, len(score_list)):
#     j = i
#     while j > 0:
#       if score_list[j] > score_list[j - 1]:
#         swap(scores, j, j-1)
#         swap(players, j, j-1)
#       j -= 1 
  
# def main():
#   generate()
#   bubblesort(scores, players)
#   for i in range(len(scores)):
#     print("{}\t {}'s score: \t{}".format(i + 1, players[i], scores[i]))


# main()
      
  # bubble sort: compare numbers if numbers to the left > right swap
#----------------------------------------------------------------------------
import random
number = []
for i in range(100):
  number.append(random.randint(1,200))

print(number)

def swap(alist, i1, i2):
  temp = alist[i1]
  alist[i2] = alist[i2]
  alist[i2] = temp

def bubblesortGreatest(score_list):
  for i in range(1, len(score_list)):
    j = 1
    while j > 0:
      if score_list[j] > score_list[j - 1]:
        swap(number, j, j-1)
      j -= 1 

def binarySearch(alist, number):
  bubblesortGreatest(number)
  
  minimunIndex = 0
  
  maximumIndex = len(alist)
  
  
  while (minimunIndex <= maximumIndex):
    
    midPoint = maximumIndex // 2
    
    if alist[midPoint] < number:
      maximumIndex = midPoint - 1

    elif alist[midPoint] > number:
      minimunIndex = midPoint + 1

    else:
      return midPoint 

  return - 1

num = int(input("what number are you looking for"))
x = binarySearch(number, num)
if(x != -1):
  print(binarySearch(number,num))
else:
  print("The number is not on the list")