import praw

bot = praw.Reddit(user_agent = 'DogYearsBot v0.1',
                  client_id = 'jfctVhoZe3cI4g',
                  client_secret = 'GgWxcDWVIQkAaUuBPptwhq2k0wQ',
                  username = 'DogYearsBot',
                  password = 'iamabotmadebyjack')

subreddit = bot.subreddit('test')
comments = subreddit.stream.comments()

for comment in comments:
   text = comment.body
   if '%d years' in text.lower():
      message = "For reference, that's %d*7 dog years\nThis is a bot in testing, please ignore."
      comment.reply(message)
