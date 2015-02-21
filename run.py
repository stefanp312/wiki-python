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

    resp = twilio.twiml.Response()
    resp.message(reply)
    return str(resp)

def searchWikipedia(query):
    summary = ""
    try:
        summary = wikipedia.summary(search_term, sentences = 2)
    except wikipedia.exceptions.DisambiguationError as e:
        return "That can refer to multiple things. Which did you mean? " + ", ".join(e.options)
    return summary

if __name__ == "__main__":
    app.run(debug=True)
