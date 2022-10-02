
# Hell Let Loose (HLL) Discord bot  

An discord bot that use the extended RCON tool for Hell Let loose, to show server status.

# Run the Discord Bot
Your Discord bot stops running when you exit the SSH session. To keep the bot running full-time, use Tmux or PM2.

## Option 1: Run the Bot with Tmux
Follow this guide to install Tmux.
Create a tmux session.

tmux new -s DiscordBot
Change to the Discord bot project directory.

cd ~/discord-bot 
Start the bot.

python3 discord_bot.py
To stop the Discord Bot, press CTRL + C

## Option 2: Run the Bot with PM2
PM2 is a process manager for Python.

Install npm.

apt install npm -y 
Install PM2.

npm install -g pm2
Change to the Discord bot project directory.

cd ~/discord-bot 
Start the bot.

pm2 start discord_bot.py --interpreter=/usr/bin/python3
Common PM2 Commands
Make sure you are in the ~/discord-bot directory, then use these commands to control your bot.

List all PM2 processes:

pm2 list
Stop the Discord bot:

pm2 stop discord_bot.py
Restart the Discord bot:

pm2 restart discord_bot.py
