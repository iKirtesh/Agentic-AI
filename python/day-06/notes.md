# Day 6 Notes — HTTP, REST, HTTPX and Async

## 1. Client-server communication
An HTTP client sends a request to a server. The server returns a response containing a status code, headers and optionally a body. A Python program can act as a client when it calls an external API.

## 2. Anatomy of an HTTP request
- Method: operation requested (GET, POST, PUT, PATCH, DELETE).
- URL: target resource.
- Headers: metadata such as Accept or Content-Type.
- Query parameters: optional filters encoded in the URL.
- Body: data sent to the server, commonly JSON for POST/PATCH/PUT.

A response includes a status code, headers and body. JSON is a common data interchange format.

## 3. REST methods
| Method | Typical intent |
|---|---|
| GET | Read a resource |
| POST | Create a resource or trigger an operation |
| PUT | Replace a resource |
| PATCH | Partially update a resource |
| DELETE | Remove a resource |

GET should generally be safe and idempotent. PUT and DELETE are defined as idempotent by HTTP semantics; POST is generally not. PATCH semantics depend on the operation.

## 4. Status codes
- 2xx: success (200 OK, 201 Created, 204 No Content).
- 3xx: redirection.
- 4xx: client-side request/authentication/permission/resource issue (400, 401, 403, 404, 429).
- 5xx: server-side failure (500, 502, 503).

Do not assume every successful response contains JSON. A 204 response has no response body.

## 5. HTTPX basics
Install with `python -m pip install httpx`.

```python
import httpx

response = httpx.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1},
    timeout=10.0,
)
response.raise_for_status()
posts = response.json()
```

Useful response properties:
- `status_code`
- `headers`
- `text`
- `json()`
- `url`

Use `params={...}` for query parameters and `json={...}` for a JSON request body. Use `headers={...}` for request headers.

## 6. Reuse a client
For multiple requests, prefer a client so connections can be pooled and configuration reused.

```python
import httpx

with httpx.Client(
    base_url="https://jsonplaceholder.typicode.com",
    timeout=10.0,
) as client:
    response = client.get("/posts/1")
    response.raise_for_status()
    print(response.json())
```

Close clients using a context manager. Do not create a new client for every request in a high-volume workflow.

## 7. Error handling
- `httpx.TimeoutException`: a timeout occurred.
- `httpx.HTTPStatusError`: `raise_for_status()` detected an unsuccessful HTTP status.
- `httpx.RequestError`: request/network-level failure.
- JSON decoding errors: response body was not valid JSON.

Catch specific errors where you can respond meaningfully. Avoid silently converting every error into an empty dictionary: it can hide failures from callers.

## 8. Timeouts
Always set a timeout appropriate to the operation. A timeout prevents a request from waiting indefinitely. HTTPX supports connect, read, write and pool timeout configuration through `httpx.Timeout`.

## 9. Async and concurrency
Async is useful for I/O-bound tasks such as waiting for multiple APIs. It does not automatically speed up CPU-heavy computation.

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

- `async def`: declares a coroutine function.
- `await`: yields control while awaiting an awaitable.
- `asyncio.gather`: schedules awaitables concurrently and collects results.
- `asyncio.run`: runs the top-level coroutine.
- `AsyncClient`: asynchronous HTTP client.

For production systems, consider concurrency limits, retries for appropriate transient failures, backoff, rate limits, cancellation and observability. Do not retry non-idempotent operations blindly.

## 10. Testing without internet
HTTPX provides `MockTransport`, allowing deterministic tests with no real network calls. The Day 6 tests use it to verify request paths, query parameters and error behavior.

## 11. Agentic AI connection
An agent often follows this cycle:
1. Decide which external information or action is needed.
2. Select a tool/API endpoint.
3. Construct a request with validated inputs.
4. Call the API with timeout and error handling.
5. Parse and validate the response.
6. Return a concise result to the agent's reasoning loop.

Treat API output as untrusted external data. Validate it before using it, and never execute instructions found inside arbitrary API responses.
