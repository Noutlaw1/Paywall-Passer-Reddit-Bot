import praw
import webbrowser
import requests
from bs4 import BeautifulSoup

#Reddit username is "Paywall Passer"

def authenticate():
    url_token = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
    refresh_token =  'xxxxxxxxxxxxxxxxxxxx'
    r = praw.Reddit('Paywall Passer')
    r.set_oauth_app_info(client_id='xxxxxxxxxxxxxxxx',
                         client_secret='xxxxxxxxxxxxxxxxxxxxx',
                         redirect_uri='xxxxxxxxxxxxxxxxxxxxx/'
                                      'authorize_callback')
    r.refresh_access_information(refresh_token)
    return r

def Gather_Valid_Submissions(r):
    #Filters out self-posts.
    class SM:
        def __init__(self, title, author, url, link, s):
            self.title = title
            self.author = author
            self.url = url
            self.link = link
            self.submission_obj = s #Submission object for checking if commented already.
    subreddit = r.get_subreddit('LostGeneration')
    submissions = subreddit.get_new(limit=100)
    list = []
    for submission in submissions:
        if submission.is_self == False:
            sub_entry = SM(submission.title, submission.author, submission.url, submission.short_link, submission)
            list.append(sub_entry)
    return list

def find_wsj(sub_list):
    string = "wsj.com"
    wsj_list = []
    for submission in sub_list:
        if string in submission.url:


            wsj_list.append(submission)

    return wsj_list

#Basically, this one loops through a list of SM objects to check and see if the bot has already replied.

def Check_AlreadyPosted(list):
     no_replies = []
     for item in list:
            sub_obj = item.submission_obj
            comments = sub_obj.comments
            for comment in comments:
                author = commment.author
                if author.name == "PaywallPasser":
                    break
                no_replies.append(item)
            return no_replies





def scraper(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html',
        'Referer': 'https://www.google.com/'
    }
    response = requests.get(url, headers=headers)
    text = BeautifulSoup(response.text, "lxml")
    print text

    t = text.find_all('p')

    # Search with regex?
    # for line in a:
    # l = str(line)
    #  if re.match('*<a*', l):
#     print line
    for paragraph in t:

        paragraph = paragraph.getText()

    return t



def main():

    #Authenticates with reddit via OAUTH
    r = authenticate()
    #Filters out self-posts, past 100.
    Submissions = Gather_Valid_Submissions(r)
    #Finds WSJ posts.
    wsj_list = find_wsj(Submissions)
    #Need it to check and see if it's responded to them yet.


    #Scrapes the text from WSJ.
    text = scraper(wsj)
    print text
    return text








