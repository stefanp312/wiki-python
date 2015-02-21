from flask import Flask, request, redirect
import twilio.twiml
import wikipedia

app = Flask(__name__)

# Try adding your own number to this list!

@app.route("/", methods=['GET', 'POST'])
def main_reply():
    
    from_number = request.values.get('From', None)
    recieved_message = request.values.get('Body')

    reply = searchWikipedia(query=recieved_message)
    if len(reply)>160:
        reply=reply[0:159]
    resp = twilio.twiml.Response()
    resp.message(reply)

    for message in client.messages:
        print message.body
    return str(resp)

def searchWikipedia(query):
    summary = ""
    try:
        summary = wikipedia.summary(query, sentences = 1)
    except wikipedia.exceptions.DisambiguationError as e:
        #return "That can refer to multiple things. Which did you mean? " + ", ".join(e.options)
        summary = wikipedia.summary(e.options[1], sentences = 1)
    return summary

if __name__ == "__main__":
    app.run(debug=True)
