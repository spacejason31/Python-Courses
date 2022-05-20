def list_product(my_list):
    result = 1
    for number in my_list:
        result = result * number
    return result
if __name__ == "main":
    print(list_product([2,3]))
    print(list_product([2,10,15]))

def sum_ofnumbers(**args):
    total = 0
    for number in args:
        total += number
        print(total)
    return total
if __name__ == "main":
    print(sum_ofnumbers(1,3,2,5,4))

def person_details(**kwargs):
    print("Personal Details")
    print("-"*20)
    for key, value in kwargs.items():
        print("{} : {}".format(key,value))

def fib_seq(iteration):
    fib_list = []
    for i in range(0, iteration+1):
        if i == 0:
            fib_list.append(0)
        if i == 1:
            fib_list.append(1)
        if i > 1:
            fib_next_num = fib_list[i-1] + fib_list[i-2]
            fib_list.append(fib_next_num)
    print(fib_list[-1])

stored = {0:0, 1:1}
def fib_dynamic(n):
    if n in stored:
        return stored[n]
    else:
        stored[n] = fib_dynamic(n-1) + fib_dynamic(n-2)
        return stored[n]
