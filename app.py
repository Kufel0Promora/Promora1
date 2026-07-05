from flask import Flask, request, jsonify
from flask_cors import CORS
import bcrypt
import json
import requests
import threading
import asyncio
import os
from config import SECRET_KEY, DISCORD_TOKEN, GUILD_ID

app = Flask(__name__)
app.secret_key = SECRET_KEY
CORS(app)

USERS_FILE = 'users.json'

# ============================================================
# URUCHOM BOTA W TLE (Z OBSŁUGĄ BŁĘDÓW)
# ============================================================

def run_bot():
    try:
        from bot import bot
        print("🤖 Uruchamianie bota...")
        bot.run(DISCORD_TOKEN)
    except Exception as e:
        print(f"❌ Błąd bota: {e}")

# Uruchom bota w osobnym wątku tylko jeśli DISCORD_TOKEN istnieje
if DISCORD_TOKEN and DISCORD_TOKEN != 'TWÓJ_TOKEN':
    thread = threading.Thread(target=run_bot)
    thread.daemon = True
    thread.start()
    print("🤖 Bot uruchomiony w tle")
else:
    print("⚠️ Brak tokena bota – bot nie zostanie uruchomiony")

# ============================================================
# FUNKCJE POMOCNICZE
# ============================================================

def load_users():
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

# ============================================================
# WERYFIKACJA PRZEZ API DISCORDA
# ============================================================

def verify_user_discord(user_id: str):
    if not DISCORD_TOKEN or DISCORD_TOKEN == 'TWÓJ_TOKEN':
        return None
    url = f"https://discord.com/api/v10/guilds/{GUILD_ID}/members/{user_id}"
    headers = {"Authorization": f"Bot {DISCORD_TOKEN}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return {
                'verified': True,
                'id': data['user']['id'],
                'username': data['user']['username'],
                'display_name': data.get('nick', data['user']['username'])
            }
        return None
    except:
        return None

# ============================================================
# ENDPOINTY API
# ============================================================

@app.route('/ping')
def ping():
    return "Pong!", 200

@app.route('/api/verify', methods=['POST'])
def verify():
    data = request.json
    user_id = data.get('userId')
    if not user_id:
        return jsonify({'error': 'Brak ID'}), 400
    result = verify_user_discord(user_id)
    if result:
        return jsonify(result)
    return jsonify({'verified': False, 'error': 'Nie znaleziono'}), 404

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    user_id = data.get('userId')
    password = data.get('password')
    confirm = data.get('confirmPassword')
    username = data.get('username', f'User_{user_id[-4:]}')
    
    if not user_id or not password:
        return jsonify({'error': 'Wypełnij wszystkie pola'}), 400
    if len(password) < 6:
        return jsonify({'error': 'Hasło min. 6 znaków'}), 400
    if password != confirm:
        return jsonify({'error': 'Hasła nie są identyczne'}), 400
    
    result = verify_user_discord(user_id)
    if not result:
        return jsonify({'error': 'Nie jesteś na serwerze Promora!'}), 400
    
    users = load_users()
    if user_id in users:
        return jsonify({'error': 'Już zarejestrowany'}), 400
    
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[user_id] = {
        'password': hashed.decode('utf-8'),
        'username': username,
        'banned': False,
        'score': 0,
        'rank': '🆕 Początkujący'
    }
    save_users(users)
    return jsonify({'success': True, 'message': 'Rejestracja udana!'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user_id = data.get('userId')
    password = data.get('password')
    
    users = load_users()
    if user_id not in users:
        return jsonify({'error': 'Nieprawidłowy ID lub hasło'}), 400
    if users[user_id].get('banned', False):
        return jsonify({'error': 'Konto zablokowane'}), 403
    
    hashed = users[user_id]['password'].encode('utf-8')
    if not bcrypt.checkpw(password.encode('utf-8'), hashed):
        return jsonify({'error': 'Nieprawidłowy ID lub hasło'}), 400
    
    return jsonify({
        'success': True,
        'user': {
            'id': user_id,
            'username': users[user_id]['username'],
            'score': users[user_id].get('score', 0),
            'rank': users[user_id].get('rank', '🆕 Początkujący')
        }
    })

@app.route('/api/save-score', methods=['POST'])
def save_score():
    data = request.json
    user_id = data.get('userId')
    score = data.get('score')
    
    if not user_id:
        return jsonify({'error': 'Brak ID'}), 400
    
    users = load_users()
    if user_id not in users:
        return jsonify({'error': 'Użytkownik nie istnieje'}), 400
    if users[user_id].get('banned', False):
        return jsonify({'error': 'Konto zablokowane'}), 403
    
    users[user_id]['score'] = score
    if score >= 500:
        users[user_id]['rank'] = '👑 Legenda'
    elif score >= 100:
        users[user_id]['rank'] = '🏆 Mistrz'
    elif score >= 50:
        users[user_id]['rank'] = '⭐ Doświadczony'
    elif score >= 10:
        users[user_id]['rank'] = '🌟 Nowicjusz'
    else:
        users[user_id]['rank'] = '🆕 Początkujący'
    
    save_users(users)
    return jsonify({
        'success': True,
        'rank': users[user_id]['rank'],
        'score': users[user_id]['score']
    })

@app.route('/api/leaderboard', methods=['GET'])
def leaderboard():
    users = load_users()
    leaderboard = []
    for user_id, data in users.items():
        if not data.get('banned', False):
            leaderboard.append({
                'id': user_id,
                'username': data.get('username', f'User_{user_id[-4:]}'),
                'score': data.get('score', 0),
                'rank': data.get('rank', '🆕 Początkujący')
            })
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    return jsonify(leaderboard[:10])

@app.route('/api/reset-password', methods=['POST'])
def reset_password():
    data = request.json
    user_id = data.get('userId')
    new_password = data.get('newPassword')
    
    if not user_id or not new_password:
        return jsonify({'error': 'Brak ID lub nowego hasła'}), 400
    
    if len(new_password) < 6:
        return jsonify({'error': 'Hasło musi mieć co najmniej 6 znaków'}), 400
    
    users = load_users()
    if user_id not in users:
        return jsonify({'error': 'Użytkownik nie istnieje'}), 404
    
    hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    users[user_id]['password'] = hashed.decode('utf-8')
    save_users(users)
    
    return jsonify({'success': True, 'message': 'Hasło zostało zresetowane!'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
