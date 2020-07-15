import discord
import random
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    game = discord.Game("마법 연습")
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event

async def on_message(message):
    answer = ["네?", "네 주인님", "하이!", "응응"]
    answer2 = ["마법 연습하고 있어!", "팩이랑 놀고 있어", "잘라구 했어", "밥 먹을려구"]
    answer3 = ["응! 좋아", "네 주인님", "응 이리와!", "시러"]
    answer4 = ["응! 좋아", "네 주인님", "착하지", "시러"]
    channel = message.channel
    if message.author.id == 345782367719522322:
        if message.content == "에밀리아":
            await message.channel.send(random.choice(answer))
        if message.content.startswith("뭐해?"):
            await message.channel.send(random.choice(answer2))
        if message.content == "나도 같이 놀자":
            await message.channel.send(random.choice(answer3))
        if message.content == "나 안아줘":
            await message.channel.send(random.choice(answer4))
        if message.content == "사랑해":
            await message.channel.send("나도 사랑해..!")
client.run("NzMyNjcwMjQzMTU5NDA4NzEw.Xw4CLA.RKLGo05D_iNEoS6KpSJRYRPpbZo")