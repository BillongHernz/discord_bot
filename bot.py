# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

# import disc_func
from disc_func.TicTacToe.TicTacToe import TicTacToe, print_board

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


# Global Data
bot.tictactoe = {}


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='real-python'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


@bot.command(name='echo', help='Repeats input as an echo')
async def echo(ctx, *args):
    await ctx.send(f"{ctx.author.display_name}: {' '.join(args)}")


@bot.command(name='tictactoe', help='Plays tic tac toe')
async def tictactoe(ctx, *args):

    # TO DO:
    # enable for two different users to play a game against each other?

    try:

        if ctx.author.id not in bot.tictactoe:
            # await ctx.send("First time")
            bot.tictactoe[ctx.author.id] = TicTacToe()

        if len(args) > 0:
            command = args[0]

            if command.lower() == "board":
                await ctx.send(print_board(bot.tictactoe[ctx.author.id].ret_board()))
            elif command.lower() == "newgame":
                bot.tictactoe[ctx.author.id].new_game()
                await ctx.send(print_board(bot.tictactoe[ctx.author.id].ret_board()))
            elif command.lower() == "move":
                if len(args) == 3 and args[1].isdigit() and args[2].isdigit():
                    bot.tictactoe[ctx.author.id].input_move(int(args[1]), int(args[2]))
                    await ctx.send(print_board(bot.tictactoe[ctx.author.id].ret_board()))
                else:
                    await ctx.send(f"Arguments Error: Incorrect arguments ({' '.join(args)}) for the command: {command}")
            else:
                await ctx.send(f"Invalid command given")
        else:
            await ctx.send(f"No command given for TicTacToe")

        if bot.tictactoe[ctx.author.id].has_winner():
            await ctx.send(f"Congratulations Player {bot.tictactoe[ctx.author.id].last_player()} wins!")
            bot.tictactoe[ctx.author.id].new_game()
            await ctx.send(f"Board has been reset")

        if bot.tictactoe[ctx.author.id].has_tie():
            bot.tictactoe[ctx.author.id].new_game()
            await ctx.send(f"It is a tie and no player wins!")
            await ctx.send(f"Board has been reset")

    except:
        await ctx.send("Failed to run command")

    # curr_board = bot.tictactoe[ctx.author.id].ret_board()
    # printed = print_board(curr_board)

    # await ctx.send(print_board(bot.tictactoe[ctx.author.id].ret_board()))
    # await ctx.send(f"{ctx.author.id}: {' '.join(args)}")



bot.run(TOKEN)
