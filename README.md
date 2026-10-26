# Soundboard Bot

This is a soundboard bot I initially made before discord pushed their changes to add sound boards in Discord as an actual feature. This was made using `Python` with `Nextcord` and is using `MongoDB` as its' database.

### Available Features or Commands:
```
Attendance:
  - adds: Adds a star to the mentioned user 
  - attendance: Shows the user's number of stars and accolades 
  - clockin: Clock in for the day 
  - stars: Shows the list of stars of users 
Birthday:
  - mybirthday: Shows the user's currently saved birthday and age
  - setbirthday: Saves the user's birthday
  - setbirthdayfor: Sets a birthday for a specific user
Reply:
  - coinflip: Sends a random choice between 'Heads' and 'Tails' 
  - doesntwork: Doesn't work? Don't blame Johann :^) 
  - namer: Sends a random name from the name_generator list 
  - wotd: Sends a random word from the n_words list 
SecretSanta:
  - joinsanta: Adds the user to the Secret Santa pool 
  - leavesanta: Removes the user from the pool
  - poolsanta: Lists current participants 
  - resetsanta: Reset secret santa pool 
  - startsanta: Randomly assigns each participant to someone
Voice:
  - join: Bot joins the user's current voice channel 
  - leave: Bot leaves the current voice channel 
  - pause: Bot pauses the current audio playback 
  - play: Bot plays songs from playlist 
  - playlist: Shows soundboard playlist as clickable buttons 
  - resume: Bot resumes the current audio playback 
  - stop: Bot stops the current audio playback 
Weather:
  - weather: Fetches current weather for a given city using wttr.in 
​General:
  - help: Shows this message
  - shutdown: Shuts down the bot. Only the owner can use this command. 

Type !help command for more info on a command.
You can also type !help category for more info on a category.
```
