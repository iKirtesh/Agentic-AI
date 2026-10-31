"""Small synchronous and asynchronous JSONPlaceholder API clients."""

from __future__ import annotations

import asyncio
from typing import Any, Iterable

import httpx

BASE_URL = "https://jsonplaceholder.typicode.com"


class PostsApiClient:
    """Synchronous API client for JSONPlaceholder posts."""

    def __init__(self, timeout: float = 10.0, transport: httpx.BaseTransport | None = None):
        self._client = httpx.Client(
            base_url=BASE_URL,
            timeout=timeout,
            transport=transport,
            headers={"Accept": "application/json", "User-Agent": "AgenticAI-Day6/1.0"},
        )

    def get_post(self, post_id: int) -> dict[str, Any]:
        response = self._client.get(f"/posts/{post_id}")
        response.raise_for_status()
        return response.json()

    def get_posts_by_user(self, user_id: int) -> list[dict[str, Any]]:
        response = self._client.get("/posts", params={"userId": user_id})
        response.raise_for_status()
        return response.json()

    def create_post(self, title: str, body: str, user_id: int = 1) -> dict[str, Any]:
        response = self._client.post(
            "/posts",
            json={"title": title, "body": body, "userId": user_id},
        )
        response.raise_for_status()
        return response.json()

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "PostsApiClient":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


async def fetch_posts_async(
    post_ids: Iterable[int],
    timeout: float = 10.0,
) -> list[dict[str, Any]]:
    """Fetch multiple posts concurrently using one AsyncClient."""
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=timeout) as client:
        async def fetch_one(post_id: int) -> dict[str, Any]:
            response = await client.get(f"/posts/{post_id}")
            response.raise_for_status()
            return response.json()

        return await asyncio.gather(*(fetch_one(post_id) for post_id in post_ids))
