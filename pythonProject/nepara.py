N = 12
sum = 0
count = 0
average = 0

sk = int(input("Ievadi pirmo skaitli: "))

while sk != 12:
    if sk % 2 != 0:
        sum = sum + sk
        count = count + 1
    sk = int(input("Ievadi nakamo skaitli: "))

average = sum / count
print(average)