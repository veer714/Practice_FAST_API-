from pydantic import BaseModel

class Address(BaseModel):
    city: str
    pin: int
    state: str

class User(BaseModel):
    name : str
    age: int
    address : Address

a = {'city':'Alwar',
     'pin':301001,
     'state': 'Rajasthan'}
add = Address(**a)

user = {'name': 'Veer',
        'age': 30,
        'address': add}
user1 = User(**user)
# print(user1.name)
# print(user1.age)
# print(user1.address)
# print(user1.address.city)

temp = user1.model_dump(include = ['name'])
temp1 = user1.model_dump_json(include = ['age' , 'address'])
print(temp)
print(temp1)
print(type(temp))
print(type(temp1))