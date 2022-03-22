from flask import abort
from ..models import db, AuthorModel


def get_author(id: int):
    author = AuthorModel.Authors.query.get(id)

    if author is None:
        data = {
            "empty": True
        }
        return data

    data = {
        "id": author.id,
        "username": author.username,
        "email": author.email
    }
    return data

def create_new(request_body: dict):
    new_author = AuthorModel.Authors(request_body["fullname"], request_body["username"], request_body["email"])
    db.session.add(new_author)
    db.session.commit()

def update(id: int, request_body: dict):
    author = AuthorModel.Authors.query.get(id)
    if author is None:
        data = {
            "empty": True
        }
        return data

    author.fullname = request_body['fullname']
    author.username = request_body['username']
    author.email = request_body['email']
    db.session.commit()

def delete(id: int):
    author = AuthorModel.Authors.query.get(id)
    if author is None:
        data = {
            "empty": True
        }
        return data
    db.session.delete(author)
    db.session.commit()

 
