from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, ValidationError
from typing import Optional,Any,Annotated

class Data(BaseModel):
    name: Annotated[str , Field(max_length=20, title = 'Name under 20 characters') ]
    email: EmailStr
    age: int
    git_url: AnyUrl

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        v_input = ['veer.com','icici.com','brave.com']
        v = value.split('@')[-1]
        if v not in v_input:
            raise ValidationError('Invalid email address')
        return value

    @field_validator('age' , mode = 'after')
    @classmethod
    def validate_age(cls, value):
        if value < 0 & value > 100:
            raise ValidationError('Age must be between 0 and 100')
        else:
            return value






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