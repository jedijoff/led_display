
user_number = None

numbers = ((('*** '), ('  * '), ('*** '), ('*** '), ('* * '), ('*** '), ('*** '), ('*** '), ('*** '), ('*** ')),
           (('* * '), ('  * '), ('  * '), ('  * '), ('* * '), ('*   '), ('*   '), ('  * '), ('* * '), ('* * ')),
           (('* * '), ('  * '), ('*** '), ('*** '), ('*** '), ('*** '), ('*** '), ('  * '), ('*** '), ('*** ')),
           (('* * '), ('  * '), ('*   '), ('  * '), ('  * '), ('  * '), ('* * '), ('  * '), ('* * '), ('  * ')),
           (('*** '), ('  * '), ('*** '), ('*** '), ('  * '), ('*** '), ('*** '), ('  * '), ('*** '), ('  * ')))

def disply_number(num):
    global line_1, line_2, line_3, line_4, line_5
    global user_number
    x = ''
    line_1, line_2, line_3, line_4, line_5 = ([] for i in range(5))
    for x in str(num) :
        line_1.append(numbers[0][int(x)])
        line_2.append(numbers[1][int(x)])
        line_3.append(numbers[2][int(x)])
        line_4.append(numbers[3][int(x)])
        line_5.append(numbers[4][int(x)])

    for i in line_1:
        if i == '':
            line_1.remove(i)
        else:
            continue

    print(''.join(line_1))
    print(''.join(line_2))
    print(''.join(line_3))
    print(''.join(line_4))
    print(''.join(line_5))

    run_again = input('do you want to run again y/n? ')
    if run_again == 'y':
        get_user_number()
    else:
        print('Goodbye')

def get_user_number():
    global user_number

    try:
        user_number = int(input('enter a series of digits that you wish to be displayed as in led format: '))
        disply_number(user_number)
    except ValueError:
        print('Please enter an integer.')
        get_user_number()



get_user_number()
