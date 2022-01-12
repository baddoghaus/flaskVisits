from flask import Flask
from redis import Redis

app = Flask(__name__)
client = Redis(
    host = 'redis-server',
    port = 6379
)

client.set('visits', 0)

@app.route('/')
def home():
    visits = client.get('visits')
    client.set('visits', int(visits) + 1)
    return "Number of visits is %d" % (int(visits))
