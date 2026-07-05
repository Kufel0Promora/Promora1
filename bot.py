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

if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
