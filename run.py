from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
}

@app.route("/", methods=['GET', 'POST'])
def main_reply():
    
    from_number = request.values.get('From', None)
    recieved_message = request.values.get('Body')
    resp = twilio.twiml.Response()
    with resp.message(recieved_message) as m:
        m.media("https://demo.twilio.com/owl.png")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
