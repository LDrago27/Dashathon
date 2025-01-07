from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def fetch_channel_messages(token, channel_id):
    """
    Fetch all messages from a Slack channel.

    Args:
        token (str): Slack API token.
        channel_id (str): The ID of the Slack channel.

    Returns:
        list: A list of messages from the channel.
    """
    client = WebClient(token=token)
    messages = []
    has_more = True
    next_cursor = None

    try:
        while has_more:
            response = client.conversations_history(
                channel=channel_id,
                cursor=next_cursor
            )

            messages.extend(response['messages'])
            has_more = response['has_more']
            next_cursor = response.get('response_metadata', {}).get('next_cursor')

    except SlackApiError as e:
        print(f"Error fetching messages: {e.response['error']}")

    return messages

if __name__ == "__main__":
    # Replace with your Slack API token and channel ID
    #SLACK_API_TOKEN = ""
    #CHANNEL_ID = ""

    all_messages = fetch_channel_messages(SLACK_API_TOKEN, CHANNEL_ID)

    print(f"Fetched {len(all_messages)} messages.")

    # Save messages to a text file
    output_file = "slack_messages.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        for message in all_messages:
            file.write(f"{message}\n")

    print(f"Messages saved to {output_file}.")
