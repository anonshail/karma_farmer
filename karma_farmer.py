import praw

def init_subreddit():
	"this function is used to initialise a reddit instnace"

	reddit = praw.Reddit(client_id='SHmCzYYbti2q9Q',
                     client_secret='m38NwYit68-1_Uu7ou2nU3nfe9k',
                     password='thisisapassword',
                     user_agent='karma_farmer by /u/kurithesheep',
                     username='SpiritualPrinciple0')

	print(reddit)