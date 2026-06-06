class coursems():
    def __init__(self):
        self.file="coursems.txt"
    def add_course(self):
        course_id=input("enter course id:")
        course_name=input("enter course name:")
        trainer_name=input("enter trainer name:")
        duration=input("enter duration:")
        try:
            with open(self.file,"r") as f:
                courses=f.readlines()
        except:
            courses=[]
        for course in courses:
            if course.strip()=="":
                continue
            i,n,t,d=course.strip().split(",")
            if i==course_id:
                print("ALREADY ADDED")
                return
            
        with open(self.file,"a") as f:
            f.write(str(course_id)+","+course_name+","+trainer_name+","+str(duration)+"\n")
        print("COURSE ADDED")
    def view_course(self):
        with open(self.file,"r") as f:
            courses=f.readlines()
        if not courses:
            print("NO COURSES TO VIEW")
            return
        for course in courses:
            if course.strip()=="":
                continue
            i,n,t,d=course.strip().split(",")
            print("\ncourse id:",i,
                  "\ncourse name:",n,
                  "\ntrainer name:",t,
                  "\nduration:",d,"\n")
    def search_course(self):
        course_id=input("enter course id:")
        with open(self.file,"r") as f:
            courses=f.readlines()
        found=False
        for course in courses:
            if course.strip()=="":
                continue
            i,n,t,d=course.strip().split(",")
            if i==course_id:
                print("\ncourse id:",i,
                      "\ncourse name:",n,
                      "\ntrainer name:",t,
                      "\nduration:",d,"\n")
                found=True
        if not found:
            print("INVALID ID")
    def update_course(self):
        course_id=input("enter course id:")
        courses_name=input("enter course name:")
        trainers_name=input("enter trainer name:")
        durations=input("enter duration:")
        with open(self.file,"r") as f:
            courses=f.readlines()
        update=[]
        found=False
        for course in courses:
            if course.strip()=="":
                continue
            i,n,t,d=course.strip().split(",")
            if i==course_id:
                update.append(str(i)+","+courses_name+","+trainers_name+","+str(durations)+"\n")
                found=True
            else:
                update.append(course)
        with open(self.file,"w") as f:
            f.writelines(update)
        if found:
            print("COURSE UPDATED")
        else:
            print("INVALID ID")
    def delete_course(self):
        course_id=input("enter course id:")
        with open(self.file,"r") as f:
            courses=f.readlines()
        delete=[]
        found=False
        for course in courses:
            if course.strip()=="":
                continue
            i,n,t,d=course.strip().split(",")
            if i==course_id:
                found=True
            else:
                delete.append(course)
        with open(self.file,"w") as f:
            f.writelines(delete)
        if found:
            print("COURSE DELETE")
        else:
            print("INVALID ID")
system=coursems()
while True:
    print("\nCOURSE MANAGEMENT SYSTEM")
    print("1.add course")
    print("2.view course")
    print("3.search course")
    print("4.update course")
    print("5.delete course")
    print("6.EXIT")
    choice=input("enter your choice:")
    if choice=="1":
        system.add_course()
    elif choice=="2":
        system.view_course()
    elif choice=="3":
        system.search_course()
    elif choice=="4":
        system.update_course()
    elif choice=="5":
        system.delete_course()
    
    elif choice=="6":
        print("------------EXITING COURSE MANAGEMENT SYSTEM------------------")
        break
    else :
        print("invalid choice :(")
                          
            
                
            
        
                
            
            
                   
            
            
            
        
        
