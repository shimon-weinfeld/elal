import sys
from twilio.rest import Client

phone_number = '+972587100770'

account_sid = 'ACbafdc5e94e04e9fc1d0f11833a5f97a9'
auth_token = '74972df6fa2b4701890e687bf4c9e621'
client = Client(account_sid, auth_token)


def send_message(message):
    client.messages.create(
      from_='+19894738434',
      body=message,
      to=phone_number
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <MESSAGE>")
        sys.exit(0)

    send_message(sys.argv[1])
