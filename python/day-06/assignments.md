# Day 6 Assignments

Complete these in order. Try each task before opening `answers.md`.

## A. Fundamentals
1. Explain the difference between an HTTP request and response.
2. Give one realistic use case for GET, POST, PUT, PATCH and DELETE.
3. Explain the difference between 401 and 403.
4. What is the difference between a path parameter and a query parameter?
5. Why should an API client set a timeout?

## B. Coding
1. Fetch post 1 from JSONPlaceholder and print its title.
2. Fetch posts for user ID 2 using query parameters.
3. Send a POST request with a title, body and userId.
4. Implement a function that raises an informative error for non-2xx responses.
5. Implement an async function that fetches three posts concurrently.
6. Add a custom User-Agent header to a request.
7. Handle a timeout separately from an HTTP status error.

## C. Mini-project — Reusable API Client
Use `code/api_client.py` as a starting point.

Requirements:
- Use a reusable HTTPX client.
- Fetch one post by ID.
- Fetch posts filtered by user ID.
- Raise errors for unsuccessful responses.
- Configure a timeout.
- Provide an async function to fetch multiple post IDs concurrently.
- Write tests using HTTPX MockTransport; tests must not require internet access.

## D. Stretch tasks
1. Add a maximum concurrency limit for async requests using an asyncio semaphore.
2. Add retry with exponential backoff for selected transient failures only.
3. Validate the shape and types of returned JSON before using it.
4. Add a method that returns only the post title and user ID.

## Self-review checklist
- [ ] I can explain HTTP methods and status codes.
- [ ] I can use query parameters, headers and JSON bodies.
- [ ] I can use HTTPX Client and AsyncClient.
- [ ] I can distinguish timeout, request and status errors.
- [ ] I can explain why async helps with concurrent I/O.
- [ ] My tests run without a live API.
