# Your code goes here
from flask import Flask, request

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd():
    session_id   = request.values.get("sessionId", None)
    serviceCode  = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text         = request.values.get("text", "default")


    response = ''

    if text == '':
        response = 'CON Welcome to our Emergency Service Dial *789*60000# for Emergeny response\n1. Report an emergency\n2. Speak to an agent'
    elif text == '1':
        response = 'CON Choose information you want to Report\n1. Crime\n2. Fire\n3. Accident\n4. Health Issue\n5. Floods\n6. Others'
    elif text == '2':
        response = f'END Please contact our customer care on 0800 123 456\nYour phone number is {phone_number}'
    elif text.startswith('1*1'):
        response = 'END You reported a Crime\n1. Robbery\n2. Kidnapping\n3. Murder\n4. Mob Justice'
    elif text.startswith('1*2'):
        response = 'END You reported a Fire\n1. Electrical fire\n2. Gas explosion\n3. Others'
    elif text.startswith('1*3'):
        response = 'END You reported an Accident\n1. Traffic Accidents\n2. Home Accidents\n3. Industrial Accidents\n4. Medical Accidents\n5. Others'
    elif text.startswith('1*4'):
        response = 'END You reported a Health Issue\n1. Asthma\n2. Stroke'
    elif text.startswith('1*5'):
        response = 'END You reported Floods\n1. Heavy floods\n2. Burst river banks\n3. Other'
    elif text.startswith('1*6'):
        response = 'END You reported Others\nMention your Emergency'
    else:
        response = 'END Invalid selection'

    return response


@app.route('/', methods=['GET'])
def index():
    return 'Welcome to Emergency Service Dial *789*60000# for Emergency response'

if __name__ == '__main__':
    app.run(debug=True)
