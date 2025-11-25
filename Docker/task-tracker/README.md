# 📋 Task Tracker

A simple and elegant task management application built with FastAPI, HTML, CSS, and JavaScript. Perfect for learning Docker containerization concepts.

## Features

- ✅ Create, read, update, and delete tasks
- 📊 Real-time statistics dashboard
- 🎨 Modern, responsive UI
- 🚀 RESTful API built with FastAPI
- 💾 In-memory storage (resets on restart)

## Project Structure

```
task-tracker/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── .dockerignore          # Docker ignore file
├── README.md              # This file
└── static/
    ├── index.html         # Frontend HTML
    ├── styles.css         # Styling
    └── app.js             # JavaScript logic
```

## Running Locally (Without Docker)

### Prerequisites
- Python 3.11 or higher

### Steps

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

4. **Access the application:**
   Open your browser and navigate to `http://localhost:8000`

## Running with Docker

### Prerequisites
- Docker installed on your system

### Build and Run

1. **Build the Docker image:**
   ```bash
   docker build -t task-tracker .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 task-tracker
   ```

3. **Access the application:**
   Open your browser and navigate to `http://localhost:8000`

### Useful Docker Commands

- **List running containers:**
  ```bash
  docker ps
  ```

- **Stop the container:**
  ```bash
  docker stop <container_id>
  ```

- **Remove the container:**
  ```bash
  docker rm <container_id>
  ```

- **Remove the image:**
  ```bash
  docker rmi task-tracker
  ```

- **View container logs:**
  ```bash
  docker logs <container_id>
  ```

- **Run container in detached mode:**
  ```bash
  docker run -d -p 8000:8000 --name my-task-tracker task-tracker
  ```

## API Endpoints

- `GET /` - Serve the frontend
- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/{task_id}` - Update a task
- `DELETE /api/tasks/{task_id}` - Delete a task
- `GET /health` - Health check endpoint

## Learning Docker with This Project

This application is designed to help you understand:

1. **Dockerfile syntax** - How to define a container image
2. **Image layers** - How Docker caches and builds layers
3. **Port mapping** - Exposing container ports to host
4. **Container lifecycle** - Building, running, stopping containers
5. **Best practices** - Using .dockerignore, multi-stage builds concepts

## Next Steps for Learning

- Try modifying the Dockerfile to use different base images
- Experiment with Docker Compose for multi-container setups
- Add environment variables for configuration
- Implement persistent storage with Docker volumes
- Create a multi-stage build to optimize image size

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** Vanilla HTML, CSS, JavaScript
- **Server:** Uvicorn ASGI server
- **Containerization:** Docker

## License

MIT License - Feel free to use this project for learning purposes!