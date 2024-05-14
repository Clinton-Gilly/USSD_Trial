const http = require('http');
const { urlencoded } = require('body-parser');
const { config } = require('dotenv');
const AfricasTalking = require('africastalking');

config();

const app = AfricasTalking({
    apiKey: process.env.API_KEY,
    username: process.env.USERNAME,
});

const { USSD } = app;

const PORT = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    let requestBody = '';

    req.on('data', (data) => {
        requestBody += data;

        if (requestBody.length > 1e7) {
            res.writeHead(413, 'Request Entity Too Large', { 'Content-Type': 'text/plain' }).end();
        }
    });

    req.on('end', async () => {
        const data = urlencoded({ extended: false });

        try {
            const body = await data(req);

            // Handle USSD session here
            const { sessionId, serviceCode, phoneNumber, text } = body;

            let response;

            // Logic to handle different USSD stages and responses
            if (text === '') {
                response = 'CON Welcome to Disaster Reporting. \n';
                response += '1. Report a disaster \n';
                response += '2. Check status of reported disaster';
            } else if (text === '1') {
                response = 'CON Please describe the disaster:';
            } else if (text.startsWith('1*')) {
                // Handle disaster reporting logic
                // You can call appropriate APIs to report the disaster
                // and provide appropriate response to the user
                response = 'END Disaster reported successfully. Thank you.';
            } else if (text === '2') {
                // Logic to check status of reported disasters
                response = 'END No reported disasters found.';
            } else {
                response = 'END Invalid input. Please try again.';
            }

            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end(response);
        } catch (error) {
            console.error('Error:', error);
            res.writeHead(500, 'Internal Server Error', { 'Content-Type': 'text/plain' });
            res.end();
        }
    });
});

server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
