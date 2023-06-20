from flask import Flask, render_template, request, url_for, redirect
import mysql.connector
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


app = Flask(__name__)
conn = mysql.connector.connect(host="localhost", user="root", password="", database="users")
cursor = conn.cursor()
bot = ChatBot("chatbot = ChatBot('ChatBott')")

trainer = ListTrainer(bot)

cool = ("I would like a cooler temperature vacation", "cooler temperature", "cooler weather", "cooler", "cool")

hot = ("I would like a hotter temperature vacation", "hotter temperature", "hotter weather", "hotter", "hot")

beach = ["I would like a beach vacation", "beach vacation", "beach", "I would love a beach vacation"]
mountain = ["I would like a mountain vacation", "mountain vacation", "mountain", "I would love a mountain vacation"]
city = ["I would like a city vacation", "city vacation", "city", "I would love a city vacation"]

exit_conditions = (":q", "quit", "exit")


id = 1

weatherh = ""
typeb = ""
weatherc = ""
typem = ""
place1 = ""
typec=""
place2=""

@app.route('/')
def welcome():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login1.html")


@app.route('/register')
def register():
    return render_template("register2.html")


@app.route('/home')
def home():
    return render_template("home_page.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/homeyoyo')
def yoyo():
    return render_template("home_page.html")


@app.route('/deals')
def deals():
    return render_template("Deals.html")


@app.route('/login_validation',methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    cursor.execute("""SELECT * FROM user WHERE email LIKE '{}' AND password LIKE '{}'""".format(email, password))
    users = cursor.fetchall()
    print(users)
    if len(users) > 0:
        return render_template('home_page.html')
    else:
        return "incorect password/username"


@app.route('/add_user', methods=['POST'])
def add_user():
    global id
    name=request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')
    cursor.execute("""INSERT INTO user (user_id,name,email,password) VALUES 
    ('{}','{}','{}','{}')""".format(id, name, email, password))
    conn.commit()
    id = id+1
    return render_template('home_page.html')



@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if userText in cool:
        global weatherc
        weatherc = "cool"

    if userText in hot:
        global weatherh
        weatherh = "hot"

    if userText in beach:
        global typeb
        typeb = "beach"
        hi()


    if userText in mountain:
        global typem
        typem = "mountain"
        hi()

    if userText in city:
        global typec
        typec = "city"
        hi()
    return str(bot.get_response(userText))



@app.route('/about999')
def about999():
    return render_template("about1.html")





def hi():
    global weatherc
    global typeb
    global weatherh
    global typem
    global typec
    global place1
    global place2
    if weatherc == "cool" and typeb == "beach":

        weatherc=""
        typeb=""

    if weatherc == "cool" and typec == "city":
        global place1
        print("delhi")
        place1="delhi"
        weatherc=""
        typec=""

    if weatherh == "hot" and typec == "city":
        global place2
        print("mumbai")
        place2="mumbai"
        weatherh=""
        typec=""

    if weatherh == "hot" and typeb == "beach":
        print("pondicherry")
        weatherh = ""
        typeb = ""
    if weatherc == "cool" and typem == "mountain":
        print("shimla")
        weatherc = ""
        typem = ""
    if weatherh == "hot" and typem == "mountain":
        print("kalpetta")
        weatherh = ""
        typem = ""



@app.route("/chatbot")
def chatbot():

    if place1 == "delhi":
        return redirect(url_for('place1'))
    if place2 == "mumbai":

        return redirect(url_for('place2'))
    return render_template("chatbot.html")


@app.route("/place1")
def place1():
    global place1
    place1=""
    return render_template("place1.html")

@app.route("/place2")
def place2():
    global place2
    place2=""
    return render_template("place2.html")

def ref():
    if place1=="delhi":
        print("hi")
        return render_template("place1.html")
@app.route('/book999')
def book999():

    global place
    place=""
    return render_template("book_know.html")


if __name__ == "__main__":
    app.run(debug=True)
