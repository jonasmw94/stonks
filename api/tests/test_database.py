import pytest
import datetime
from api.database import get_user, insert_user, mongo
from api.main import app

def finalize():
    mongo.db.drop_collection('users')

@pytest.fixture(scope="session", autouse=True)
def preapre(request):
    request.addfinalizer(finalize)
    mongo.db.drop_collection('users')

def test_that_query_user_is_none():
    user = get_user('123')
    assert user == None

def test_that_query_user_is_not_none_after_inserting_a_given_user():
    insert_user('123')
    user = get_user('123')
    assert user != None