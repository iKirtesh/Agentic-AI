import asyncio

from api_client import fetch_posts_async


async def main() -> None:
    posts = await fetch_posts_async([1, 2, 3])
    for post in posts:
        print(post["id"], post["title"])


if __name__ == "__main__":
    asyncio.run(main())
