from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Dict
import uuid

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory task storage
tasks: Dict[str, dict] = {}

class Task(BaseModel):
    title: str
    completed: bool = False

@app.get("/")
def serve_ui():
    return FileResponse("static/index.html")

@app.get("/api/tasks")
def get_tasks():
    return tasks

@app.post("/api/tasks")
def create_task(task: Task):
    task_id = str(uuid.uuid4())
    tasks[task_id] = task.dict()
    return {"id": task_id, **tasks[task_id]}

@app.put("/api/tasks/{task_id}")
def update_task(task_id: str, updated_task: Task):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = updated_task.dict()
    return {"id": task_id, **tasks[task_id]}

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"message": "Task deleted"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
