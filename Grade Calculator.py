user_first_name = input("Please, type your first name: ")
user_second_name = input("Please, type your second name: ")
user_full_name = user_first_name + user_second_name
if not user_full_name.isalpha():
    print("Please provide a valid value for your name.")
    exit()
else:
    print("Your name is right.")

score1 = float(input("Type your score for exam 1 (out of 100): "))
score2 = float(input("Type your score for exam 2 (out of 100): "))
score3 = float(input("Type your score for exam 3 (out of 100): "))
attendance = float(input("Type your total attendance (out of 100): "))
average_score = (score1 + score2 + score3)/3
split_name = user_full_name.split()
gpa = average_score / 25
first_inicial = user_first_name[0]
second_inicial = user_second_name[0]
inicials = (first_inicial, second_inicial)

if not (0 <= score1 <= 100):
    print("Please provide a valid value for exam 1, between 0 and 100.")
    exit()
elif not (0 <= score2 <= 100):
    print("Please provide a valid value for exam 2, between 0 and 100.")
    exit()
elif not (0 <= score3 <= 100):
    print("Please provide a valid value for exam 3, between 0 and 100.")
    exit()
elif not (0 <= attendance <= 100):
    print("Please provide a valid value for attendance, between 0 and 100.")
    exit()
else:
    print("Your average score is:\n ", average_score)
    print("Your Second name is:", user_second_name)
    print("Your initials are:", inicials)
    
    if attendance <= 75:
        print("Your grade is: F")
    elif (85 < average_score <= 100):
        print("Your grade is A")
    elif (70 < average_score <= 85):
        print("Your grade is B")
    elif(55 < average_score <= 70):
        print("Your grade is C")
    elif ( 40 < average_score <= 55):
        print("Your grade is D")
    else:
        print("Your grade is F")
    print("Your GPA is: ", gpa)
            





