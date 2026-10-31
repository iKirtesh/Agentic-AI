import httpx
import pytest

from api_client import DemoApiClient


def handler(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/posts/404":
        return httpx.Response(404, json={"detail": "missing"})
    return httpx.Response(200, json={"id": 7, "title": "Mock post"})


def test_get_post_uses_http_response():
    transport = httpx.MockTransport(handler)
    with DemoApiClient(transport=transport) as api:
        post = api.get_post(7)
    assert post["title"] == "Mock post"


def test_non_success_status_raises():
    transport = httpx.MockTransport(handler)
    with DemoApiClient(transport=transport) as api:
        with pytest.raises(httpx.HTTPStatusError):
            api.get_post(404)
