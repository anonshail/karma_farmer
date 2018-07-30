import praw

def init_bot():
	"this function is used to initialise a reddit instnace"

	reddit = praw.Reddit(client_id='SHmCzYYbti2q9Q',
                     client_secret='m38NwYit68-1_Uu7ou2nU3nfe9k',
                     password='thisisapassword',
                     user_agent='karma_farmer by /u/kurithesheep',
                     username='SpiritualPrinciple0')

	return reddit

def build_dict():
	"function to form the subreddit dictionary after reading subreddit_list.txt"
	subreddit_dict=dict();

	#reading form the file and forming the dict
	with open("subreddit_list.txt") as raw_data:
		for item in raw_data:
			if ':' in item:	#checking if line is normal or not
				key, value = item.split(':', 1)
				subreddit_dict[key] = value.rstrip()	#removing the trailing newline
			else:	#skipping junk lines
				pass

	return subreddit_dict


#the main scrip starts here
reddit = init_bot()				#obtaining a reddit insance here
subreddit_list = build_dict()	#obtaining the subreddit dictionary