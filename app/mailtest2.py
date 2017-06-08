from flask_mail import Message

@app.route("/")
def index():

    msg = Message("Hello",
                  sender="noamhermanse3@gmail.com",
                  recipients=["noamhermanse@gmail.com"])