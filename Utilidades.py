import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.members = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f"Pronto! {bot.user}")
    await bot.tree.sync()

@bot.tree.command(name="ping", description="Verifica se o Bot Está online")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)  
    await interaction.response.send_message(f"Pong!! \nLatência: {latency}ms")

@bot.tree.command(name="produtos", description="Mostra os produtos da PerfectTea")
async def produtos(interaction: discord.Interaction):
    await interaction.response.send_message("https://imgur.com/a/FZ3KKTv")

@bot.tree.command(name="site", description="Mostra o site da PerfectTea")
async def site(interaction: discord.Interaction):
    await interaction.response.send_message("<:bonzibuddy:1421905197554208829> https://perfecttea.squareweb.app")

@bot.tree.command(name="anunciar", description="⌈ Staff ⌋ Anuncia em algum canal")
async def anunciar(
    interaction: discord.Interaction, 
    tempo: str, 
    mensagem: str, 
    canal: discord.TextChannel = None
):
    """
    tempo: formato '10s', '5m', '2h'
    mensagem: o que será enviado depois
    canal: opcional, canal onde a mensagem será enviada
    """
    target_channel = canal or interaction.channel  
    await interaction.response.send_message(f"⏱ Timer iniciado para {target_channel.mention}: a mensagem será enviada em {tempo}")

    unidades = {"s": 1, "m": 60, "h": 3600}
    try:
        if tempo[-1] not in unidades:
            await interaction.followup.send("Formato inválido! Use 's', 'm' ou 'h' (ex: 10s, 5m)")
            return
        segundos = int(tempo[:-1]) * unidades[tempo[-1]]
    except:
        await interaction.followup.send("Formato inválido!")
        return

    await asyncio.sleep(segundos)
    await target_channel.send(mensagem)

@bot.tree.command(name="avatar", description="⌈ Staff ⌋ Mostra o avatar de um usuário.")
async def avatar_command(
    interaction: discord.Interaction, 
    membro: discord.Member = None
):
    target_user = membro or interaction.user
    avatar_url = target_user.display_avatar.url
    
    embed = discord.Embed(
        title=f"Avatar de **{target_user.display_name}**",
        color=discord.Color.blue()
    )
    
    embed.set_image(url=avatar_url)
    embed.set_footer(text=f"Solicitado por: {interaction.user.name}")
    
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="loja", description="⌈ Informação ⌋ Mostra itens da Loja")
async def loja(interaction: discord.Interaction):
    await interaction.response.send_message(
        "- Bots do Discord" \
        "- WallPapers" \
        "- Stickers" \
        "- Templates" \
        "- Artes digitais" \
        "- Sites"
    )

bot.run(TOKEN)
