import asyncio
from typing import Any, Iterable

import httpx

BASE_URL = "https://jsonplaceholder.typicode.com"


class DemoApiClient:
    def __init__(self, timeout: float = 10.0, transport: httpx.BaseTransport | None = None):
        self.client = httpx.Client(
            base_url=BASE_URL,
            timeout=timeout,
            transport=transport,
            headers={"Accept": "application/json"},
        )

    def get_post(self, post_id: int) -> dict[str, Any]:
        response = self.client.get(f"/posts/{post_id}")
        response.raise_for_status()
        return response.json()

    def close(self) -> None:
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


async def get_posts_async(post_ids: Iterable[int]) -> list[dict[str, Any]]:
    async with httpx.AsyncClient(base_url=BASE_URL, timeout=10.0) as client:
        async def fetch(post_id: int) -> dict[str, Any]:
            response = await client.get(f"/posts/{post_id}")
            response.raise_for_status()
            return response.json()

        return await asyncio.gather(*(fetch(post_id) for post_id in post_ids))
