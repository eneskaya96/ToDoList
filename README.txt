This is project for Python - FLASK 

This simple TO DO List project

There are four database table 
    -> TASKS -- keeps all tasks
    -> TODOTASK -- keeps task which are in TODO state
    -> INPROGRES -- keeps task which are in INPROGRES state
    -> DONE -- keeps task which are in DONE state

There are 4 API endpoint, its documentation is
Documentation
    -> html-documentation-generated/index.html
    -> online link : https://app.swaggerhub.com/apis/ENESKAYA/ToDoList/1.0.0

You can activate virtualenv with following commands
Virtual enviroment
    -> virtualenv env
    -> source env/bin/activate


You can activate Database with following python code
    -> python3 clearDB.python
    -> you should delete todo.db with hand

You can start the app with
    -> python3 app.py

You can test the functions with 
    -> python3 test.python
    -> you should see all functions "pass"    
    
You can try with curl command from terminals
Curls
    create task
    ->  curl -d '{"content" : "task 1"}' -H 'Content-Type: application/json' -X POST  http://127.0.0.1:5000/task/createTask
    get all tasks
    -> curl -X GET http://127.0.0.1:5000/tasks/getAllTasks
    get specific table task
    -> curl -X GET http://127.0.0.1:5000/tasks/getTasks/TODO
    -> curl -X GET http://127.0.0.1:5000/tasks/getTasks/INPROGRESS
    -> curl -X GET http://127.0.0.1:5000/tasks/getTasks/DONE
    move to 
    -> curl -X GET http://127.0.0.1:5000/moveTask/1/INPROGRESS

                            MUHAMMET ENES KAYA



