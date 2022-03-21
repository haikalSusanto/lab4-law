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

 
