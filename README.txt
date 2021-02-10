Python - FLASK 

TO DO List 

Virtual enviroment
    -> virtualenv env
    -> source env/bin/activate


Database
    -> from app import db
    -> db.create_all()
    

Curls
    create task
    -> curl -d '{"content" : "task 1"}' -H 'Content-Type: application/json' -X POST  http://127.0.0.1:5000/createTask
    get all tasks
    -> curl -X GET http://127.0.0.1:5000
    get specific table task
    -> curl -X GET http://127.0.0.1:5000/getTasks/TODO
    -> curl -X GET http://127.0.0.1:5000/getTasks/INPROGRESS
    -> curl -X GET http://127.0.0.1:5000/getTasks/DONE
    move to 
    -> curl -X GET http://127.0.0.1:5000/moveTask/1/INPROGRESS


Documentation

    -> html-documentation-generated/index.html
    -> online link : https://app.swaggerhub.com/apis/ENESKAYA/ToDoList/1.0.0
    