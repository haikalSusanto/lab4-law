import os
from flask import abort
from ..models import db, AuthorModel
from werkzeug.utils import secure_filename


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

def get_all_author():
    authors = AuthorModel.Authors.query.order_by(AuthorModel.Authors.username).all()
    author_list = list()
    for author in authors:
        single_author = {
            "fullname": author.fullname,
            "username": author.username,
            "email": author.email
        }
        author_list.append(single_author)

    if authors is None:
        data = {
            "empty": True
        }
        return data

    data = author_list
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

def upload(id:int, request_files:dict):
    author = AuthorModel.Authors.query.get(id)
    if author is None:
        data = {
            "empty": True
        }
        return data

    file = request_files['file']
    filename = secure_filename(file.filename)

    is_path_exists= os.path.exists(os.getcwd()+f"/files/{id}/")
    if not is_path_exists:
        os.mkdir(os.getcwd()+f"/files/{id}/" )

    file.save(os.path.join(os.getcwd()+f"/files/{id}/" + filename))

 
