from datetime import datetime, timedelta

from click import group, argument
from slack_bolt.adapter.socket_mode import SocketModeHandler

from .sleepy import make_client, create_app, handle_mention
from .config import config


@group()
def cli():
    pass


@cli.command()
@argument("text")
@argument("secs", type=int)
def schedule_message(text, secs):
    client = make_client(config.SLACK_USER_TOKEN)
    r = client.chat_scheduleMessage(
        channel=config.SLACK_CHANNEL_ID,
        text=text,
        post_at=round((datetime.now() + timedelta(seconds=secs)).timestamp())
    )
    print(r.data)


@cli.command()
def list_scheduled_messages():
    client = make_client(config.SLACK_USER_TOKEN)
    r = client.chat_scheduledMessages_list(
        channel=config.SLACK_CHANNEL_ID,
    )
    print(r.data)


@cli.command()
def start_handler():
    app = create_app(config.SLACK_BOT_TOKEN)
    client = make_client(config.SLACK_USER_TOKEN)
    app.event("app_mention")(handle_mention(client, config.SLACK_CHANNEL_ID))
    handler = SocketModeHandler(app, app_token=config.SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    cli()
