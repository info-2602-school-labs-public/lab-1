#================================================

# Lab Tasks

#-------------------------------------------------

## Task 3

from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
async def hello_world():
    return 'Hello, World!'

### New Function
#@app.get('/students')
#async def get_students():
#    return data
### End of new function

#-------------------------------------------------

## Task 5 

### New Function
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: # select only the students with a given meal preference
                filtered_students.append(student) # add match student to the result
        return filtered_students
    return data
### End of new function

#-------------------------------------------------

## Task 4
@app.get('/students/{id}')
async def get_student(id):
    for student in data:
        if student['id'] == id: # Only return the student if the ID matches
            return student
        
#-------------------------------------------------

#================================================

# Homework

#-------------------------------------------------

## Exercise 1
### Create a route /stats which returns a count of the various meal preferences and programmes in the data set

@app.get('/stats')
async def get_stats():
    pref_counts = {}
    programme_counts = {}
    stats = {}

    for student in data:

        pref = student['pref']
        programme = student['programme']
        # Count meal preferences
        # pref = student['pref']
        if pref in stats:
            stats[pref] += 1
        else:
            stats[pref] = 1

        # Count programmes
        # programme = student['programme']
        if programme in stats:
            stats[programme] += 1
        else:
            stats[programme] = 1 

    return stats
    
#-------------------------------------------------

## Exercise 2
### Create additional routes; /add/a/b, /subtract/a/b, multiply/a/b and divide/a/b that takes in 2 route parameters a and b and returns the result of the calculation

@app.get('/add/{a}/{b}')
async def add(a: float, b: float):
    return {
        "operation": "add",
        "a": a,
        "b": b,
        "result": a + b
    }

@app.get('/subtract/{a}/{b}')
async def subtract(a: float, b: float):
    return {
        "operation": "subtract",
        "a": a,
        "b": b,
        "result": a - b
    }

@app.get('/multiply/{a}/{b}')
async def multiply(a: float, b: float):
    return {
        "operation": "multiply",
        "a": a,
        "b": b,
        "result": a * b
    }

@app.get('/divide/{a}/{b}')
async def divide(a: float, b: float): 
    if b == 0:
        return {
            "error": "Division by zero is not allowed."
        }
    return {
        "operation": "divide",
        "a": a,
        "b": b,
        "result": a / b
    }

#-------------------------------------------------