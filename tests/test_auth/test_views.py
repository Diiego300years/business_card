import pytest
from dotenv import load_dotenv
from app import create_app, db
from app.models import User

load_dotenv()


"""
        just type pytest tests/test_auth/test_views.py 
"""

@pytest.fixture()
def app():
    app = create_app('testingConfigWithDocker')
    app_context = app.app_context()
    app_context.push()
    yield app
    db.session.remove()
    db.drop_all()
    app_context.pop()

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_login_bad_email(client):
    response = client.post('/auth/login', data={
        'username': 'newuser',
        'email': '@',
        'remember_me': False,
        'password': 'strongpassword'
        })

    assert b'Invalid email address' in response.data


def test_logout_redirect(client):
    response = client.get("/logout")
    # Check that there was one redirect response.
    assert len(response.history) == 1
    # Check that the second request was to the main page.
    assert response.request.path == "/"

    response = client.get("/logout")


def test_register_user_success(app, client):
    # Sample registration data
    with app.app_context():

        response = client.post('/auth/register', data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'strongpassword',
        })

        print(response.data)

        assert response.status_code == 200
        # assert b'Confirmation email has been sent to your email.' in response.data

        user = User.query.filter_by(email='newuser@example.com').first()
        assert user is not None
        assert user.email == 'newuser@example.com'
        assert user.check_password('strongpassword')


def test_login(client):
    response = client.get('/')
    assert response.status_code == 200