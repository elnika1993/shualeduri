x = int(input("Enter x: "))
y = int(input("Enter y: "))
nishani = input("choose: +/-/:/* ")
if nishani == "+":
    def mimateba():
        print(x+y)
    print("answer is: ",x+y)
elif nishani == "-":
    def gamokleba():
        k=x-y
    print("Answer is: ", x-y)
elif nishani == ":":
    def gayofa():
        k=x/y
    print("Answer is: ", x/y)
elif nishani == "*":
    def gamravleba(x,y):
        x*y
    print("Answer is: ",x*y)
else:
    print("Error")
