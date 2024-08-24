# Soundboard Bot

This is a soundboard bot I initially made before discord pushed their changes to add sound boards in Discord as an actual feature. This is made using `Python` with `Nextcord` and for the "backend" ~~for now~~ is using `pickledb`.

### Available Features or Commands:
```
- adds - <Admin only command> adds a star if the bot missed a clockin commands
- attendance - displays the attendance and how much stars the server member has attained
- clockin - logs the user as present for a day which adds 1 to his total attendance
- help - shows the available commands
- join - commands the bot to join the voice call (if there are present members)
- leave - commands the bot to leave the voice call (if the bot is currently in a voice call)
- pause - pauses the currently playing sound
- play - plays a sound availble in playlist
- playlist - displays the available sounds the bot can play
- resume - resumes a currently paused sound
- shutdown - the bot shutsdown
- stars - shows the stars leaderboard and displays how many stars each member has attained
- stop - stops the sound the bot is currently playing
```