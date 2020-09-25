import tweepy
import random


consumer_key = 'wuB5LswEU7aHC5YwyQhLTFwzY'
consumer_secret= '9HeDelzVHDOrxT3fFTzFqZEvmOhaet8dxCKKDR4L9cVcnBcd1G'
access_token = '1307343241197486084-W6E1ZK0CfomxATmcPqrSrlKfkNu0Oa'
access_token_secret = '7ipfQIoDSuPO2OI5B4giQpL0zVbDtRawWUX0RBwKoLCNb'


#Setting up access to the Twitter API with tweepy
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api =tweepy.API(auth)


# n is a integer that represents the number of twitter handles used in the game
n=int(input("\n Enter the number of twitter handles you would like to play with: "))

#creating, appending, and shuffling the list twitter handles requested by the user
twitter_users = []
for i in range(n):
	twitter_users.append(input("Enter twitter handle #"+ str(i+1)+ ": "))
random.shuffle(twitter_users)

#creating a list with the full statuses of each user's first 3200 tweets
users_status=[]
for i in range(n):
	users_status.append(api.user_timeline(twitter_users[i], count=3200, 
		tweet_mode= "extended",exclude_replies='true', include_rts = 'false'))



#the nested list within all_tweets will contain individual tweets by a certain user
all_tweets = [[] for x in range (n)]
guess= ['' for x in range(n)]
final_correct_counter = []
cont = 'y'


def tweets_in_list(number,user_tweets):	
	'''
	Isolates the text property of a tweet 

	Tweets are filtered to exclude tags (@) and links (http) not 
	already filtered out by the parameters of api.user_timeline
	Given: number = (n-1) used to index into lists, user_tweets 
	= the nested list corresponding to all_tweets[n-1]
	Returns: None
	'''
	for status in users_status[number]:
		if "@" not in status.full_text and "http" not in status.full_text:
			(user_tweets).append(status.full_text)
	return None





def guess_tweet(number, user_tweets,c_counter):
	'''
	Displays a randomly selected Tweet, and evaluates user's guess.

	Calls tweets_in_list then chooses a random tweet from one of all_tweet's 
	nested lists. Evaluates the user's guesses and checks for correctness.
	
	Given: number (int) = (n-1)used to index into lists, user_tweets ()= the nested 
	list corresponding to all_tweets[n-1], c_counter (int) = the initalized correctness counter
	Returns: c_counter (int) = contains data used for scoring
	'''
	tweets_in_list(number, user_tweets)
	y= random.randint(0,len(user_tweets)-1)
	print("\n" + "Tweet "+ str(number+1)+ ": " + user_tweets[y],)
	guess[number] = input("Guess the twitter handle for this tweet: ")
	if guess[number] == twitter_users[number]:
		print(guess[number] + " is the correct twitter handle!\n")
		c_counter=c_counter+1
		return c_counter
	else:
		print("That's not quite right\n")
		c_counter=c_counter
		return c_counter


while cont=="y":
	correct_counter = 0
	
	for x in range(n):
		if (n-1)>=x:
			correct_counter=guess_tweet(x,all_tweets[x],correct_counter)
	print ("Your score is "+ str(int(100*correct_counter/n))+ "%\n")
	final_correct_counter.append(100* correct_counter/n)
	cont = input("Would you like to play again? (y/n) : \n")

print ("Your final score is "+ str(int(sum(final_correct_counter)
		/len(final_correct_counter)))+ "%\n")




