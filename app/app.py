from fastapi import FastAPI


app = FastAPI()


# minimal app, get request
@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong"}


# GET --> Read Todo
@app.get('/todo', tags=['To-Dos'])
async def get_todo() -> dict:
    return {"data": todos}


# POST --> Create Todo
@app.post('/todo', tags=['To-Dos'])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {"data": "A todo has been added"}



# PUT --> Update Todo
@app.put('/todo/{id}', tags=['To-Dos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todo['Activity'] = body['Activity']
            return {
                "data": f"To-Do with {id} has been updated"
            }
    return {"data": f"To-Do itehm with id number: {id} was not found!"} 


# DELETE --> Delete Todo
@app.delete('/todo/{id}', tags=['To-Dos'])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"To-Do with {id} has been deleted"
            }
    return {"data": f"To-Do itehm with id number: {id} was not found!"} 







todos = [
    {
        "id": "1",
        "Activity": "Jogging for 2 hours at 7:00AM."
    },
    {
        "id": "2",
        "Activity": "Writing 3 pages of my new book at 2:00PM."
    }
]
