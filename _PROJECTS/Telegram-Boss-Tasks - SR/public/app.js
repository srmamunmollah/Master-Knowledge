const STATUS_LABELS = { todo: 'To Do', in_progress: 'In Progress', done: 'Done' };
const POLL_INTERVAL_MS = 10000;
let currentUser = null;

async function init() {
  const meRes = await fetch('/api/me');
  if (!meRes.ok) {
    window.location.href = '/login.html';
    return;
  }
  currentUser = await meRes.json();
  document.getElementById('userInfo').textContent = `${currentUser.username} (${currentUser.role})`;
  if (currentUser.role !== 'owner') {
    document.getElementById('actionsHeader').style.display = 'none';
  }

  await loadTasks();
  setInterval(loadTasks, POLL_INTERVAL_MS);
}

async function loadTasks() {
  const res = await fetch('/api/tasks');
  if (res.status === 401) {
    window.location.href = '/login.html';
    return;
  }
  const tasks = await res.json();
  renderTasks(tasks);
}

function renderTasks(tasks) {
  const tbody = document.getElementById('taskBody');
  const emptyState = document.getElementById('emptyState');
  tbody.innerHTML = '';
  emptyState.style.display = tasks.length ? 'none' : 'block';

  for (const task of tasks) {
    const tr = document.createElement('tr');

    const msgTd = document.createElement('td');
    msgTd.textContent = task.message_text;
    tr.appendChild(msgTd);

    const createdTd = document.createElement('td');
    createdTd.textContent = new Date(task.created_at).toLocaleString();
    tr.appendChild(createdTd);

    const statusTd = document.createElement('td');
    const badge = document.createElement('span');
    badge.className = `badge badge-${task.status}`;
    badge.textContent = STATUS_LABELS[task.status] || task.status;
    statusTd.appendChild(badge);
    tr.appendChild(statusTd);

    const actionsTd = document.createElement('td');
    if (currentUser.role === 'owner') {
      const select = document.createElement('select');
      for (const [value, label] of Object.entries(STATUS_LABELS)) {
        const opt = document.createElement('option');
        opt.value = value;
        opt.textContent = label;
        if (value === task.status) opt.selected = true;
        select.appendChild(opt);
      }
      select.addEventListener('change', () => updateStatus(task.id, select.value));
      actionsTd.appendChild(select);
    }
    tr.appendChild(actionsTd);

    tbody.appendChild(tr);
  }
}

async function updateStatus(id, status) {
  await fetch(`/api/tasks/${id}`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status }),
  });
  loadTasks();
}

document.getElementById('logoutBtn').addEventListener('click', async () => {
  await fetch('/api/logout', { method: 'POST' });
  window.location.href = '/login.html';
});

init();
