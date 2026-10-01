import discord
import json

with open("lxc_settings.json", "r") as f:
    lxccfg = json.load(f)


token = " "

async def identifydesktop(self):
    payload = {
        "op": self.IDENTIFY,
        "d": {
            "token": self.token,
            "capabilities": 4093,
            "properties": {
                "os": "Windows",
                "browser": "Discord Client",
                "device": "Desktop",
                "system_locale": "en-US",
                "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
                "browser_version": "147.0.0.0",
                "os_version": "10",
                "referrer": "",
                "referring_domain": ""
            },
            "compress": False,
            "client_state": {
                "guild_versions": {},
                "highest_last_message_id": "0",
                "read_state_version": 0,
                "user_guild_settings_version": -1,
                "user_settings_version": -1,
                "private_channels_version": "0",
                "api_code_version": 0
            }
        }
    }
    await self.send_as_json(payload)


async def identifymobile(self):
    payload = {
        "op": self.IDENTIFY,
        "d": {
            "token": self.token,
            "capabilities": 4093,
            "properties": {
                "os": "iOS",
                "browser": "Discord iOS",
                "device": "iPhone",
                "system_locale": "en-US",
                "browser_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/605.1.15",
                "browser_version": "17.5",
                "os_version": "17.5",
                "referrer": "",
                "referring_domain": ""
            },
            "compress": False,
            "client_state": {
                "guild_versions": {},
                "highest_last_message_id": "0",
                "read_state_version": 0,
                "user_guild_settings_version": -1,
                "user_settings_version": -1,
                "private_channels_version": "0",
                "api_code_version": 0
            }
        }
    }
    await self.send_as_json(payload)


async def identify(self):
    device = str(lxccfg.get("device_indicator", "desktop")).lower()

    if device == "mobile":
        return await identifymobile(self)
    elif device == "desktop":
        return await identifyvr(self)

    return await identifydesktop(self)


discord.gateway.DiscordWebSocket.identify = identify


lxc = discord.Client()


lxc.run(token)
