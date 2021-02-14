import requests,json
from decouple import config

resultOfGetALLTasks = [{'content': 'task 1', 'id': 1, 'table_name': 'TODO'}, {'content': 'task 2', 'id': 2, 'table_name': 'TODO'}]
resultOfGetTODOTasks = [{'content': 'task 1', 'id': 1}, {'content': 'task 2', 'id': 2}]
resultOfGetProgressTasks = []

newResultOfGetTODOTasks = [{'content': 'task 2', 'id': 2}]
newResultOfGetProgressTasks = [{'content': 'task 1', 'id': 1}]

url = config('URL')

urlCreteTask = url + "/task/createTask"
urlgetTasks = url + "/tasks/getAllTasks"
urlgetTODOTasks = url + "/tasks/getTasks/TODO"
urlgetPROGRESSTasks = url + "/tasks/getTasks/INPROGRESS"
urlgetmoveTask = url + "/task/moveTask/1/INPROGRESS"


headers = {"Content-type": "application/json"}
data=json.dumps({"content" : "task 1"})
data2=json.dumps({"content" : "task 2"})

#create two task 
responseCreateTask = requests.post(urlCreteTask, data=data,headers=headers)
responseCreateTask = requests.post(urlCreteTask, data=data2,headers=headers)

#read all tasks
responseGetTasks = requests.get(urlgetTasks).json()
#read all TODO tasks
responseGetTODOTasks = requests.get(urlgetTODOTasks).json()
#read all PROGRESS tasks
responseGetProgressTasks = requests.get(urlgetPROGRESSTasks).json()



if "SUCCESS"  in responseCreateTask.text: 
    print("task create pass")  
else:
    print("task create fail")


#print(responseGetTasks)
if resultOfGetALLTasks == responseGetTasks:
    print("get all tasks pass")
else:
    print("get all tasks fail")


#print(responseGetTODOTasks)
if resultOfGetTODOTasks == responseGetTODOTasks:
    print("get TODO tasks pass")
else:
    print("get TODO tasks fail")


#print(responseGetProgressTasks)
if resultOfGetProgressTasks == responseGetProgressTasks:
    print("get INPROGRESS tasks pass")
else:
    print("get INPROGRESS tasks fail")

#move task 1 to INPROGRESS
responseGetProgressTasks = requests.get(urlgetmoveTask).json()
#get new TODOtaks and INPROGRESS taks
responseGetTODOTasks = requests.get(urlgetTODOTasks).json()
responseGetProgressTasks = requests.get(urlgetPROGRESSTasks).json()

#print(responseGetTODOTasks)
#print(responseGetProgressTasks)
if newResultOfGetTODOTasks == responseGetTODOTasks and newResultOfGetProgressTasks == responseGetProgressTasks:
    print("move tasks pass")
else:
    print("move tasks fail")


