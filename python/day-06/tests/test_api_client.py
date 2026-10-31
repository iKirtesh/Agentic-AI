import json

import httpx
import pytest

from api_client import PostsApiClient


def json_response(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/posts/404":
        return httpx.Response(404, json={"message": "Not found"})
    if request.method == "POST":
        payload = json.loads(request.content)
        return httpx.Response(201, json={"id": 101, **payload})
    if request.url.path == "/posts":
        assert request.url.params["userId"] == "2"
        return httpx.Response(200, json=[{"id": 2, "userId": 2, "title": "Second"}])
    return httpx.Response(200, json={"id": 1, "userId": 1, "title": "Hello"})


def test_get_post_uses_response_json() -> None:
    transport = httpx.MockTransport(json_response)
    with PostsApiClient(transport=transport) as api:
        post = api.get_post(1)
    assert post["title"] == "Hello"


def test_get_posts_passes_query_parameter() -> None:
    transport = httpx.MockTransport(json_response)
    with PostsApiClient(transport=transport) as api:
        posts = api.get_posts_by_user(2)
    assert posts[0]["userId"] == 2


def test_create_post_sends_json_body() -> None:
    transport = httpx.MockTransport(json_response)
    with PostsApiClient(transport=transport) as api:
        created = api.create_post("Day 6", "HTTPX practice", user_id=3)
    assert created == {
        "id": 101,
        "title": "Day 6",
        "body": "HTTPX practice",
        "userId": 3,
    }


def test_http_error_is_not_silently_ignored() -> None:
    transport = httpx.MockTransport(json_response)
    with PostsApiClient(transport=transport) as api:
        with pytest.raises(httpx.HTTPStatusError):
            api.get_post(404)
