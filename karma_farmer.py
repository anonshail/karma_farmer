import praw

def init_bot():
	"this function is used to initialise a reddit instnace"

	reddit = praw.Reddit(client_id='SHmCzYYbti2q9Q',
                     client_secret='m38NwYit68-1_Uu7ou2nU3nfe9k',
                     password='thisisapassword',
                     user_agent='karma_farmer by /u/kurithesheep',
                     username='SpiritualPrinciple0')

	return reddit


#the main scrip starts here
reddit = init_bot()		#obtaining a reddit insance here

