async function fetchTasks() {
    const res = await fetch('/api/tasks');
    const tasks = await res.json();
    renderTasks(tasks);
    updateStats(tasks);
}

async function addTask() {
    const title = document.getElementById('taskTitle').value;
    if (!title) return;

    await fetch('/api/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title })
    });

    document.getElementById('taskTitle').value = '';
    fetchTasks();
}

async function toggleTask(id, completed) {
    await fetch(`/api/tasks/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            title: document.getElementById(`label-${id}`).innerText, 
            completed 
        })
    });

    fetchTasks();
}

async function deleteTask(id) {
    await fetch(`/api/tasks/${id}`, { method: 'DELETE' });
    fetchTasks();
}

function renderTasks(tasks) {
    const container = document.getElementById('taskList');
    container.innerHTML = '';

    Object.entries(tasks).forEach(([id, task]) => {
        const li = document.createElement('li');

        li.innerHTML = `
            <span id="label-${id}" style="text-decoration: ${task.completed ? 'line-through' : 'none'}">
                ${task.title}
            </span>
            <div>
                <button onclick="toggleTask('${id}', ${!task.completed})">Toggle</button>
                <button onclick="deleteTask('${id}')">Delete</button>
            </div>
        `;

        container.appendChild(li);
    });
}

function updateStats(tasks) {
    const total = Object.keys(tasks).length;
    const completed = Object.values(tasks).filter(t => t.completed).length;
    const pending = total - completed;

    document.getElementById('stats').innerText = 
        `Total: ${total} | Completed: ${completed} | Pending: ${pending}`;
}

fetchTasks();
