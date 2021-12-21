import tweepy as tp
import credentials
import time

# function that adds a space in between ingredients that are more than 1 word long
def make_spacing(str):
    for i in range(0, len(str)-1):
        if str[i].islower() and str[i+1].isupper():
            str = str[0:i+1] + " " + str[i+1:]
            make_spacing(str)
    return str

# Credentials to login to twitter api
consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
access_token = credentials.access_token
access_secret = credentials.access_token_secret

# Login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# adding each recipe to a list
recipes_file = open('generated_recipes.txt', 'r')
recipe_list = recipes_file.readlines()


for r in recipe_list:
    # for the recipe we add each ingredient as an element to the recipe
    recipe = r.split()
    # we add a whitespace in between ingredients that are multiple words
    for i in range(0, len(recipe)):
        recipe[i] = make_spacing(recipe[i])

    # Creating the structure for the tweet
    line = '#CocktailOfTheDay \n'
    for ingredient in recipe:
        line = line + ingredient + '\n'
    line = line + '\nEnjoy!'
    # Writing this tweet to a file
    with open('tweet.txt', 'w') as w_file:
        w_file.write(line)
    w_file.close()

    # Tweeting the tweet we just added to the file
    with open('tweet.txt', 'r') as r_file:
        api.update_status(r_file.read())
        print(r_file.read())
    r_file.close()
    # uncomment break if you only want 1 tweet
    break

    # sleep for 1 day
    #time.sleep(86400)

    #print("Cocktail Recipe of the Day:")
    #for ingredient in recipe:
    #    print(ingredient)
    #print('\nEnjoy!\n')

recipes_file.close()
