import discord
from discord.ext import commands
from config import DISCORD_TOKEN, GUILD_ID

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'🤖 Zalogowano jako {bot.user}')
    guild = bot.get_guild(GUILD_ID)
    if guild:
        print(f'📡 Serwer: {guild.name} (ID: {guild.id})')
        print(f'👥 Liczba członków: {guild.member_count}')
    else:
        print(f'❌ Nie znaleziono serwera o ID: {GUILD_ID}')

@bot.command(name='check_user')
async def check_user(ctx, user_id: str):
    guild = ctx.guild
    if not guild:
        await ctx.send("❌ Ta komenda działa tylko na serwerze!")
        return
    try:
        member = await guild.fetch_member(int(user_id))
        if member:
            await ctx.send(f"✅ Użytkownik {member.display_name} jest na serwerze!")
        else:
            await ctx.send(f"❌ Użytkownik o ID `{user_id}` nie znaleziony.")
    except:
        await ctx.send(f"❌ Użytkownik o ID `{user_id}` nie znaleziony.")

@bot.command(name='reset_password')
@commands.has_permissions(administrator=True)
async def reset_password(ctx, user_id: str, new_password: str):
    import json, bcrypt, os
    users_file = 'users.json'
    
    # Sprawdź czy plik istnieje
    if not os.path.exists(users_file):
        await ctx.send("❌ Baza użytkowników nie istnieje.")
        return
    
    # Wczytaj użytkowników
    with open(users_file, 'r', encoding='utf-8') as f:
        users = json.load(f)
    
    # Sprawdź czy użytkownik istnieje
    if user_id not in users:
        await ctx.send(f"❌ Użytkownik o ID `{user_id}` nie istnieje.")
        return
    
    # Hashuj nowe hasło
    hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    users[user_id]['password'] = hashed.decode('utf-8')
    
    # Zapisz
    with open(users_file, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2, ensure_ascii=False)
    
    await ctx.send(f"✅ Hasło dla użytkownika `{user_id}` zostało zresetowane!")

@bot.command(name='reset_password')
@commands.has_permissions(administrator=True)
async def reset_password(ctx, user_id: str, new_password: str):
    import json, bcrypt, os, requests
    
    # Sprawdź czy użytkownik ma uprawnienia (tylko admin)
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("❌ Tylko administrator może resetować hasła!")
        return
    
    # Sprawdź czy hasło ma minimum 6 znaków
    if len(new_password) < 6:
        await ctx.send("❌ Hasło musi mieć co najmniej 6 znaków!")
        return
    
    # Ścieżka do pliku users.json na Render (przez API)
    try:
        # Pobierz listę użytkowników
        response = requests.get('https://promora-backend.onrender.com/api/leaderboard')
        if response.status_code != 200:
            await ctx.send("❌ Nie udało się połączyć z bazą danych!")
            return
        
        users_data = response.json()
        
        # Sprawdź czy użytkownik istnieje
        user_exists = False
        for user in users_data:
            if user['id'] == user_id:
                user_exists = True
                break
        
        if not user_exists:
            await ctx.send(f"❌ Użytkownik o ID `{user_id}` nie istnieje!")
            return
        
        # Wyślij zapytanie do API resetowania hasła
        reset_response = requests.post(
            'https://promora-backend.onrender.com/api/reset-password',
            json={'userId': user_id, 'newPassword': new_password},
            headers={'Content-Type': 'application/json'}
        )
        
        if reset_response.status_code == 200:
            await ctx.send(f"✅ Hasło dla użytkownika `{user_id}` zostało zresetowane!")
        else:
            await ctx.send(f"❌ Błąd resetowania hasła: {reset_response.text}")
            
    except Exception as e:
        await ctx.send(f"❌ Błąd: {str(e)}")
        
if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
