import csv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

@app.post("/person/")
async def create_person(person: Person):
    with open("new.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([person.id, person.name, person.age])
        return{"message": "Person has been created successfully", "data": person}

@app.get("/person{id}")
async def get_id(id: int):
    with open("new.csv", "r") as file:
        reader = csv.reader(file)
        next (reader)
        for column in reader:
            if int(column[0]) == id:
                return Person(id=int(column[0]),name=column[1], age=column[2] )
    return{"message": "Person not found"}