import pytest
import datetime
from api.database import get_user, insert_user
from api.main import app

def test_that_query_user_is_none():
    with app.app_context():
        user = get_user('123')
        assert user == None

def test_that_query_user_is_not_none_after_inserting_a_given_user():
    with app.app_context():
        insert_user('123')
        user = get_user('123')
        assert user != None