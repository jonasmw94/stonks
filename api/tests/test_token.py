import pytest
import datetime
from api.token import generate_token, decode_token
from api.main import app

@pytest.fixture
def token():
    token = generate_token('test', 'supersecret')
    yield token

def test_that_generated_user_token_is_not_none(token):
    assert token is not None

def test_that_generated_user_can_be_decoded(token):
    decoded_token = decode_token(token, 'supersecret')
    print(decode_token)
    assert decoded_token['user'] == 'test'