from fastapi import FastAPI,Path , HTTPException,Query
import json

app = FastAPI()

def load_data():
    with open('pateints.json' , 'r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {'message':'Patient management API '}

@app.get("/about")
def name():
    return {'developer':'Patient Management API - created by Veer '
            }

@app.get("/patients")
def view():
    data = load_data()
    return data

@app.get("/patients/{patient_id}")
def view_patient(patient_id:str = Path(... , description="Patient ID" , example="P001")):
    data = load_data()
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404 , detail="patient not found")


@app.get("/sort")
def sort_patients(sort_by:str = Query(..., description="Sort by patient height,bmi" , example="height or bmi"),
                  order:str =  Query('asc', description="Sort by patient height,bmi" , example="asc" )):

    valid_field = ['height', 'bmi']
    data = load_data()
    if sort_by not in valid_field:
        raise HTTPException(404 , detail= 'invalid input')

    if order not in ['asc', 'desc']:
        raise HTTPException(404 , detail= 'invalid input')

    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values() ,  key = lambda x: x.get(sort_by,0) , reverse  = sort_order)
    return sorted_data