from flask import abort
from ..models import db, ArticleModel


def get_article(id: int):
    article = ArticleModel.Articles.query.get(id)

    if article is None:
        data = {
            "empty": True
        }
        return data

    data = {
        # "id": author.id,
        # "username": author.username,
        # "email": author.email
    }
    return data

 
