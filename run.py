from flask import Flask, request, redirect, session
import twilio.twiml
import wikipedia

SECRET_KEY = 'donuts'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!

@app.route("/", methods=['GET', 'POST'])
def main_reply():
    
    from_number = request.values.get('From', None)
    recieved_message = request.values.get('Body')

    #create cmds variable from cookies
    cmds = session.get('cmds', [""])
    searchs = session.get('searchs', [["",0]])

    if "image" in recieved_message:
        #send the wikipedia page iamge
        print "not working"
    elif "more" in recieved_message:
        # query wikipedia with the recieved message and get next sentence
        cmds.append("more")
        lastSearch = searchs[len(searchs)-1]
        print lastSearch
        lastCharacterSeen = lastSearch[1]
        print lastCharacterSeen
        reply = searchWikipedia(query=recieved_message,4)
        nextStringIndex =  reply.index(". ", beg=lastCharacterSeen)
        reply = reply[lastCharacterSeen:nextStringIndex]
    else
        # query wikipedia with the recieved message
        reply = searchWikipedia(query=recieved_message)
        searchs.append([recieved_message,len(reply)])

    #trim the length of the reply to one text
    if len(reply)>160:
        reply=reply[0:159]

    #get the response scheme from twilio and add reply as message body
    resp = twilio.twiml.Response()
    resp.message(reply)

    print reply

    # Save the new cmds/searchs list in the session
    session['cmds'] = cmds
    session['searchs'] = searchs

    return str(resp)

def searchWikipedia(query, sentences = 1):
    summary = ""
    try:
        summary = wikipedia.summary(query, sentences = sentences)
    except wikipedia.exceptions.DisambiguationError as e:
        #return "That can refer to multiple things. Which did you mean? " + ", ".join(e.options)
        summary = wikipedia.summary(e.options[1], sentences = sentences)
    return summary

if __name__ == "__main__":
    app.run(debug=True)
