'''import turtle as t
t.forward(500)
t.right(90)
t.forward(100)
t.right(90)
t.forward(500)

t.right(90)
t.forward(100)'''

'''for i in range(6):
    t.forward(100)
    t.right(60)
    for i in range(4):
        t.forward(30)
        t.right(90)


for i in range(6):
    t.forward(100)
    for x in range (5):
        t.forward(33)
        t.right(72)
    t.right(60)
  '''


sum = 0
lst = [0,1]

while True:
    last = lst[len(lst)-1]
    sum = last + lst[len(lst)-2]
    if sum < 1000:
        lst.append(sum)
    else:
        break

print(lst)
    
