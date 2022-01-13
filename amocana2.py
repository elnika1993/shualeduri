x = int(input("Enter any number: "))
#k = 0
choose = input("choose: kenti or luwi")
if choose == "kenti":
    def kenti ():
        for i in range(1, x):
            print(i)
if choose == "luwi":
    def luwi():
        i = 0
        while i <= x:
            print(i+2)
            i += 1
