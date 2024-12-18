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
git clone <https://github.com/vishwa707/Library-Management-System-API>
