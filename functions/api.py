import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

NEWS_API_KEY = config("NEWS_API_KEY")
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
TMDB_API_KEY = config("TMDB_API_KEY")
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

class api:
    def __init__(self,args):
        self.intent=args["intent"]
        self.object=args["object"]
        self.location=args["location"]
        self.source=args["source"]
        self.recipient=args["recipient"]
        self.subject=args["subject"]
    
    def SearchEntity(self):
        if(self.source=="google"):
            kit.search(self.object)
        elif(self.source=="youtube"):
            kit.playonyt(self.object)
        elif(self.source=="wikipedia"):
            wikipedia.summary(self.object, sentences=2)
        else:
            print("source not found")
            pass
    
    def SendEmail(self):
        try:
            email = EmailMessage()
            email['To'] = self.recipient
            email["Subject"] = self.subject
            email['From'] = EMAIL
            email.set_content(message)
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.login(EMAIL, PASSWORD)
            s.send_message(email)
            s.close()
            return True
        except Exception as e:
            print(e)
            return False
    
    def get_latest_news(self):
        news_headlines = []
        res = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
        articles = res["articles"]
        for article in articles:
            news_headlines.append(article["title"])
        return news_headlines[:5]

    def get_weather_report(self):
        res = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={self.location}&appid={OPENWEATHER_APP_ID}&units=metric").json()
        weather = res["weather"][0]["main"]
        temperature = res["main"]["temp"]
        feels_like = res["main"]["feels_like"]
        return weather, f"{temperature}℃", f"{feels_like}℃"

    def get_trending_movies(self):
        trending_movies = []
        res = requests.get(
            f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
        results = res["results"]
        for r in results:
            trending_movies.append(r["original_title"])
        return trending_movies[:5]

    def get_random_joke(self):
        headers = {
            'Accept': 'application/json'
        }
        res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
        return res["joke"]

    def get_random_advice(self):
        res = requests.get("https://api.adviceslip.com/advice").json()
        return res['slip']['advice']
