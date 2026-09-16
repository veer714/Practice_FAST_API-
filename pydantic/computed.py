from pydantic import BaseModel,field_validator, ValidationError,model_validator,computed_field
from typing import Optional,Any,Annotated

class User(BaseModel):
    name: str
    age: int
    hieght: float
    wieght: float

    @computed_field()
    @property
    def bmi(self) -> float:
        return (self.wieght/(self.hieght ** 2))


def insert(data:User):
    print(data.name)
    print(data.age)
    print(data.hieght)
    print(data.wieght)
    print(data.bmi)

d = {'name':'Veer',
     'age':10,
     'hieght':1.72,
     'wieght':71.06 }

data = User(**d)
insert(data)