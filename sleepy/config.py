import os

class Config:
    SLACK_APP_TOKEN = os.environ["SLACK_APP_TOKEN"]
    SLACK_USER_TOKEN = os.environ["SLACK_USER_TOKEN"]
    SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
    SLACK_CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]
    SLACK_COMMAND_CHANNEL_ID = os.environ["SLACK_COMMAND_CHANNEL_ID"]


config = Config()
