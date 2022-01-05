def multiply():
    arr = []
    for i in list(range(1,6)):
            arr.append(int(input("Type a number: ")))
    result = 1
    for x in arr:
            result = result * x
    print(result)

multiply()
