from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    products = ["Ciabata", "Baguete", "Pretzel"]
    return products[1]