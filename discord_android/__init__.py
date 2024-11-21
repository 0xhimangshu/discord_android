import discord.gateway

from .core import DiscordWebSocket


def init():
    discord.gateway.DiscordWebSocket.identify = DiscordWebSocket.identify
