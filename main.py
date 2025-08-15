from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')
def menu():
 context = {
  "title": "меню",


  "link vk": "https://vk.com/id612168895",
  "put": "../static/css/style.css",
  "fon": "../static/image/фон сталкера.jpg",
  "audio": "../static/image/Studiya_stalker_-_Stalker_zov_pripyati_koncovka_62816187.mp3",
  "loin": "https://vk.com/id612168895",

 }
 return render_template("index.html", **context)


@app.route('/yupiter/')
def yupiter():
 return render_template('stalker_yupiter.html')


@app.route('/zaton/')
def zaton():
 return render_template('stalker_zaton.html')

@app.route('/pripat/')
def pripat():
 return render_template('prypat.html')











if __name__ == '__main__':
 app.run()