from time import sleep

def countdown(minutes):
    seconds = minutes * 60
    print()
    print("Exam Starts !!!")
    print()
    warningMade = False
    while seconds != 0:
        mins = seconds // 60
        secs = seconds % 60
        if mins < 1 and warningMade == False:
            print("Hurry Up!!!")
            warningMade = True
            print()
            
        print('{:02d}:{:02d}'.format(mins, secs), end='\r')
        sleep(1)
        seconds -= 1

    print("\nExam Over !!!")

print()
minutes = int(input("Enter minutes "))
countdown(minutes)