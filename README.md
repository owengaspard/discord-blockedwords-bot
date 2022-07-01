# Discord.py Blocked Words Bot
This is the template for a bot that blocks any specified words in your Discord server.

<a href="https://www.digitalocean.com/?refcode=1216df23cc7f&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%201.svg" alt="DigitalOcean Referral Badge" /></a>

<a href="https://www.vultr.com/?ref=9172285-8H"><img src="https://www.vultr.com/media/logo_ondark.png?_gl=1*qjtnzw*_ga*MTg4MTcwODE0MS4xNjU2NjM5MDA5*_ga_K6536FHN4D*MTY1NjYzOTAwOS4xLjEuMTY1NjYzOTU4Ni4w" alt="Vultr Referral Badge" /></a>

## Setup the bot
### Windows
1. [Download Python from the website](https://www.python.org/downloads/)
2. Open Windows Terminal or PowerShell
3. Clone the repository and cd into it: `git clone https://github.com/owengaspard/discord.py-blocked-words-bot.git && cd discord.py-blocked-words-bot`
4. Install pyenv: `pip install pyenv'
5. Create a virtual environment (venv) and activate it: `python3 -m venv bot && bot\Scripts\activate.bat`
6. Install Discord.py: `pip install discord.js`
7. Add your token to the `botToken` file
8. Run the bot: `python3 ./main.py`

### macOS/Linux
1. Ether download Python from [here](https://www.python.org/downloads/) or download it using Homebrew: `brew install python3 pip`
2. Clone the repository and cd into it: `git clone https://github.com/owengaspard/discord.py-blocked-words-bot.git && cd discord.py-blocked-words-bot`
3. Install pyenv: `pip install pyenv'
4. Create a virtual environment (venv) and activate it: `python3 -m venv bot && source bot/bin/activate`
5. Install Discord.py: `pip install discord.js`
6. Add your token to the `botToken` file
7. Run the bot: `python3 main.py`

## Adding words to the blocklist
The blocklist is in the `main.py` file. Look for the variable `blockedWords`, and change the words to whatever you desire.

## Basics of Python Arrays
When you add words, put them in quotes ("") and add a comma at the end of it only if you are adding another word under it. Do not add a comma if it is the last word in the list (Python doesn't care, but JSON files do care).
