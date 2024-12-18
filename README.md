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
   - Only requests with the correct authorization token (`alpha beta gamma`) can interact with the system.

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
```bash
Authorization: alpha beta gamma
```
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
   - GET /books: Get all books with optional search and pagination.
   - Query params: `search` (string), `page`(int), `per_page` (int).
   - Example request: `GET /books?search=Harry&page=1&per_page=5`
   - GET /books/{book_id}: Get details of a specific book by its ID.
   - PUT /books/{book_id}: Update a specific book by its ID.
   - Request body: JSON object with updated book details.
   - DELETE /books/{book_id}: Delete a book by its ID.

Members
   - POST /members: Add a new member.
   - Request body: JSON object with member details (`name`, `email`).
   - GET /members: Get all members.
   - GET /members/{member_id}: Get details of a specific member by their ID.
   - PUT /members/{member_id}: Update a specific member by their ID.
   - Request body: JSON object with updated member details.
   - DELETE /members/{member_id}: Delete a member by their ID.
