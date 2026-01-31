# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, scalable REST APIs using the FastAPI framework. You'll create a web service that handles HTTP requests and responses while implementing best practices for API design and documentation.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Build a simple REST API with FastAPI that manages a collection of data (e.g., a to-do list, book catalog, or student records). Your API should handle basic CRUD (Create, Read, Update, Delete) operations.

#### Requirements
Completed API should:

- Set up a FastAPI application with proper project structure
- Implement GET endpoints to retrieve all items and individual items by ID
- Implement a POST endpoint to create new items
- Implement a PUT endpoint to update existing items
- Implement a DELETE endpoint to remove items
- Use Pydantic models for request/response validation
- Include proper HTTP status codes for different scenarios
- Provide auto-generated API documentation (Swagger UI)

### 🛠️ Add Error Handling and Validation

#### Description
Enhance your API with robust error handling, input validation, and meaningful error responses.

#### Requirements
Completed API should:

- Validate input data using Pydantic models with appropriate constraints (e.g., min/max length, required fields)
- Return appropriate HTTP error codes (400, 404, 500) with descriptive messages
- Handle edge cases gracefully (e.g., requesting non-existent items)
- Include request/response examples in API documentation
- Test the API to ensure all endpoints work correctly
