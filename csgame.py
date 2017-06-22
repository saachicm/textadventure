start = '''
You can be a boy or a girl in High School
'''
print(start)
print("Type 'girl' to be a girl and 'boy' to be a boy")
user_input = input()
if user_input== "girl":
    print("Your counsellor suggests taking a writing course. Press 'A' to go to college of Arts and 'B'to learn computer science at a community college")
    user_input = input()

    if user_input== "A":
         print("You did not follow your dreams and are unhappy")

    elif user_input== "B":
         print("You are in a classroom with all boys and they discourage you. Press 'A' to leave. Press 'B'to stay in the course")

         user_input = input()
         if user_input== "A":
             print("You become a stay at home mom")
         if user_input== "B":
             print("You apply for a job, and beat guys to get in as you developed better skills through hardwork and dedication")
    else:
         print("Please choose between given options!!!")


elif user_input== "boy":
    print("Your counsellor has put you in AP Computer Science. Press 'A' to go to college for Computer Science and 'B' to teach yourself and then start working")
    user_input = input()
    if user_input== "A":
        print("You are recruited on university campus and get a job!!!")
    elif user_input== "B":
        print("You get an off campus recruitment internship and get hired after 6 months1!!")
    else:
        print("Please choose between the given options")

else:
    print("Please choose between the given options!!!")
