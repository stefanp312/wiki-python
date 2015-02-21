from flask import Flask, request, redirect, session
import twilio.twiml
import wikipedia

SECRET_KEY = 'donuts'
app = Flask(__name__)

# Try adding your own number to this list!

@app.route("/", methods=['GET', 'POST'])
def main_reply():
    
    from_number = request.values.get('From', None)
    recieved_message = request.values.get('Body')
    counter = session.get('counter', 0)
 
    # increment the counter
    counter += 1
 
    # Save the new counter value in the session
    session['counter'] = counter

    reply = searchWikipedia(query=recieved_message)
    if len(reply)>160:
        reply=reply[0:159]
    resp = twilio.twiml.Response()
    resp.message(reply)
    
    print reply
    print counter
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
