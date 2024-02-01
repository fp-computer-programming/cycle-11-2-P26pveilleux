total = 0 
while True:
    num = int(input("give random number"))

    if num ==-1:
        break
    total += sum
print(total)

list = []
while True:
    input = input("give me number or exit")

    if input.lower() == 'exit' :
        break

    if input.isdigit():
        num = int(input)
        list.append(num)
    else:
        print("wrong input")
    for number in list:
        if number % 3 == 0:
            print("divide by 3")
       
                    

    


