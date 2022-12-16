import logging
import sys

from slack_bolt import App
from slack_sdk.web import WebClient


logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


ORDER_MESSEAGE = 'Could You Please Remove My Late Inform Scheduled Message?'


def make_client(token):
    return WebClient(token=token, logger=logger)


def create_app(token):
    return App(token=token, logger=logger)


def cancel_scheduled_messages(client, channel, body, say):
    scheduled_messages_resp = client.chat_scheduledMessages_list(
        channel=channel,
    )
    try:
        for scheduled_message in scheduled_messages_resp.data["scheduled_messages"]:
            logger.info(scheduled_message)
            client.chat_deleteScheduledMessage(
                channel=channel,
                scheduled_message_id=scheduled_message["id"],
            )
        say("Done!")
        client.chat_delete(channel=body["event"]["channel"], ts=body["event"]["ts"])
    except Exception as e:
        say(str(e))


def handle_mention(client, channel):
    def wrapper(body, say):
        logger.info(body)
        if ORDER_MESSEAGE in body["event"]["text"]:
            cancel_scheduled_messages(client, channel, body, say)
        else:
            say("I don't understand.")

    return wrapper
