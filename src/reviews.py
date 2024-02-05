import requests

class CollectReview:
    @staticmethod
    def hooksend(webhookurl, custid, custreview, custcontact):
        """Send review information to a webhook."""
        print("This review system is made by: https://github.com/kshvsec")

        try:
            r = requests.post(webhookurl, json={"content": f"Review from: {custid}\nContact: {custcontact}\nReview: {custreview}"})
            print(f"[DEBUG]: {r.status_code}")
        except requests.RequestException as e:
            print(f"Error sending review to webhook: {e}")

    @staticmethod
    def botsend(token, chnlid: int , custid, custreview, custcontact):
        """Send review information to a Discord bot."""
        print("This review system is made by: https://github.com/kshvsec")

        try:
            headers = {"Authorization": f"Bot {token}"}
            message_url = f"https://discord.com/api/v9/channels/{chnlid}/messages"
            r = requests.post(message_url, headers=headers, json={"content": f"Review from: {custid}\nContact: {custcontact}\nReview: {custreview}"})
            print(f"[DEBUG]: {r.status_code}")
        except requests.RequestException as e:
            print(f"Error sending review to Discord bot: {e}")
