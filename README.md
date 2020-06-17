# Session Bot

Discord bot that announces upcoming sessions on the Additional Fun & Educational Events calendar!

Inspired by the [Hack Quarantine](https://hackquarantine.com) [Calendar Bot](https://github.com/HackQuarantine/calendar-bot) used to automatically make announcements from their calendar. 

## Setup

Make sure to set your Google Calendar to the same timezone as the Discord Bot. In this case, it's the timezone of the Compute Engine on Google Cloud.

```
virtualenv .venv
source .venv/bin/activate
cat .example.env > .env
```

_Make sure to fill the `.env` file with the required fields_

## Run

```
python -m bot
```
