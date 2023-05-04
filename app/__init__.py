app = Flask(__name__)

app.secret_key = os.urandom(12)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/map", methods=['GET', 'POST'])
def map():
    if request.method == 'GET':
        return render_template('home.html')