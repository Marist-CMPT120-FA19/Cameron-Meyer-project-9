def main():
    Prime = eval(input("Please enter a number: "))
    Num = []
    for i in range(2,Prime+1):
        Num.append(i)
    while len(Num)>0:
        aPrime = Num.pop(0)
        print(aPrime, "is prime!")
        for aNum in Num:
            if aNum % aPrime == 0:
                Num.remove(aNum)


if __name__ == "__main__":
    main()

