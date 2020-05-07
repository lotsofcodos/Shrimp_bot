# imports
import random, os

from discord.ext import commands
from discord.ext.commands import Bot

from dummy_web import keep_alive

#import youtube_dl
#import topic_questions.py

bot_token = os.getenv("TOKEN")
client = commands.Bot(command_prefix = '.')

# events
@client.event
async def on_ready():
    print("bot is ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

# commands

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')
@client.command()
async def Godie(ctx):
    await ctx.send('oki ):')
#@client.command()
#async def topic(ctx):
#    await ctx.send

#@client.command()
#async def Hangman(ctx):
    
@client.command()
async def topic(ctx,*,question):
    question = ['What is lying in your fridge at the moment?',
                    'Would you prefer fries or ceaser salad right now?',
                    'How often do you eat salad as a full meal?',
                    'If you had 30 secs of everyone’s attention, what is the one thing you will say?',
                    'What would you do to quickly get someone’s attention?',
                    'I am a person who thinks a lot, what about you?',
                    'If you had 30 secs of everyone’s attention, what is the one thing you will say?',
                    'What would you do to quickly get someone’s attention?',
                    'I am a person who thinks a lot, what about you?',
                    'If you had 30 secs of everyone’s attention, what is the one thing you will say?',
                    'What would you do to quickly get someone’s attention?',
                    'I am a person who thinks a lot, what about you?',
                    'What is your wildest fantasy?',
                    'Do you ever hit nostalgia and if yes, how do you feel?',
                    'Which is the one superpower you wish you had?',
                    'Did you always want to be in the profession you are in?',
                    'Which is the biggest fear of your life?',
                    'Is there anything you would try that you never tried before?',
                    'Have you ever planned a conspiracy to stalk someone?',
                    'Would you rather chose to be alone and alive or with a group of people and die?',
                    'Have you ever been chased by police?',
                    'Why are you acting weird for the past few days?',
                    'I heard you have a big secret to tell your partner, is that true?',
                    'What will you prefer? To be buried or cremated?',
                    'Which one do you want to know- When will you die or how will you die?',
                    'What is the weather like?',
                    'Watch Star Wars or Star Trek? Harry Potter or The Lord of the Rings? Use whichever movies you find most relevant.',
                    'Read on a Kindle or paperback book? This question is a starter for many possible conversations on reading, favorite books, technology, libraries, bookstores and more!',
                    'Go to a play or musical?',
                    'Go to the theater or a movie?',
                    'Wear jeans or chinos?',
                    'Have a Margarita or Pina Colada?',
                    'Drink a glass of Guinness or Fat Tire?',
                    'Drink coffee or beer?',
                    'Crash with friends or stay in a hotel?',
                    'Visit Europe or Mexico?',
                    'Vacation in Hawaii or Alaska, and why?',
                    'Choose a free trip or money? This may tell you whether the person values experiences over dollars.',
                    'Stay in a hotel or an Airbnb home?',
                    'Go skiing or snowboading?',
                    'Travel by plane, train, or automobile?',
                    'Enjoy a houseboat or speed boat?',
                    'Go climbing or zip lining?',
                    'Hike or bike?',
                    'Go to a comedy club or dance club?',
                    'Have a night out or evening in?',
                    'Watch TV or read a book?',
                    'Go canoeing or waterskiing?',
                    'Camp in an RV or stay in a tent?',
                    'Use Facebook or Twitter?',
                    'Use iPhone or Android phone?'
                    'Win the lottery or find your perfect job?',
                    'Swim in a pool or the ocean? Salt water and waves crashing on the beach or temperature controlled, lovely water all year round.',
                    'Travel by sailboat or cruise ship?',
                    'Watch sports or play sports?',
                    'Play dodgeball or kickball?',]           
    await ctx.send(f'Question: {random.choice(question)}')
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context =True)
async def purge(ctx,amount=10):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from.channel, limit==int(amount):
        messages.append(message)
    await client.delete_messages(messages)

class Survey(object):
    survey_questions = ['What is your name?',
                       'What is your age?',
                       'Where do you live?',]
    def __init__(self):
        self.question_number = 0
        self.survey_in_progress = False
        self.user = None

    def next_question(self):
        question_to_ask = self.survey_questions[self.question_number]
        self.question_number = self.question_number + 1
        if self.question_number > 2:
            self.question_number = 0
            self.survey_in_progress = False
        return question_to_ask

    def start_survey(self, user_who_started_survey):
        if not self.survey_in_progress:
            self.user = user_who_started_survey
            self.survey_in_progress = True
            print(f'{user_who_started_survey} started a survey')
    
bot_survey_memory = Survey()    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'message from {message.author} who said {message.content} ')
    # process message to see if the author has a survey running

    
    if bot_survey_memory.user is not None and bot_survey_memory.user == message.author:
        await message.channel.send(f'Your answer is: {message.content}')
        await message.channel.send(bot_survey_memory.next_question())
    await client.process_commands(message)


@client.command()
async def survey(ctx):
    bot_survey_memory.start_survey(ctx.message.author)
    await ctx.send(bot_survey_memory.next_question())
    await ctx.send('Use the command: .answer to send back your answer.')

@client.command()
async def answer(ctx,user_answer):
    await ctx.send(f'You answer is: {user_answer}')
    await ctx.send(bot_survey_memory.next_question())




keep_alive()
client.run(bot_token)
 