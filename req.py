import requests
import json
#import pprint
import os
#### cashing
cashing=os.path.exists("saral_data.json")
if cashing==True:
    with open("saral_data.json","r") as f:
        data=json.load(f)
    serial_number=1
    course_name = data["availableCourses"]
    for index_1 in course_name:
        print(serial_number,index_1["name"],":",index_1["id"])
        serial_number+=1
    u = int(input("entet"))
    cashing2=os.path.exists("courseID.json")
    if cashing2==True:
        with open("courseID.json") as fh:
            data1=json.load(fh)
        serial_number2=1
        for i in data1:
            for j in data1[i]:
                print(serial_number2,j["name"])
                slug=j["slug"]
                print(slug)
                serial_number2+=1
    child=int(input("enter the child number"))
    serialNum=1
    for i in data1:
        a=data1[i][child-1]["childExercises"]
        for j in a:
            print("  ",serialNum,j["name"])
            print("-----",j["slug"])
            serialNum+=1            
               

else:
## calling API
    saral_data=requests.get("http://saral.navgurukul.org/api/courses")
    data=saral_data.json()

    #### pushing data in json file
    with open("saral_data.json","w") as f:
        json.dump(data,f,indent=4)

    ###  this loop for coures name and id   
    serial_number=1
    course_name = data["availableCourses"]
    for index_1 in course_name:
        print(serial_number,index_1["name"],":",index_1["id"])
        serial_number+=1

    #### user input for which course you like to do
    user_choose_course=int(input("enter the serial number of course : "))-1
    id=course_name[user_choose_course]["id"]

    #### course id
    courseID=requests.get("http://saral.navgurukul.org/api/courses/"+id+"/exercises")
    courseID_data=courseID.json()

    ####pushing id in json
    with open("courseID.json","w") as fh:
        json.dump(courseID_data,fh,indent=4)

    ###course name
    serial_number2=1
    for i in courseID_data:
        for j in courseID_data[i]:
            print(serial_number2,j["name"])
            slug=j["slug"]
            print(slug)
            serial_number2+=1
    #####slug
    user=int(input("enter the course"))
    print(user,courseID_data["data"][user-1]["slug"])
    slug=courseID_data["data"][user-1]["slug"]
    slugID=requests.get("http://saral.navgurukul.org/api/courses/"+id+"/exercise/getBySlug?slug="+slug)
    slugId_Data=slugID.json()      
    with open("slugID.json","w") as slugfile:
        json.dump(slugId_Data,slugfile,indent=4)
        print(slugId_Data["content"])



    #####child
    child=int(input("enter the child number"))
    serialNum=1
    for i in courseID_data:
        a=courseID_data[i][child-1]["childExercises"]
        for j in a:
            print("  ",serialNum,j["name"])
            print("-----",j["slug"])
            serialNum+=1