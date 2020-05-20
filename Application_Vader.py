import discord
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator

# create discord client, sentiment analyzer and google translater object
client = discord.Client()
analyzer = SentimentIntensityAnalyzer()
translator = Translator()


def sentiment_analyzer_scores(text):
    trans = translator.translate(text).text
    score = analyzer.polarity_scores(trans)
    lb = score['compound']
    
    print('_________________________SENTIMENT__________________________')
    print(text)
    print("score =", lb)

    if (lb >= 0.05) and (lb < 0.4) :
        return 'est content'
    elif (lb >= 0.4) and (lb < 0.8):
        return 'est trés content'
    if (lb >= 0.8) and (lb <= 1):
        return 'est trés trés content'
    elif (lb > -0.05) and (lb < 0.05):
        return 'a un sentiment neutre'
    elif (lb > -0.4) and (lb <= -0.05):
        return ' est me content'
    elif (lb > -0.8) and (lb <= -0.4):
        return 'est tres me content'
    elif (lb >= -1) and (lb < -0.8):
        return 'est tres tres me content'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    sentiment = sentiment_analyzer_scores(message.content)
    print('sentiment: ' + str(sentiment))
    await message.channel.send('Le client   ' + str(sentiment))
# run our bot
client.run('Insert your ID')
