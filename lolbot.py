#Responsible for running the bot.

import requests
import discord
import logger
import config
from modules.lolrank import LOLRank
client = discord.Client()

@client.async_event
async def on_message(message):
    #author = message.author
    if message.content.startswith('$exit'):
        client.logout()
        print('Bot has logged out')
    if message.content.startswith('$rank'):
        summoner_name = message.content[6:]
        
        try:
            rank = LOLRank(summoner_name)
            await rank.get_ranked_data()

            await client.send_message(message.channel, rank.summoner + '\n-------------\nTier: ' + rank.tier + '\nDivison: '
                                    + rank.division + '\nLP: ' + rank.lp + '\nWins: ' + rank.wins + '\nLosses: ' + rank.losses + '\n\n')
            
        except KeyError:
            await client.send_message(message.channel, 'ERROR! No ranked stats found for this player')
            
#if you want to use email and password, enable below and disable client.run(config.token)
#client.run(config.email, config.password)
client.run(config.token)
