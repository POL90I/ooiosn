import discord
import random
from PIL import Image

bot = discord.Client()

ideas = [
    ("Подставки для ручек и карандашей из бутылок", "https://example.com/bottle-pen-holders.jpg"),
    ("Кашпо для растений из пластиковых контейнеров", "https://example.com/plastic-container-planters.jpg"),
    ("Кормушки для птиц из пластиковых бутылок", "https://example.com/plastic-bottle-bird-feeders.jpg"),
    ("Игрушки для домашних животных из пластиковых крышек", "https://example.com/plastic-lid-pet-toys.jpg"),
    ("Органайзеры для ящиков из пластиковых контейнеров", "https://example.com/plastic-container-drawer-organizers.jpg"),
    ("Украшения для дома из пластиковых бутылок", "https://example.com/plastic-bottle-home-decor.jpg"),
    ("Рамки для картин из пластиковых крышек", "https://example.com/plastic-lid-picture-frames.jpg"),
    ("Вазы для цветов из пластиковых бутылок", "https://example.com/plastic-bottle-vases.jpg"),
    ("Светильники из пластиковых бутылок", "https://example.com/plastic-bottle-lamps.jpg"),
    ("Бижутерия из пластиковых крышек", "https://example.com/plastic-lid-jewelry.jpg"),
]

@bot.event
async def on_message(message):
    if message.content == "!поделка":
        idea, image_url = random.choice(ideas)
        await message.channel.send(f"Вот идея для поделки из бытового пластика: {idea}")
        await message.channel.send(image_url)

bot.run("MTIxMTI5MDYzMzgwMTY5NTI1Mg.GFKDXr.OIo8T4TFUsc0BMndZnY1zt3fKhwJSz1W269Uy0")
