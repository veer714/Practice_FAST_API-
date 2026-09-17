from pydantic import BaseModel,EmailStr,AnyUrl , Field
from typing import Optional,List,Dict

class Data(BaseModel):
    name:str = Field(max_length=20)
    email:EmailStr
    hobbies:List[str] = Field(max_length=5)
    age:int = Field(gt = 0 , lt=130)
    bmi:float = Field(gt = 0 , lt=100)
    git_url:AnyUrl

def insert_data(data : Data):
    print(data.name)
    print(data.email)
    print(data.hobbies)
    print(data.age)
    print(data.bmi)
    print(data.git_url)


d = {
    'name': 'Veer Pratap',
    'email': 'tncjs@gmail.com',
    'hobbies': ['python','java'],
    'age': 19,
    'bmi': 21.14,
    'git_url': 'https://github.com/veer714'
}

data1 = Data(**d)
insert_data(data1)
