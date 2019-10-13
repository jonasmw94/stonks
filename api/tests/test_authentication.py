import pytest
import datetime
from main import app
from database import get_user, insert_user, mongo, check_user_login

def finalize():
    mongo.db.drop_collection('users')

@pytest.fixture(scope="session", autouse=True)
def prepare(request):
    request.addfinalizer(finalize)
    mongo.db.drop_collection('users')
    insert_user('123', '123456789')

def test_that_you_cant_login_with_wrong_password_for_user_123():
    user = check_user_login('123', '2390239029023')
    assert user == None

def test_that_you_can_login_with_correct_password_for_user_123_and_get_correct_user_back():
    user = check_user_login('123', '123456789')
    assert user != None
    assert user['user'] == '123'