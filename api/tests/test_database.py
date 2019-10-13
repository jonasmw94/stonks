import pytest
import datetime
from main.main_app import app
from database import get_user, insert_user, mongo

def finalize():
    mongo.db.drop_collection('users')

@pytest.fixture(scope="session", autouse=True)
def prepare(request):
    request.addfinalizer(finalize)
    mongo.db.drop_collection('users')

def test_that_query_user_is_none():
    user = get_user('123')
    assert user == None

def test_that_query_user_is_not_none_after_inserting_a_given_user():
    insert_user('123', '123456789')
    user = get_user('123')
    assert user != None

def test_that_query_user_is_123_after_inserting_123_user():
    insert_user('123', '123456789')
    user = get_user('123')
    assert user['user'] == '123'

def test_that_you_cannot_insert_123_user_after_123_is_inserted():
    assert insert_user('123', '123456789') is False

def test_that_you_cannot_insert_123_user_with_password_123():
    assert insert_user('123', '123') is False
