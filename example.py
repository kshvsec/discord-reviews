from src.reviews import CollectReview

# PRESET THESE VALUES
token = "YOUR DISCORD BOT TOKEN"
channelid = 0000 # review channel id
webhookurl = "YOUR WEBHOOK URL"

# INPUT THE PARAMETERS
CollectReview.hooksend(webhookurl, "Mary", "I love this product!", "mymail@mail.com")
CollectReview.botsend(token, channelid, "Mary", "I love this product!", "mymail@mail.com")