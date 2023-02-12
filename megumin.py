import hikari
import lightbulb
import random
from randomlolixd import random_photo

#https://github.com/hikari-py/hikari
#https://github.com/tandemdude/hikari-lightbulb


#MEGUMIN BOT
#@wiolex XDDDD mf gave himself a shoutout aint no way bruhhvv XDDDD

bot= lightbulb.BotApp(token='###########################################')


@bot.command
@lightbulb.command('pero','Jak dlouhy mas pero')
@lightbulb.implements(lightbulb.SlashCommand)
async def print_message(ctx):
            random_number = random.randint(1, 100)
            await ctx.respond(f"Tvoje pero ma {random_number} cm")


@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')

@bot.command
@lightbulb.command('cunny','CUNNY')
@lightbulb.implements(lightbulb.SlashCommand)
async def cunny(ctx):
    await ctx.respond('UOOOOOOOOOGH')


@bot.command
@lightbulb.command('loli', 'WE LOVE THEM YOUNG :3')
@lightbulb.implements(lightbulb.SlashCommand)
async def imgsnd(ctx):
    loli = random_photo()
    print(loli)
    with open(loli, "rb") as fh:
        f = hikari.File(loli)
    await ctx.respond(f)


bot.run()