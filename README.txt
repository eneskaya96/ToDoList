Python - FLASK 

TO DO List 

Virtual enviroment
    -> virtualenv env
    -> source env/bin/activate


Database
    -> from app import db
    -> db.create_all()
    

Curls
    -> curl -X POST http://127.0.0.1:5000/get/1
    -> curl -X GET http://127.0.0.1:5000/get/4
    -> curl -d '{"content" : "nes"}' -H 'Content-Type: application/json' -X POST  http://127.0.0.1:5000/createTask
    -> curl -X GET http://127.0.0.1:5000
    -> curl -d '{"tableName" : "DONE"}'  -H 'Content-Type: application/json'  -X GET http://127.0.0.1:5000/getTasks
    -> 