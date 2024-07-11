from falsk import Flask

app = Flask(name)

@app.route('/')
def index():
    return 'Hola mundo'

if name == 'main':
  app.rum(debug=True, host='0.0.0.0')
