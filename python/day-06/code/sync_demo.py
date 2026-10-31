from api_client import PostsApiClient


def main() -> None:
    with PostsApiClient() as api:
        post = api.get_post(1)
        print("Post title:", post["title"])

        posts = api.get_posts_by_user(1)
        print("Posts for user 1:", len(posts))

        created = api.create_post(
            title="Learning Agentic AI",
            body="Practising HTTPX on Day 6.",
            user_id=1,
        )
        print("Simulated created post ID:", created["id"])


if __name__ == "__main__":
    main()
