from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from models import Building, Organization, Functional


app = FastAPI()

buildings = [
    {"address": "Pushkin street 100", "sh": 100.0, "dol": 50.0},
    {"address": "Pushkin street 200", "sh": 200.0, "dol": 80.0},
    {"address": "Pushkin street 300", "sh": 150.0, "dol": 60.0}
]

functionals = [
    {"id": 1, "fun_id": ["Moloko"]},
    {"id": 2, "fun_id": ["Mясо"]},
    {"id": 3, "fun_id": ["Автомобили"]}
]


organizations_data = [
    {"id": 1, "name": "Azimut001", "phones": ["8800-333-3333"], "building": buildings[1], "functionals": [functionals[1]]},
    {"id": 2, "name": "Azimut002", "phones": ["8900-333-7575"], "building": buildings[2], "functionals": [functionals[2]]},
    {"id": 3, "name": "Azimut003", "phones": ["8123-456-7890"], "building": buildings[0], "functionals": [functionals[0]]}
]

buildings_objects = [Building(**building) for building in buildings]
functionals_objects = [Functional(**functional) for functional in functionals]

@app.get('/organizations', response_model=List[Organization])
async def get_organization() -> List[Organization]:
    return [Organization(**org) for org in organizations_data]

@app.get('/organizations/by-building/{building_id}', response_model=List[Organization])
async def get_organizations_by_building(building_id: int):
    return [org for org in organizations_data if org['building']['address'] == buildings[building_id]['address']]

@app.get('/organizations/by-functional/{functional_id}', response_model=List[Organization])
async def get_organizations_by_functional(functional_id: int):
    return [
        org for org in organizations_data
        if any(func['id'] == functional_id for func in org['functionals'])
    ]

@app.get('/organization/{org_id}', response_model=Organization)
async def get_organization_by_id(org_id: int):
    for org in organizations_data:
        if org['id'] == org_id:
            return org
    raise HTTPException(status_code=404, detail="Organization not found")

@app.get('/organizations/by-name/{name}', response_model=List[Organization])
async def get_organizations_by_name(name: str):
    return [org for org in organizations_data if name in org['name']]


# @app.get('/items')
# async def items()->List[Post]:
#     return [Post(**post) for post in posts]






# class Post(BaseModel):
#     id:int
#     title: str
#     body: str
#     author: User
#
# users = [
#     {'id':1, "name": 'John', "age": 34},
#     {'id':2, "name": 'Mike', "age": 40},
#     {'id':3, "name": 'Jasmin', "age": 24}
# ]
#
# posts = [
#     {'id':1, 'title': 'News 1', 'body': 'Text 1', 'author': users[1]},
#     {'id':2, 'title': 'News 2', 'body': 'Text 2','author': users[0]},
#     {'id':3, 'title': 'News 3', 'body': 'Text 3','author': users[2]}
# ]
#
# @app.get('/items')
# async def items()->List[Post]:
#     return [Post(**post) for post in posts]
#
# @app.get('/items/{id}')
# async def items(id:int)->Post:
#     for post in posts:
#         if post['id']==id:
#             return Post(**post)
#     raise HTTPException(status_code=404, detail = 'Post not found')
#
# @app.get('/search')
# async def search(post_id: Optional[int]=None)-> dict:
#     if post_id :
#         for post in posts:
#             if post['id'] == post_id:
#                 return post
#         raise  HTTPException(status_code=404, detail = 'Post not found')
#
#     else:
#         return { 'data': 'No post id provided'}
