def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print('Why do we use methods?\n')
    print('1. To repeat a statement multiple times.\n')
    print('2. To decompose a program into several small subroutines.\n')
    print('3. To determine the execution time of a program.\n')
    print('4. To interrupt the execution of a program.\n')
    ans = int(input("\n"))
    while (ans!=2):
        print("Please, try again.\n")
        ans = int(input("\n"))
        if(ans==2):
            print("Congratulations, have a nice day!\n")
            break

def end():
    print('Congratulations, have a nice day!')


greet('Bottass', '2022')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
