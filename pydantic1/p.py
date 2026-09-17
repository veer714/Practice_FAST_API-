from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, ValidationError,model_validator
from typing import Optional,Any,Annotated

class Data(BaseModel):
    name: Annotated[str , Field(max_length=20, title = 'Name under 20 characters') ]
    email: EmailStr
    age: int
    git_url: AnyUrl
    emergency_cont: Optional[str]

    @model_validator(mode='after')
    def validated_emergency(cls, model):
        if model.age > 60 & 'emergency' not in model.emergency_cont:
            raise ValidationError('should have emergency cont details')
        else:
            return model






def insert(data:Data):
    print(data.name)
    print(data.email)
    print(data.age)
    print(data.git_url)

d = {
    'name':'Veer Pratap',
    'email':'raghavverr26@veer.com',
    'age' : '19',
    'git_url':'https://github.com/veer714'
}

data = Data(**d)
insert(data)