from pydantic import BaseModel
from typing import List,Dict,Optional

class Patient(BaseModel):
    id: int
    name: str
    age: int
    hobbies: Optional[List[str]] = None
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.id)
    print(patient.name)
    print(patient.age)
    print(patient.hobbies)
    print(patient.contact_details)

def update_patient_data(patient: Patient):
    print(patient.id)
    print(patient.name)
    print(patient.age)
    print(patient.hobbies)
    print(patient.contact_details)

pat = {'id':1,'name':'Veer Pratap' , 'age':18 , 'hobbies':['Gaming','coding','Movies and shows'] ,
       'contact_details':{'email':'raghavveer714@gmail.com' , 'mob no.' : '9079035431'}}
patient_data = Patient(**pat)
insert_patient_data(patient_data)

pat = {'id':1,'name':'Veer Pratap' , 'age':18,
       'contact_details':{'email':'raghavveer714@gmail.com' , 'mob no.' : '9079035431'}}
patient_data = Patient(**pat)
insert_patient_data(patient_data)

# update_patient = {'id':1,'name':'Veer Pratap' , 'age':19}
# patient_data1 = Patient(**update_patient)
# update_patient_data(patient_data1)
