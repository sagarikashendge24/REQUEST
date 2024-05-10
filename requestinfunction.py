import requests
import json
def topics():
    i=0
    while i<len(data["availableCourses"]):
        Courses = (data["availableCourses"][i]["name"])
        print(i+1," ",Courses,data["availableCourses"][i]["id"])
        i=i+1
    user_input = int(input("Enter your courses number that you want to learn:-"))
    print(data["availableCourses"][user_input-1]["name"])

saral_api = " http://saral.navgurukul.org/api/courses"    
saral_url = requests.get(saral_api)                       
data = saral_url.json()
with open ("courses.json","w") as saral_data:
    json.dump(data,saral_data,indent = 4)
serial_no = 0
for i in data["availableCourses"]:
    print(serial_no+1 ,i["name"], i["id"])
    serial_no=serial_no+1
print("")
user_input =int(input("Enter your courses number that you want to learn:- "))
parent_id=data["availableCourses"][user_input-1]["id"]
print(data["availableCourses"][user_input-1]["name"])

user_input_1=input("if you want next or previous n/p: ")
if user_input_1=="p":
    topics()

parent_api = "http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][user_input-1]["id"])+"/exercises"
parent_url = requests.get(parent_api)
data_1 = parent_url.json()
with open ("parentes.json","w") as child_data:
    json.dump(data_1,child_data,indent=4)

serial_no_1=0
for i in data_1["data"]:
    print(serial_no_1+1,".",i["name"])
    if len(i["childExercises"])>0:
        s= 0
        for j in i['childExercises']:
            s = s+ 1
            print("    ",s,j['name'])
    else:
        print("         1",i["name"])
    serial_no_1+=1

topic_no = int(input("Enter topic number that's you want to learn:- "))
my_list=[]
m = 0
while m < len(data_1["data"][topic_no-1]["childExercises"]):
    print("     ", m+1 ,data_1["data"][topic_no-1]["childExercises"][m]["name"])
    slug = (data_1["data"][topic_no-1]["childExercises"][m]["slug"])
    # m = m +1
    # calling a child exercise 

    child_exercises_url = ("http://saral.navgurukul.org/api/courses/" +  str(parent_id) +"/exercise/getBySlug?slug=" + slug )
    Data_3 = requests.get(child_exercises_url)

    # converting data into a json file

    convert_data = Data_3.json()
    with open("Topic.json","w") as f:
        json.dump(convert_data,f,indent=4)
    my_list.append(convert_data["content"])
    m = m + 1

def slug_1(questions_no):
    # questions_no = int(input("choose the specific questions no :- "))
    question=questions_no-1
    print(my_list[question])
    while questions_no > 0 :
        next_question = input("do you next question or previous question n/p :- ")
        if questions_no == len(my_list):
            print("next page")
        if next_question == "p" :
            if questions_no == 1:
                print("no more questions")
                break
            else:
            # elif questions_no > 0:
                questions_no = questions_no  -1
                print(my_list[questions_no])
        elif next_question == "n":
            if questions_no < len(my_list):
                index = questions_no + 1
                print(my_list[index-1])
                question = question + 1
                questions_no = questions_no + 1 
                if question == (len(my_list)-1) :
                    print("next page")
                    break
questions_no = int(input("choose the specific questions no :- "))
slug_1(questions_no)



