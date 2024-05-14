USSD Trial
Overview
This repository contains a Python script for implementing a USSD (Unstructured Supplementary Service Data) trial. USSD is a technology used by GSM cellular telephones to communicate with the service provider's computers. It's commonly used for menu-based information and services, such as mobile banking, prepaid callback services, and more.

This trial implementation aims to demonstrate the basic functionality of USSD by providing a simple menu-based system that users can interact with using their mobile phones.

Requirements
Python 3.x
Flask (for web server)
ngrok (for local testing)
Usage
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/ussd-trial.git
Navigate to the project directory:
bash
Copy code
cd ussd-trial
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Start the Flask web server:
bash
Copy code
python app.py
Expose your local server to the internet using ngrok:
bash
Copy code
ngrok http 5000
Note the ngrok URL generated, and configure it as the callback URL in your USSD service provider's dashboard.

Test the USSD trial by dialing the provided USSD code on your mobile phone. Follow the on-screen prompts to navigate through the menu options.

File Structure
app.py: Contains the Flask application for handling USSD requests.
ussd_menu.py: Defines the menu structure and logic for the USSD trial.



