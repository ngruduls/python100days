ok = 1
while ok == 1:
    n = int(input("ievadiet naturālu skaitli: "))
    while n <= 0:
        n = int(input("IEVADIET NATURĀLU SKAITLI!!!!!!!! NATURĀLU skaitli!!!"))

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
    ok = int(input(" Vai turpināt (1) vai beigt (0)?"))