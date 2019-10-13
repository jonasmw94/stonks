import pytest
import datetime
from main.main_app import app
from token_handler import generate_token, decode_token

@pytest.fixture
def token():
    token = generate_token('test', 'supersecret')
    yield token

def test_that_generated_user_token_is_not_none(token: str):
    assert token is not None

def test_that_generated_user_can_be_decoded(token: str):
    decoded_token = decode_token(token, 'supersecret')
    print(decode_token)
    assert decoded_token['user'] == 'test'