import datetime


def user_information(ussnm,pssd):
    name = input("Enter Your Name Please: ")
    address = input("Your Address: ") 
    age = input("Your Age Pls: ")
    ussnm_ = ussnm+"task.txt"

    f = open(ussnm_,'a')
    f.write(pssd)
    f.write("\nName: ")
    f.write(name)
    f.write('\n')
    f.write("Address : ")
    
    f.write(address)
    f.write('\n')
    f.write("Age : ")
    f.write(age)
    f.write('\n')
    f.close()

def  signup():
    print("Please Enter The Username By Which You Want To Create Your Account")
    username  = input("Please Enter Here: ")
    password = input("Enter A Password: ")
    user_information(username, password)
    print("Sir, Pls Proceed Towards LOGIN")
    login()


def login():
    print("Plese Enter Your Username Below")
    user_nm = input("Enter Here: ")

    pssd_wr = (input("Enter The Password: "))+'\n'
    try:
        usernm = user_nm+"task.txt"
        f_ = open(usernm,'r')


        k = f_.readlines(0)[0]
        f_.close()

        if pssd_wr == k:
            print("-----------------------------------")
            print("Enter   --1--\tTo View Your Data\nEnter   --2--\tTo Add Task\nEnter   --3--\tUpdate\\Task Status\nEnter   --4--\tView Task Status")
            print("-----------------------------------")
            a = input("ENTER>> ")

            if a == '1':
                view_data(usernm)
            elif a == '2':
                task_information(usernm)
            elif a  =='3':
                task_update(user_nm)
            elif a =='4':
                task_update_viewer(user_nm)
            else:
                print("Wrong Input! Andha Hai Kya?")
        else:
            print("SIR YOUR PASSWORD IS WRONG << Pls Try Again")
            login()
    except Exception as e:
        print(e)
        login()


def view_data(username):
    ff = open(username,'r')
    print(ff.read())
    ff.close()

def task_information(username):
    print("Sir Enter No of Task You Want To Add")
    j = int(input(">> "))
    f1 = open(username, 'a')

    for i in range(1,j+1):
        task = input("Enter The Task-> ")
        target = input("Enter The Target-> ")
        PP = "TASK"+str(i)+' :'
        qq = "TARGET "+str(i)+" :"

        f1.write(PP)
        f1.write(task)
        f1.write('\n')
        f1.write(qq)
        f1.write(target)
        f1.write('\n')
        print("Do U Want To Stop Then Press (SpaceBar+Enter) Otherwise Press (ENTER")
        s = input()
        if s==' ':
            break
    f1.close()


def task_update(username):
    username = username+"TASK.txt"
    print("Pls Enter The Task Which Are Completed")
    task_completed = input()

    print("Enter Task Which Are Still Not Started By You")
    task_not_started = input()

    print("Enter Task Which You Are Doing")
    task_ongoing = input()

    fw = open(username, 'a')
    DT = str(datetime.dtaetime.now())
    fw.write(DT)
    fw.write("\n")
    fw.write("COMPLETED TASK: ")
    fw.write(task_completed)
    fw.write("\n")
    fw.write("ONGOING TASK: ")
    fw.write(task_ongoing)
    fw.write("\n")
    fw.write("NOT YET STARTED: ")
    fw.write(task_not_started)
    fw.write("\n")

def task_update_viewer(username):
    ussnm = username+"TASK.txt"
    o = open(ussnm,'r')
    print(o.read())
    o.close()

if __name__=='__main__':
    print("WELCOME TO SARTHAK'S TASK MANAGER")
    print("Sir Are You New To This Software")
    a = int(input("Type (1) if NEW Otherwise Press (0) :: "))
    if a==1:
        signup()
    elif a == 0:
        login()
    else:
        print("You have provided wrong input !")
