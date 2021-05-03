import discord
from coincappy import CoinMarketCap
from discord.ext import commands
from discord.ext.commands import command, errors, Cog, cooldown
from discord.ext import tasks

class Crypto(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command(aliases=["slookup", "sl"])
	async def symbollookup(self, ctx, symbol):
		def isstr(var):
			try:
				var = str(var)
				return var, True
			except:
				return False
		
		if isstr(symbol) != True:
			await ctx.send(f"{symbol} is not a valid symbol")
		
		cmc = CoinMarketCap("1a4e566f-aa02-4ffc-a5b0-54f920860500")
		response = cmc.crypto_quotes(symbol=symbol, convert="AUD")
		pass

def setup(bot):
	bot.add_cog(Crypto(bot))