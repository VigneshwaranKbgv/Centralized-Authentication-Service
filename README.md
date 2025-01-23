# Centralized Authentication Service

This project provides a centralized authentication service with support for **email/password** and **Google OAuth2** login. It consists of a **FastAPI backend** and a **React frontend**. The backend uses **Redis** for token blacklisting and session management.

---

## Features

- **User Registration**: Register new users with email and password.
- **User Login**: Log in with email and password or Google OAuth2.
- **JWT Authentication**: Secure authentication using JSON Web Tokens (JWT).
- **Token Blacklisting**: Blacklist JWT tokens on logout using Redis.
- **Protected Routes**: Frontend routes are protected and accessible only to authenticated users.
- **Google OAuth2 Integration**: Seamless login with Google accounts.
- **Redis Integration**: Used for token blacklisting and session management.

---

## Technologies Used

- **Backend**: FastAPI (Python)
- **Frontend**: React (JavaScript)
- **Database**: PostgreSQL
- **Authentication**: JWT, Google OAuth2
- **Caching/Session Management**: Redis

---

## Setup Instructions

### Prerequisites

- Python 3.11
- Node.js (Development tool for frontend)
- PostgreSQL
- Redis
- Google OAuth2 credentials (Client ID and Client Secret)

---

### Backend Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/VigneshwaranKbgv/centralized-auth-service.git
   cd centralized-auth-service/app/backend
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the `backend` directory:
   ```plaintext
   DATABASE_URL=postgresql://user:password@localhost:5432/authservice
   SECRET_KEY=your-secret-key
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
   GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback
   REDIS_HOST=localhost
   REDIS_PORT=6379
   REDIS_DB=0
   ```

4. **Run the Backend Server**:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will be available at [http://localhost:8000](http://localhost:8000).

---

### Frontend Setup

1. **Navigate to the Frontend Directory**:
   ```bash
   cd ../frontend
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the `frontend` directory:
   ```plaintext
   REACT_APP_API_URL=http://localhost:8000
   ```

4. **Run the Frontend Server**:
   ```bash
   npm start
   ```
   The frontend will be available at [http://localhost:3000](http://localhost:3000).

---

## Usage

1. **Register a New User**:
   - Navigate to `/register` and fill out the registration form.

2. **Log In**:
   - Navigate to `/login` and log in with your email and password or Google OAuth2.

3. **Access Protected Routes**:
   - After logging in, you can access protected routes like the home page (`/`).

4. **Log Out**:
   - Click the logout button on the home page to log out. This will blacklist the token in Redis.

---

## Redis Integration

Redis is used for:
- **Token Blacklisting**: When a user logs out, their JWT token is added to a Redis blacklist.
- **Session Management**: User sessions can be stored in Redis for scalability and performance.

### Redis Commands for Debugging
- **List All Keys**:
  ```bash
  redis-cli KEYS *
  ```
- **Check a Specific Key**:
  ```bash
  redis-cli GET <key>
  ```
- **Check Key Expiration**:
  ```bash
  redis-cli TTL <key>
  ```

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

---

## Contact

For questions or feedback, please contact:

- **Vigneshwaran K**
- Email: [vigneshwarankbgv@gmail.com](mailto:vigneshwarankbgv@gmail.com)
- GitHub: [VigneshwaranKbgv](https://github.com/VigneshwaranKbgv)

---
