from __future__ import unicode_literals
import twitter
api = twitter.Api(consumer_key='2NaQG8gvhJFQMBqBFSUMtmNXU',
                  consumer_secret='x40pfiGb10mh5O9YrBNRf0sONjKZlRNHjwzcYe7cFmrjWO7MBn',
                  access_token_key='943212098947084288-PqVPedPoMTMyDJVANMMadC1BuKshDNJ',
                  access_token_secret='BVSEfLcE8wvcu9FEOwNwOHqgv35EKvx1Twtt6KLa7G2nr')

print(api)
status = api.PostUpdate('I love python-twitter!')
status = api.PostUpdate('These are lights!')
# print(status.text)
