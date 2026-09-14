from pydantic import BaseModel,EmailStr
from typing import Optional,List,Dict

class Data(BaseModel):
    name:str
    email:EmailStr
    hobbies:List[str]
    age:int
    bmi:float

def insert_data(data : Data):
    print(data.name)
    print(data.email)
    print(data.hobbies)
    print(data.age)
    print(data.bmi)


d = {
    'name': 'Veer Pratap',
    'email': 'tncjs@gmail.com',
    'hobbies': ['python','javascript'],
    'age': 20,
    'bmi': 21.14
}

data1 = Data(**d)
insert_data(data1)
