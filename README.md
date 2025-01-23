Centralized Authentication Service

This project provides a centralized authentication service with support for **email/password** and **Google OAuth2** login. It consists of a **FastAPI backend** and a **React frontend**.

## Features
- **User Registration**: Register new users with email and password.
- **User Login**: Log in with email and password or Google OAuth2.
- **JWT Authentication**: Secure authentication using JSON Web Tokens (JWT).
- **Protected Routes**: Frontend routes are protected and accessible only to authenticated users.
- **Google OAuth2 Integration**: Seamless login with Google accounts.

## Technologies Used
- **Backend**: FastAPI (Python)
- **Frontend**: React (JavaScript)
- **Database**: PostgreSQL
- **Authentication**: JWT, Google OAuth2

---

## Setup Instructions

### Prerequisites
- Python 3.11
- Node.js (for frontend)
- PostgreSQL
- Google OAuth2 credentials (Client ID and Client Secret)

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
   - Create a `.env` file in the `backend` directory:
     ```plaintext
     DATABASE_URL=postgresql://user:password@localhost:5432/authservice
     SECRET_KEY=your-secret-key
     GOOGLE_CLIENT_ID=your-google-client-id
     GOOGLE_CLIENT_SECRET=your-google-client-secret
     GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback
     ```

4. **Run the Backend Server**:
   ```bash
   uvicorn main:app --reload
   ```
   - The backend will be available at `http://localhost:8000`.

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
   - Create a `.env` file in the `frontend` directory:
     ```plaintext
     REACT_APP_API_URL=http://localhost:8000
     ```

4. **Run the Frontend Server**:
   ```bash
   npm start
   ```
   - The frontend will be available at `http://localhost:3000`.

---

## Usage
1. **Register a New User**:
   - Navigate to `/register` and fill out the registration form.

2. **Log In**:
   - Navigate to `/login` and log in with your email and password or Google OAuth2.

3. **Access Protected Routes**:
   - After logging in, you can access protected routes like the home page (`/`).

4. **Log Out**:
   - Click the logout button on the home page to log out.

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
  Email: vigneshwarankbgv@gmail.com  
  GitHub: [VigneshwaranKbgv](https://github.com/VigneshwaranKbgv)
```
