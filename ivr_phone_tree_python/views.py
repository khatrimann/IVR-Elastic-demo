from flask import (
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for,
)
from twilio.twiml.voice_response import VoiceResponse

from ivr_phone_tree_python import app
from ivr_phone_tree_python.view_helpers import twiml


@app.route('/')
@app.route('/ivr')
def home():
    return render_template('index.html')


@app.route('/ivr/welcome', methods=['POST'])
def welcome():
    response = VoiceResponse()
    with response.gather(
        num_digits=1, action=url_for('menu'), method="POST"
    ) as g:
        g.say(message="Hey, we are from blah team. " +
              "Please press 1 to start the interview. Also pleas enote to continue after each question, press 1" , loop=3)
    return twiml(response)


@app.route('/ivr/menu', methods=['POST'])
def menu():
    selected_option = request.form['Digits']
    option_actions = { '1': _q_1
                      }

    if option_actions.has_key(selected_option):
        response = VoiceResponse()
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()


@app.route('/ivr/planets', methods=['POST'])
def planets():
    selected_option = request.form['Digits']
    option_actions = {'2': "+12024173378",
                      '3': "+12027336386",
                      "4": "+12027336637"}

    if selected_option in option_actions:
        response = VoiceResponse()
        response.dial(option_actions[selected_option])
        return twiml(response)

    return _redirect_welcome()

@app.route('/ivr/question_1', methods=['POST'])
def question_1():
    selected_option = request.form['Digits']
    option_actions = { '1': _q_2}

    if selected_option in option_actions:
        response = VoiceResponse()
        response.say('Heading on to question 2')
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

@app.route('/ivr/question_2', methods=['POST'])
def question_2():
    selected_option = request.form['Digits']
    option_actions = { '1': _q_3}

    if selected_option in option_actions:
        response = VoiceResponse()
        response.say('Heading on to question 3')
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

@app.route('/ivr/question_3', methods=['POST'])
def question_3():
    selected_option = request.form['Digits']
    option_actions = { '1': _q_4}

    if selected_option in option_actions:
        response = VoiceResponse()
        response.say('Heading on to question 4')
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

@app.route('/ivr/question_4', methods=['POST'])
def question_4():
    selected_option = request.form['Digits']
    option_actions = { '1': _q_5}

    if selected_option in option_actions:
        response = VoiceResponse()
        response.say('Heading on to question 5')
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

@app.route('/ivr/question_5', methods=['POST'])
def question_5():
    selected_option = request.form['Digits']
    option_actions = { '1': _q_6}

    if selected_option in option_actions:
        response = VoiceResponse()
        response.say('Heading on to question 6')
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

@app.route('/ivr/question_6', methods=['POST'])
def question_6():
    selected_option = request.form['Digits']
    option_actions = { '1': _q_7}

    if selected_option in option_actions:
        response = VoiceResponse()
        response.say('Heading on to question 7')
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

@app.route('/ivr/question_7', methods=['POST'])
def question_7():
    selected_option = request.form['Digits']
    option_actions = { '1': bye}

    if selected_option in option_actions:
        response = VoiceResponse()
        response.say('You are done')
        option_actions[selected_option](response)
        return twiml(response)

    return _redirect_welcome()

# private methods

def _give_instructions(response):
    response.say("To get to your extraction point, get on your bike and go " +
                 "down the street. Then Left down an alley. Avoid the police" +
                 " cars. Turn left into an unfinished housing development." +
                 "Fly over the roadblock. Go past the moon. Soon after " +
                 "you will see your mother ship.",
                 voice="alice", language="en-GB")

    response.say("Thank you for calling the E T Phone Home Service - the " +
                 "adventurous alien's first choice in intergalactic travel")

    response.hangup()
    return response


def _list_planets(response):
    with response.gather(
        numDigits=1, action=url_for('planets'), method="POST"
    ) as g:
        g.say("To call the planet Broh doe As O G, press 2. To call the " +
              "planet DuhGo bah, press 3. To call an oober asteroid " +
              "to your location, press 4. To go back to the main menu " +
              " press the star key.",
              voice="alice", language="en-GB", loop=3)

    return twiml(response)


def _redirect_welcome():
    response = VoiceResponse()
    response.say("Returning to the main menu", voice="alice", language="en-GB")
    response.redirect(url_for('welcome'))

    return twiml(response)

def _q_1(response):
    with response.gather(
        num_digits=1, action=url_for('question_1'), method="POST", timeout = 120, speech_timeout = 120
    ) as g:
        g.say('What is data science', voice="alice", language="en-GB")
    
    return response

def _q_2(response):
    with response.gather(
        num_digits=1, action=url_for('question_2'), method="POST", timeout = 120, speech_timeout = 120
    ) as g:
        g.say('What are chatbots?', voice="alice", language="en-GB")

    return response

def _q_3(response):
    with response.gather(
        num_digits=1, action=url_for('question_3'), method="POST", timeout = 120, speech_timeout = 120
    ) as g:
        g.say('What is regularization?', voice="alice", language="en-GB")

    return response

def _q_4(response):
    with response.gather(
        num_digits=1, action=url_for('question_4'), method="POST", timeout = 120, speech_timeout = 120
    ) as g:
        g.say('What is logistic regression?', voice="alice", language="en-GB")

    return response

def _q_5(response):
    with response.gather(
        num_digits=1, action=url_for('question_5'), method="POST", timeout = 120, speech_timeout = 120
    ) as g:
        g.say('Explain normal distribution?', voice="alice", language="en-GB")

    return response

def _q_6(response):
    with response.gather(
        num_digits=1, action=url_for('question_6'), method="POST", timeout = 120, speech_timeout = 120
    ) as g:
        g.say('What is k-means algorithm?', voice="alice", language="en-GB")

    return response

def _q_7(response):
    with response.gather(
        num_digits=1, action=url_for('question_7'), method="POST", timeout = 120, speech_timeout = 120
    ) as g:
        g.say('What is collaborative filtering?', voice="alice", language="en-GB")

    return response

def bye(response):
    response.say("Your interview with blah has been done, results will be shared soon " +
                 "Thank you")

    response.hangup()
    return response
