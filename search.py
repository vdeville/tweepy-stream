# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import tweepy
import json
import sys
import pyglet
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


"""

    Warning, keyrword @MyTheValentinus for example, capture all tweets when @MyTheValentinus is writing, non sensitive case.

    /!\ All keywords are non sensitive case.

    To search a hastag, simply search #YouFavoritePoneyHastag in keyword.

    For example: I would like to get all tweet contain my twitter pseudo, my hastag and my lastname
    my pseudo is: @MyTheValentinus
    my hastag is: #valentin
    my lastname is: deville

    Total keywords is: @MyTheValentinus,#valentin,deville

    This chain of keyword get all of them.

"""
terme = raw_input(bcolors.OKGREEN + "Quels termes souhaitez vos rechercher en temps réel ? Séparés par une virgule (ex: MyTheValentinus,#Carnaval,@MyTheValentinus )\n")
compteur = 0
music = pyglet.resource.media('a_team.wav')  # Load a epic sound !

class getData(StreamListener):

    def on_data(self, data):
        global compteur
        compteur += 1

        data = json.loads(data)  # Load JSON

        """
            Print different user and tweet info
        """
        userData = bcolors.ENDC + bcolors.BOLD + data["user"]["screen_name"]
        userData.encode('utf-8')  # Fix problem with user special char
        print (userData)
        if data["text"]:

            #music.play()  # Play the sound
            print (bcolors.OKBLUE + data["text"])  # Print text
            print (bcolors.WARNING + unicode(u"\u2501"), unicode(u"\u2501"), unicode(u"\u2501"), unicode(u"\u2501"), unicode(u"\u2501"), 'Nbr: ', bcolors.BOLD, compteur)  # separator
            return True
        else:
            return True

    def on_error(self, status):  # If error print status
        print(status)

try:
    """
        Launch stream tweet and set filter to track.
    """
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, getData())
    stream.filter(track=[terme])

except KeyboardInterrupt:  # If press CTRL + C
    print (bcolors.FAIL + bcolors.BOLD + "You kill the script, thank for using my script. Follow me on twitter " + bcolors.UNDERLINE + "@MyTheValentinus" + bcolors.ENDC)
    sys.exit()
