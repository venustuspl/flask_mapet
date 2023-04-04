
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    app.run(debug = True, port = 80);

# Zmieniam na 80 by móc wywoływać aplikację  po prostu „localhost” zamiast „localhost:5000”.
# Parametr „debug” powoduje, że zmiany na plikach z kodem będą od razu aktualizowane na serwerze, bez potrzeby restartu.