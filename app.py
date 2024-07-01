# app.py
from flask import Flask, request, jsonify
import sqlite3
from languages.python import compile_and_run_python
from languages.javascript import compile_and_run_javascript
from languages.java import compile_and_run_java

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('compilerd.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS leaderboard (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        language TEXT NOT NULL,
        code TEXT NOT NULL,
        result TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/submit', methods=['POST'])
def submit_code():
    data = request.get_json()
    username = data['username']
    language = data['language']
    code = data['code']

    # Call the appropriate function to compile and run the code
    if language == 'python':
        result = compile_and_run_python(code)
    elif language == 'javascript':
        result = compile_and_run_javascript(code)
    elif language == 'java':
        result = compile_and_run_java(code)
    else:
        return jsonify({'error': 'Unsupported language'}), 400

    # Store the result in the leaderboard
    conn = sqlite3.connect('compilerd.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO leaderboard (username, language, code, result)
    VALUES (?, ?, ?, ?)
    ''', (username, language, code, result['stdout'] + result['stderr']))
    conn.commit()
    conn.close()

    return jsonify(result)

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    conn = sqlite3.connect('compilerd.db')
    c = conn.cursor()
    c.execute('SELECT username, language, result, created_at FROM leaderboard ORDER BY created_at DESC')
    rows = c.fetchall()
    conn.close()

    leaderboard = []
    for row in rows:
        leaderboard.append({
            'username': row[0],
            'language': row[1],
            'result': row[2],
            'created_at': row[3]
        })

    return jsonify(leaderboard)

if __name__ == '__main__':
    app.run(debug=True)
# app.py
from flask import Flask, request, jsonify
import sqlite3
from languages.python import compile_and_run_python
from languages.javascript import compile_and_run_javascript
from languages.java import compile_and_run_java

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('compilerd.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS leaderboard (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        language TEXT NOT NULL,
        code TEXT NOT NULL,
        result TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/submit', methods=['POST'])
def submit_code():
    data = request.get_json()
    username = data['username']
    language = data['language']
    code = data['code']

    # Call the appropriate function to compile and run the code
    if language == 'python':
        result = compile_and_run_python(code)
    elif language == 'javascript':
        result = compile_and_run_javascript(code)
    elif language == 'java':
        result = compile_and_run_java(code)
    else:
        return jsonify({'error': 'Unsupported language'}), 400

    # Store the result in the leaderboard
    conn = sqlite3.connect('compilerd.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO leaderboard (username, language, code, result)
    VALUES (?, ?, ?, ?)
    ''', (username, language, code, result['stdout'] + result['stderr']))
    conn.commit()
    conn.close()

    return jsonify(result)

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    conn = sqlite3.connect('compilerd.db')
    c = conn.cursor()
    c.execute('SELECT username, language, result, created_at FROM leaderboard ORDER BY created_at DESC')
    rows = c.fetchall()
    conn.close()

    leaderboard = []
    for row in rows:
        leaderboard.append({
            'username': row[0],
            'language': row[1],
            'result': row[2],
            'created_at': row[3]
        })

    return jsonify(leaderboard)

if __name__ == '__main__':
    app.run(debug=True)
