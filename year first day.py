y = int(input("Enter The Year:"))
def leapyear(y):
    sum = 0
    a1 = int((y//100)*100)
    a12 = int(a1/400)
    sum += a12*97
    a1 = a1 % 400
    a1 = a1/100
    sum += a1*24
    a2 = y % 100
    if a2 % 4 == 0:
        a3 = (a2/4)-1
    else:
        a3 = int(a2//4)
    sum += a3
    return sum
n = y % 7
l = leapyear(y)
total = n + l
total = int(total % 7)
list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
print("The First Day Of The Year Is",list[total])
y = input()