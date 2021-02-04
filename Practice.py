#program to accept input from user,and determine if guess was right
#declaring variables
secret_num = 9
guess_limit = 3
guess_count = 0
#while loop to collect input from user until,guess is correct
while guess_count < guess_limit:
    #keep collecting input from user until guess is up to three
    #asking user for input
    guess = int(input("what's your guess> "))
    guess_count +=1
    if guess == secret_num:
        print('Correct!')
        #break out of the while loop as lon as guess is correct
        break
    else:
        print('Try again')
else:
    print('You failed')