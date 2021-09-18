from starlette.testclient import TestClient


def test_route(client: TestClient) -> None:
    """Test `{{ cookiecutter.plugin.lower().replace('-','_') }}.route`."""
    response = client.get("/{{ cookiecutter.plugin.removeprefix('rsserpent-plugin-') }}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"
    assert response.text.count("Example Title") == 1
