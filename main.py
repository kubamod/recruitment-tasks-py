
import re
from decimal import *

def postal_code_generator(first_postal_code: str, second_postal_code: str):

#    pattern = re.compile("\d{2}-\d{3}")
#    if pattern.match(first_postal_code) == None or pattern.match(second_postal_code) == None:
#        exit('Postal code is wrong')

    first_postal_code = first_postal_code
    second_postal_code = second_postal_code

    fpc_left = int(first_postal_code.split('-')[0])
    fpc_right = int(first_postal_code.split('-')[1])

    spc_left = int(second_postal_code.split('-')[0])
    spc_right = int(second_postal_code.split('-')[1])

    postal_codes = [str]

    if (fpc_left > spc_left):
        buff = fpc_left
        fpc_left = spc_left
        spc_left = buff

    if (fpc_left == spc_left):
        for j in range(fpc_right + 1, spc_right):
            postal_codes.append(str(fpc_left) + '-' + str(j))
    else:
        for i in range(fpc_left, spc_left):
            print(i)
            for j in range(fpc_right + 1, 1000):
                postal_codes.append(str(i) + '-' + str(j))
            for j in range(0, spc_right):
                postal_codes.append(str(i + 1) + '-' + str(j).zfill(3))


    if (fpc_left > spc_left):
        return postal_codes.reverse()

    return postal_codes


# print(postal_code_generator('92-900', '91-990'))



def task_nr_3(elements, n: str):
    numbers = []
    for i in range(1, n + 1):
        if i not in elements:
            numbers.append(i)
    return numbers

# print(task_nr_3([2,3,7,4,9], 10))




def taskt_nr_3():
    numbers = [Decimal]
    start = Decimal('2.00')
    for i in range(1, 9):
        numbers.append(start)
        start = start + Decimal('0.5')
    
    return numbers

# print(taks_nr_3())
