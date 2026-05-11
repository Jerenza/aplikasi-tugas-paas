from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Simulasi database sederhana (in-memory)
todos = []
next_id = 1

database_url = os.environ.get('DATABASE_URL')

@app.route('/')
def beranda():
    return jsonify({
        'aplikasi': 'API To-Do List',
        'versi': '1.0.0',
        'status': 'aktif',
        'endpoints': ['/todos', '/health']
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'sehat', 'total_todos': len(todos)})

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'data': todos, 'total': len(todos)})

@app.route('/todos', methods=['POST'])
def tambah_todo():
    global next_id
    data = request.get_json()
    todo_baru = {
        'id': next_id,
        'judul': data.get('judul', ''),
        'selesai': False
    }
    todos.append(todo_baru)
    next_id += 1
    return jsonify({'pesan': 'Todo berhasil ditambahkan', 'data': todo_baru}), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def hapus_todo(todo_id):
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({'pesan': f'Todo {todo_id} dihapus'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

print("APPLICATION BOOT SUCCESS")