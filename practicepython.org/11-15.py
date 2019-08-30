# EX 11 

def get_divisors():
    n = int(input("Please enter a number: "))
    list_d = [1]
    for i in range(2, n):
        if n % i == 0:
            list_d.append(i)
    if list_d != [1]:
        print(f"{n} is not prime here are his divisors: {list_d}")
    else:
        print("Number is prime")
get_divisors()



# EX 12
def f_and_l(n):
    return [n[0],n[len(n)-1]]

# EX 13
def gen_fib():
    num = int(input("How many Fibonacci numbers would you like to generate"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib
        = [1,1]
        while i < num:
            fib.append(fib[i] + (fib[i-1]))
            i += 1
    return fib

# EX 14

#1 Func:
def dup1(list1):
    new_list = []
    for x in list1:
        if x not in new_list:
            new_list.append(x)
    return new_list
                

#2 Func:
def dup2(list1):
    list1 = set(list1)
    list1 = list(list1)
    return list1


# EX 15
def stringR():
    sent = input("Enter a sentence you would like to reverse: ")
    listR = sent.split()
    n = list(reversed(listR))
    f = " ".join(n)
    print(f)
    return f
stringR()
