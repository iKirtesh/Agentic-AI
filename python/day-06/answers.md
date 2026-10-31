# Day 6 Answer Guide

## A. Fundamentals
1. A request is the client's message to a server; a response is the server's reply.
2. GET reads, POST commonly creates, PUT replaces, PATCH partially updates, DELETE removes.
3. 401 means valid authentication credentials are missing or invalid; 403 means the server understood the request but refuses authorization.
4. A path parameter identifies a resource in the route (for example `/posts/12`); a query parameter modifies or filters the request (for example `/posts?userId=2`).
5. Timeouts bound waiting time and prevent a slow or unavailable service from holding resources indefinitely.

## B. Example solutions

### 1. Fetch a post title
```python
import httpx

response = httpx.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10.0,
)
response.raise_for_status()
print(response.json()["title"])
```

### 2. Filter by user
```python
response = httpx.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 2},
    timeout=10.0,
)
response.raise_for_status()
posts = response.json()
```

### 3. POST JSON
```python
payload = {"title": "Day 6", "body": "API practice", "userId": 1}
response = httpx.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload,
    timeout=10.0,
)
response.raise_for_status()
print(response.json())
```

### 4. Check status
```python
def require_success(response):
    response.raise_for_status()
    return response
```

### 5. Concurrent async calls
```python
import asyncio
import httpx

async def main():
    async with httpx.AsyncClient(
        base_url="https://jsonplaceholder.typicode.com",
        timeout=10.0,
    ) as client:
        responses = await asyncio.gather(
            client.get("/posts/1"),
            client.get("/posts/2"),
            client.get("/posts/3"),
        )
        for response in responses:
            response.raise_for_status()
            print(response.json()["title"])

asyncio.run(main())
```

### 6. Header
```python
response = httpx.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    headers={"User-Agent": "AgenticAI-Learning/1.0"},
    timeout=10.0,
)
```

### 7. Error handling
```python
try:
    response = httpx.get(url, timeout=2.0)
    response.raise_for_status()
except httpx.TimeoutException:
    print("The API took too long to respond")
except httpx.HTTPStatusError as exc:
    print("The API returned", exc.response.status_code)
except httpx.RequestError as exc:
    print("Network/request failure:", exc)
```

## Key lesson
Do not treat every failure as an empty successful result. Preserve useful error information so the caller (or agent) can decide whether to retry, ask for different input, or stop.
