# Flask + Node.js Full Stack App

A full-stack registration form application with:
- **Frontend**: Node.js + Express + EJS
- **Backend**: Python Flask (REST API)
- **Infrastructure**: Docker + Docker Compose

---

## 📁 Project Structure

```
flask-node-project/
├── frontend/               # Node.js + Express
│   ├── views/
│   │   └── index.ejs       # Form template
│   ├── public/             # Static assets
│   ├── server.js           # Express app
│   ├── package.json
│   └── Dockerfile
├── backend/                # Python Flask
│   ├── app.py              # Flask app
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml      # Orchestration
├── .gitignore
└── README.md
```

---

## 🚀 Running with Docker Compose

```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up --build -d

# Stop all services
docker-compose down
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:5000

---

## 🛠 Running Locally (without Docker)

### Backend (Flask)
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend (Node.js)
```bash
cd frontend
npm install
FLASK_BACKEND_URL=http://localhost:5000 node server.js
```

---

## 🐳 Docker Hub

Push images to Docker Hub:

```bash
# Backend
docker build -t your-dockerhub-username/flask-backend:latest ./backend
docker push your-dockerhub-username/flask-backend:latest

# Frontend
docker build -t your-dockerhub-username/express-frontend:latest ./frontend
docker push your-dockerhub-username/express-frontend:latest
```

---

## 🌐 API Endpoints

| Method | Endpoint  | Description              |
|--------|-----------|--------------------------|
| GET    | /         | Flask welcome            |
| POST   | /process  | Process form submission  |
| GET    | /health   | Health check             |

### POST /process — Request Body
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": "21",
  "subject": "Computer Science",
  "gender": "Male",
  "interest": ["Web Development", "AI / ML"],
  "message": "Looking forward to it!"
}
```

---

## 📦 Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Frontend  | Node.js, Express, EJS |
| Backend   | Python 3.11, Flask, Gunicorn |
| Container | Docker, Docker Compose |
| Network   | Docker Bridge Network |
