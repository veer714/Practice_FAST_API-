from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field,computed_field
from fastapi.responses import JSONResponse
from typing import Annotated,Literal,Optional
import json

app = FastAPI()

def load_data():
    with open('pateints.json', 'r') as f:
        data = json.load(f)

    return data

class Patient(BaseModel):
    id:Annotated[str , Field(... , description="patient id" , examples=['P001'])]
    name: Annotated[str , Field(... , description="patient name" , examples=['Veer'])]
    city:Annotated[str , Field(... , description="patient city" , examples=['Alwar'])]
    age: Annotated[int , Field(... , gt = 0,lt = 100 , description="patient age" , examples=[19])]
    gender: Annotated[Literal['male' , 'female' , 'other'] , Field(... , description="patient gender")]
    height: Annotated[float , Field(... , gt = 0, description="patient height in meters" , examples=[1.8])]
    weight:Annotated[float , Field(... , gt = 0, description="patient weight in kilograms" , examples=[70])]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/(self.height**2),2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'underweight'
        elif self.bmi <= 25:
            return 'normal'
        else:
            return 'overweight'



class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(..., description="patient name", examples=['Veer'])]
    city: Annotated[Optional[str], Field(..., description="patient city", examples=['Alwar'])]
    age: Annotated[Optional[int], Field(..., gt=0, lt=100, description="patient age", examples=[19])]
    gender: Annotated[Optional[Literal['male', 'female', 'other']], Field(..., description="patient gender")]
    height: Annotated[Optional[float], Field(..., gt=0, description="patient height in meters", examples=[1.8])]
    weight: Annotated[Optional[float], Field(..., gt=0, description="patient weight in kilograms", examples=[70])]



def save_data(data):
    with open('pateints.json', 'w') as f:
        json.dump(data, f)



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

@app.post("/create")
def create_patient(patient:Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code= 400 , detail= 'patient already exists')

    data[patient.id] = patient.model_dump(exclude=['id'])
    save_data(data)
    return JSONResponse(status_code=201, content= 'patient created succesfully' )

@app.put("/edit/{patient_id}")
def update_patient( patient_id:str, patientupdate:PatientUpdate):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code= 404 , detail= 'patient not found')

    existing_info = data[patient_id]
    updated_info = patientupdate.model_dump(exclude_unset=True)

    for key,value in updated_info.items():
        existing_info[key] = value


    existing_info['id'] = patient_id
    patient_obj = Patient(**existing_info)

    existing_info = patient_obj.model_dump(exclude=['id'])
    data[patient_id] = existing_info

    save_data(data)
    return JSONResponse(status_code=200, content= 'patient updated succesfully' )


@app.put("/delete/{patient_id}")
def delete_patient( patient_id:str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code= 404 , detail= 'patient not found')

    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200, content= 'patient deleted succesfully' )



