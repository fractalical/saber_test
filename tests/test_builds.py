import pytest

from app.pkg.settings import settings
from conftests import client


@pytest.mark.parametrize(
    'x_api_token,build,build_name,status_code',
    [
        ('', 'build', 'some_name', 403),
        ('some_api_token', 'build', 'some_name', 403),
        (settings.X_API_TOKEN.get_secret_value(), 'build', '', 400),
        (settings.X_API_TOKEN.get_secret_value(), 'build', 'some_name', 404),
        (settings.X_API_TOKEN.get_secret_value(), 'build', 'write_beautiful', 200),
        (settings.X_API_TOKEN.get_secret_value(), 'builds', 'write_beautiful', 422)
    ]
)
def test_get_tasks(x_api_token, build, build_name, status_code):
    headers = {'X-API-TOKEN': x_api_token}
    response = client.post('/build/get_tasks', headers=headers, json={
        build: build_name
    })

    assert response.status_code == status_code
