/// SETUP DEPENDENCIES ///
const express = require('express');
const bodyParser = require("body-parser");
require('dotenv').config();
const app = express();
const cors = require('cors');


/// REQUIRE CONTROLLERS ///
const emailController = require('./controllers/postmarkController');

/// SET UP CORS ///
// need to call cors before setting up routes
// Set up a whitelist and check against it:

// const whitelist = ['http://test.awarchitect.com']
// const corsOptions = {
//     origin: function (origin, callback) {
//         if (whitelist.indexOf(origin) !== -1) {
//             callback(null, true)
//         } else {
//             callback(new Error('Not allowed by CORS'))
//         }
//     }
// }

/// USE MIDDLEWARE ///
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
// app.use(cors(corsOptions));
app.use(cors());

app.route('/email')
    .post(emailController.sendEmail)

/// SET SERVER CONSTANTS ///
const PORT = 8080;
const HOST = '0.0.0.0';

/// RUN SERVER ///
app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);


