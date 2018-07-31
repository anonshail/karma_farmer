import os
import json
import urllib.request
import time
list_of_subs=dict()
#Replace the below line with the actual path of the file "loop_through_these_subs.txt"
path="/home/vishal/Python_Programming/"#Replace with your own path
os.chdir(path)
f=open("loop_through_these_subs.txt","r")#From a file containing subs to rip from
for line in f:
	line=line.rstrip('\n')
	list_of_subs[line]=[]#store subreddits to extract details from in the dictionary
#print(list_of_subs)
f.close()
request_urls=[]
generic_url="https://old.reddit.com/r/"#old>new  btw
for key in list_of_subs.keys():
	key=generic_url+key+"/.json"#obtain the json page of the url
	request_urls.append(key)#store keys(subreddits) in a list. probably change this later
#print(request_urls)
for url in request_urls:
	while(1):
		try:
			data=urllib.request.urlopen(url)
			break
		except:
			print("429. Trying again in 3 seconds")
			time.sleep(3)
	response=data.read()
	response=json.loads(response)
	#Reference json link as follows
	count=0#to loop through the json content
	for i in response['data']['children'][count]['data']:
		try:
			#Need to streamline the below lines. FeelsWeirdMan
			subreddit=response['data']['children'][count]['data']['subreddit']
			#print(subreddit)
			title=response['data']['children'][count]['data']['title']
			link_url=response['data']['children'][count]['data']['url']
			number_of_comments=response['data']['children'][count]['data']['num_comments']
			author_of_post=response['data']['children'][count]['data']['author']
			selftext=response['data']['children'][count]['data']['selftext']
			list_of_subs[subreddit]+=[[title,link_url,number_of_comments,author_of_post,selftext]]
			count+=1
		except:#Find out the reason behind list index going out of range
			#print("list index out of range")
			pass
#print(list_of_subs)
for key in list_of_subs:
	f=open("Data_from_subs.txt","a")
	f.write(key)
	for value in list_of_subs[key]:
		f.write("%s\n" % value)#need to fix this with regards to stripping the \n and improving the formatting and such
	f.close()#probably better to close after all iterations. Haven't fully read the theory behind it