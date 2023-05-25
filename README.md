
# Hell Let Loose (HLL) Discord bot  

An discord bot that use the extended RCON tool for Hell Let loose, to show server status.

## Prerequisites
Be administrator on an existing Discord or create one.

Create a new application on https://discord.com/developers/applications
Create a new Bot for this application and keep the bot token for configuration.
**Note:** The bot must have the "MESSAGE CONTENT INTENT" option checked. 

Generate a OAuth2 URL to deploy the bot, go to OAuth2/URL Generator, select "bot" and copy the generated URL.
Add the bot to your Discord by logging in and choosing the target server at the generated URL. 

## Run on a server
### Prerequisites
The target server must have following software installed: 
* GIT (https://git-scm.com/download/linux)
* Docker engine (https://docs.docker.com/engine/install/)

### Configuration
Checkout the project and configure ```.env``` file with expected data.
```sh
# Discord expected guild ID
GUILD_ID="<Discord guild's ID to use>"
# List of discord's roles allowed to command the bot (.start, .stop, .restart) delimited by ","
# Can be retrieved on discord by typing "\@<Role>" in a chat, the expected format is "<@&[0-9]+>"
ALLOWED_ROLES="<list of allowed roles>"

# BOT_1 CONFIGURATION
# Discord bot application token
BOT_TOKEN_1="<Bot token tu use (dedicated to each HLL server)>"
# Name of the channel to create on discord
CHANNEL_NAME_1="<Channel name, ie. server-1>"
# CRCON API URL format: <ip>:<port>, ie.: 127.0.0.1:8010
HLL_RCON_HOST_1="<CRCON API URL, ie. 127.0.0.1:8010>"

# BOT_2 CONFIGURATION
# Discord bot application token
BOT_TOKEN_2="<Bot token tu use (dedicated to each HLL server)>"
# Name of the channel to create on discord
CHANNEL_NAME_2="<Channel name, ie. server-2>"
# CRCON API URL format: <ip>:<port>, ie.: 127.0.0.1:8010
HLL_RCON_HOST_2="<CRCON API URL, ie. 127.0.0.1:8010>"
```

### Build & Run
Run following commands to build and run the bots with Docker compose. 
```
docker-compose build
docker-compose up --force-recreate
```

## Run locally
### Dependencies
```
pip3 install -r requirements.txt
```

### Configuration
Create a local configuration file named ```.env.local``` at project root.
Content for direct execution (without Docker):
```shell
# Discord expected guild ID
GUILD_ID="<Discord guild's ID to use>"
# List of discord's roles allowed to command the bot (.start, .stop, .restart) delimited by ","
# Can be retrieved on discord by typing "\@<Role>" in a chat, the expected format is "<@&[0-9]+>"
ALLOWED_ROLES="<list of allowed roles>"

# Discord bot application token
BOT_TOKEN="<Bot token tu use>"
# Name of the channel to create on discord
CHANNEL_NAME="<Channel name, ie. server-1>"
# CRCON API URL format: <ip>:<port>, ie.: 127.0.0.1:8010
HLL_RCON_HOST="<CRCON API URL, ie. 127.0.0.1:8010>"
```

### Run
Run the following command to start the bot. It can be stopped by interrupting it with CTRL+C.
```sh
python3 discord_bot/bot.py
```

## Run locally with Docker
You must have Docker Desktop (https://docs.docker.com/desktop/install/windows-install/) installed to proceed.

### Configuration
Create a local configuration file named ```.env.docker``` at project root.
Content for Docker execution with multiple HLL server:
```sh
# Discord expected guild ID
GUILD_ID="<Discord guild's ID to use>"
# List of discord's roles allowed to command the bot (.start, .stop, .restart) delimited by ","
# Can be retrieved on discord by typing "\@<Role>" in a chat, the expected format is "<@&[0-9]+>"
ALLOWED_ROLES="<list of allowed roles>"

# BOT_1 CONFIGURATION
# Discord bot application token
BOT_TOKEN_1="<Bot token tu use (dedicated to each HLL server)>"
# Name of the channel to create on discord
CHANNEL_NAME_1="<Channel name, ie. server-1>"
# CRCON API URL format: <ip>:<port>, ie.: 127.0.0.1:8010
HLL_RCON_HOST_1="<CRCON API URL, ie. 127.0.0.1:8010>"

# BOT_2 CONFIGURATION
# Discord bot application token
BOT_TOKEN_2="<Bot token tu use (dedicated to each HLL server)>"
# Name of the channel to create on discord
CHANNEL_NAME_2="<Channel name, ie. server-2>"
# CRCON API URL format: <ip>:<port>, ie.: 127.0.0.1:8010
HLL_RCON_HOST_2="<CRCON API URL, ie. 127.0.0.1:8010>"
```

### Build & Run
Run following commands to build and run the bots with Docker compose. 
```
docker-compose build
docker-compose --env-file .env.docker up --force-recreate
```

## Run the Discord Bot (obsolete)
Your Discord bot stops running when you exit the SSH session. To keep the bot running full-time, use Tmux or PM2.

### Option 1: Run the Bot with Tmux
Follow this guide to install Tmux.
Create a tmux session.

tmux new -s DiscordBot
Change to the Discord bot project directory.

cd ~/discord-bot 
Start the bot.

python3 discord_bot.py
To stop the Discord Bot, press CTRL + C

### Option 2: Run the Bot with PM2
PM2 is a process manager for Python.

#### Prerequisites

Install npm.
```apt install npm -y```

Install PM2.
```npm install -g pm2```

Change to the Discord bot project directory.


#### Start the bot

In the repository directory, run the following command:
```pm2 start discord_bot/bot.py --interpreter=/usr/bin/python3```

#### Get bot logs

```pm2 logs bot```


#### Common PM2 Commands
Make sure you are in the repository directory, then use these commands to control your bot.

List all PM2 processes:
```pm2 list```

Stop the Discord bot:
```pm2 stop bot```

Restart the Discord bot:
```pm2 restart bot```
