import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".L ", intents=intents)

mascotas = {
    "dog": {
        "nombre": "Dog",
        "MFR": ("0.009", "★☆☆"),
        "NFR": ("0.006", "★☆☆"),
        "FR": ("0.003", "★☆☆")
    }
}

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def L(ctx, mascota=None):

    if mascota is None:
        await ctx.send("❌ Escribe una mascota. Ejemplo: `.L dog`")
        return

    mascota = mascota.lower()

    if mascota not in mascotas:
        await ctx.send("❌ No encuentro esa mascota.")
        return

    datos = mascotas[mascota]

    mensaje = (
        f"**{datos['nombre']}**\n\n"
        f"**MFR**\n"
        f"{datos['MFR'][0]}\n"
        f"{datos['MFR'][1]}\n\n"
        f"**NFR**\n"
        f"{datos['NFR'][0]}\n"
        f"{datos['NFR'][1]}\n\n"
        f"**FR**\n"
        f"{datos['FR'][0]}\n"
        f"{datos['FR'][1]}"
    )

    await ctx.send(mensaje)

bot.run(os.getenv("DISCORD_TOKEN"))
