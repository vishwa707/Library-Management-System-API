# Library Management System API

## Overview
This project implements a **Library Management System** API using Flask. The API allows for the management of books and members in a library, providing the ability to perform CRUD operations on both entities. The system includes basic features such as authentication, search functionality, pagination, and token-based access control.

## Key Features
1. **Books Management**:
   - Add a new book
   - View all books
   - Get details of a single book
   - Update a book's details
   - Delete a book
   - Search books by title or author
   - Pagination for listing books

2. **Members Management**:
   - Add a new member
   - View all members
   - Get details of a single member
   - Update member information
   - Delete a member

3. **Authentication**:
   - Token-based authentication for secure access to API routes.
   - Only requests with the correct authorization token can interact with the system.

## Technologies Used
- **Flask**: A micro-framework for Python used to build the API.
- **Python**: Programming language used to implement the application.

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine:

```bash
git clone https://github.com/vishwa707/Library-Management-System-API
```

### 2. Install Dependencies
This project uses Flask. To install Flask and any required dependencies, follow these steps:

1. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:
      ```bash
      .\venv\Scripts\activate
      ```

    - On MacOS/Linux:
      ```bash
      source venv/bin/activate
      ```

3. Install Flask using pip:

    ```bash
    pip install flask
    ```
### 3. Running the Application
To start the application, use the following command:

```bash
python LMS.py
```
The Flask app will start running on http://127.0.0.1:5000/ by default.

### 4. API Authentication
To interact with the API, you need to include a valid token in the request headers:
You can make API requests using tools like Postman or crul

### API Endpoints
Books
   - POST /books: Add a new book.
       - Request body: JSON object with book details (title, author, isbn, year).
        - Example:
          ```bash
          {
           "title": "Book Title",
           "author": "Author Name",
           "isbn": "123456789",
           "year": 2023
          }
          ```
   - GET `/books`: Get all books with optional search and pagination.
   - Query params: `search` (string), `page`(int), `per_page` (int).
   - Example request: `GET /books?search=Harry&page=1&per_page=5`
   - GET `/books/{book_id}`: Get details of a specific book by its ID.
   - PUT `/books/{book_id}`: Update a specific book by its ID.
   - Request body: JSON object with updated book details.
   - DELETE `/books/{book_id}`: Delete a book by its ID.

Members
   - POST `/members`: Add a new member.
   - Request body: JSON object with member details (`name`, `email`).
   - GET `/members`: Get all members.
   - GET `/members/{member_id}`: Get details of a specific member by their ID.
   - PUT `/members/{member_id}`: Update a specific member by their ID.
   - Request body: JSON object with updated member details.
   - DELETE `/members/{member_id}`: Delete a member by their ID.
     
## Authentication
All the API routes require a valid Authorization token in the request headers.
```bash
Authorization: alpha beta gamma
```
If the token is missing or incorrect, the server will return an Unauthorized error with HTTP status code 401.

## Design Choices
1. Data Storage:
   - The data (books and members) is stored in memory in the data dictionary. This is for simplicity and demonstration purposes. In a production system, a database like MySQL, PostgreSQL, or MongoDB would be used.
2. Token-based Authentication:
   - The system uses a hardcoded token (alpha beta gamma) to authenticate requests. This ensures that only authorized users can access the API endpoints.
   - In a real-world scenario, you would use more secure methods like OAuth2, JWT tokens, or session-based authentication.
3. Search and Pagination:
   - The search functionality allows users to search books by title or author. The search term is case-insensitive.
   - Pagination ensures that API responses for books are manageable and don't overwhelm the user with too much data. The page and per_page query parameters control this.
4. Error Handling:
   - The system includes basic error handling. If an entity (book or member) is not found, the API will return a 404 Not Found status with a relevant error message.
5. No Third-party Libraries:
   - As per the requirements, no third-party libraries except for Flask were used. The token-based authentication and search functionality were implemented manually.

## Assumptions
   - The API assumes that the request body for adding or updating books and members is well-formed (i.e., valid JSON).
   - The token is hardcoded and must be passed with every request for security.
   - The system uses in-memory data storage, meaning the data will be lost when the server is restarted.

## Limitations
1. **Persistence:** The data is stored in memory and will be lost if the server is restarted. To make it persistent, you would need to integrate a database.
2. **Authentication**: The authentication mechanism is basic and not secure for production use. It is recommended to implement more secure methods in a real-world scenario.
3. **No User Management:** There is no user role management; every request with the correct token is granted full access.
4. **Search Functionality:** The search functionality is quite simple and only works for titles and authors. Advanced search filters could be added for other fields in the future.

## Tests
For testing the functionality of the API, you can use Postman or curl to send requests to the endpoints. Each API call should include the correct token for authentication.

**Example tests:**
Books
1. POST `/books`: Add a new book with valid data.
2. GET `/books`: Get all books, testing both search and pagination.
3. GET `/books/{book_id}`: Get a single book by its ID.
4. PUT `/books/{book_id}`: Update an existing book.
5. DELETE `/books/{book_id}`: Delete a book.

Members
1. POST `/memebers`: Add a new member with valid data.
2. GET `/members`: Get all members
3. GET `/members/{member_id}`: Get a single member by its ID.
4. PUT `/members/{member_id}`: Update an existing member.
5. DELETE `/members/{member_id}`: Delete a member.
