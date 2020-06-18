# commands
client.remove_command("help")


## There was a space between @ and client on the next line
@client.command()
async def commands(ctx):
  author = ctx.message.author
  embed = discord.Embed(
    colour = discord.Colour.red()
  )
  # title embed here saying Commands
  embed.set_author(name='Commands')
  embed.add_field(name= '.ping', value= 'Sends back pong , have fun laying table tennis uwu!', inline=False)
  embed.add_field(name= '.Godie', value= 'to let ur anger out ;)', inline=False)
  embed.add_field(name= '.avatar @mention', value= 'shows the avatar of the person you have mentioned', inline=False)
  embed.add_field(name= '.topic shrimp', value= 'gives you a random question to start ur conversation or just answer!', inline=False)
  embed.add_field(name= '.kick', value= """this kicks members from your server, you can type a reason next to .kick @mention [reason].
  
  Warning: this command only works if Shrimp_bot has permissions to kick and ban and you yourself do as well! """, inline=False)
  embed.add_field(name= '.ban', value= """this bans members from your server, you can type a reason next to .ban @mention [reason].
  
  Warning: this command only works if Shrimp_bot has permissions to kick and ban and you yourself do as well! """, inline=False)

  await ctx.send(embed=embed)
