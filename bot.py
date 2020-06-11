import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

import datetime

import config

from modules import db

conn = db.DBConnection('./db')

# Delete default help command
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
	print('Running as {} {}'.format(bot.user.name, bot.user.id))

# Help message.. Send a PM to the user that requests help
@bot.command(description = "Send a help message")
async def help(ctx):
	embed = discord.Embed(title = "Help", description = "Help message (all commands start with a !, e.g. !getshows)", color = discord.Color.from_rgb(255, 50, 50))
	for command in bot.commands:
		embed.add_field(name = command.name, value = command.description, inline = False)
	await ctx.author.send(embed = embed)

@bot.command(description = "Create a show and save it in the database")
async def createshow(ctx, *args):
	if len(args) < 3:
		return await ctx.author.send("Invalid syntax, usage: !createshow <name> <description> <date>")

	name = args[0]
	desc = args[1]
	date = args[2]
	query = "INSERT INTO shows (`name`, `description`, `date`) VALUES ('{}', '{}', '{}')".format(name, desc, date)
	lastrowid = conn.insert(query)
	query = "SELECT * FROM shows WHERE id = {}".format(lastrowid)
	result = conn.selectall(query)
	embed = discord.Embed(title = "{} - {}".format(name, date), description = desc, color = discord.Color.from_rgb(100, 255, 100))
	await ctx.send(embed = embed)


@bot.command(description = "Retreive all the upcoming shows from the database and send them over to the user")
async def getshows(ctx):
	query = "SELECT * FROM SHOWS"
	result = conn.selectall(query)
	embed = discord.Embed(title = "Shows", description = "All the upcoming shows", color = discord.Color.from_rgb(150, 50, 150))
	for show in result:
		date = [int(x) for x in show[3].split('-')]
		dtime = datetime.datetime(date[2], date[1], date[0])
		if dtime >= datetime.datetime.now():
			embed.add_field(name = "{} - {}".format(show[1], show[3]), value = show[2], inline = False)
	await ctx.send(embed = embed)

@bot.command(description = "Shut the server down")
async def shutdown(ctx):
	conn.close()
	await ctx.send(":robot: Shutting down")
	await bot.logout()


bot.run(config.bot_token)
