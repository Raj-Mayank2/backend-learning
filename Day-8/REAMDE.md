# Day 8 — Error Handling

## What I Learned

- HTTP status codes
- HTTPException
- raise HTTPException
- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 422 Validation Error
- status module
- Custom error messages

## Key Concepts

401 → Authentication required
403 → Authenticated but not allowed
404 → Resource doesn't exist
422 → Request validation failed

## Challenge

Student API with error handling

## Key Takeaway

Use HTTPException to stop an endpoint and return a meaningful HTTP error response.