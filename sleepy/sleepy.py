import logging

from slack_bolt import App
from slack_sdk.web import WebClient


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def make_client(token):
    return WebClient(token=token, logger=logger)


def create_app(token):
    return App(token=token, logger=logger)


def cancel_scheduled_messages(client, channel):
    scheduled_messages_resp = client.chat_scheduledMessages_list(
        channel=channel,
    )
    for scheduled_message in scheduled_messages_resp.data["scheduled_messages"]:
        logger.info(scheduled_message)
        client.chat_deleteScheduledMessage(
            channel=channel,
            scheduled_message_id=scheduled_message["id"],
        )


def handle_mention(client, channel):
    def wrapper(body, say):
        if "cancel" in body["event"]["text"]:
            cancel_scheduled_messages(client, channel)

    return wrapper
