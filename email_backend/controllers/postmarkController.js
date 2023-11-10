const postmark = require("postmark");
const fs = require('fs');


/// SETUP POSTMARK ///
const client = new postmark.ServerClient(process.env.POSTMARK_API_KEY);

exports.testEmail = (req, res) => {
    res.header("Access-Control-Allow-Origin", "*");
    client.sendEmail({
        "From": process.env.FROM_EMAIL,
        "To": process.env.TO_EMAIL,
        "Subject": `Today's Santa Cruz Sunset`,
        // "Tag": req.body.type,
        "HtmlBody": fs.readFileSync("./templates/test-email.html", "utf8"),
        "TrackOpens": true,
        "TrackLinks": "HtmlAndText",
        "MessageStream": "outbound"
    });
    res.json(req.body.email);
    console.log(req.body)
}



exports.sendEmail = (req, res) => {

    
    //BENDO FIX THIS WITH BETTER CORS SOLUTION
    res.header("Access-Control-Allow-Origin", "*");
    client.sendEmail({
        "From": "ben@awarchitect.com",
        "To": req.body.email,
        "Subject": "Ana Williamson Architect Process Materials",
        "Tag": req.body.type,
        "HtmlBody": fs.readFileSync("./assets/templates/process-template.html", "utf8"),
        "TrackOpens": true,
        "TrackLinks": "HtmlAndText",
        "Attachments": [
            // {
            //   "Name": "palo_alto_weekly.pdf",
            //   "Content": fs.readFileSync("./assets/pdfs/palo_alto_weekly.pdf").toString('base64'),
            //   "ContentType": "application/octet-stream"
            // },
            {
                "Name": "AWA-logo-2017.png",
                "ContentID": "cid:AWA-logo-2017.png",
                "Content": fs.readFileSync("./assets/images/AWA-logo-2017.png").toString('base64'),
                "ContentType": "image/png"
            },
            {
                "Name": "icon-facebook.png",
                "ContentID": "cid:icon-facebook.png",
                "Content": fs.readFileSync("./assets/images/icon-facebook.png").toString('base64'),
                "ContentType": "image/png"
            },
            {
                "Name": "icon-houzz.png",
                "ContentID": "cid:icon-houzz.png",
                "Content": fs.readFileSync("./assets/images/icon-houzz.png").toString('base64'),
                "ContentType": "image/png"
            },
            {
                "Name": "icon-instagram.png",
                "ContentID": "cid:icon-instagram.png",
                "Content": fs.readFileSync("./assets/images/icon-instagram.png").toString('base64'),
                "ContentType": "image/png"
            },
            {
                "Name": "icon-pinterest.png",
                "ContentID": "cid:icon-pinterest.png",
                "Content": fs.readFileSync("./assets/images/icon-pinterest.png").toString('base64'),
                "ContentType": "image/png"
            },
            {
                "Name": "proccessemail-1.jpg",
                "ContentID": "cid:processemail-1.jpg",
                "Content": fs.readFileSync("./assets/images/processemail-1.jpg").toString('base64'),
                "ContentType": "image/jpg"
            },
            {
                "Name": "proccessemail-2.jpg",
                "ContentID": "cid:processemail-2.jpg",
                "Content": fs.readFileSync("./assets/images/processemail-2.jpg").toString('base64'),
                "ContentType": "image/jpg"
            },
            // {
            //   "Name": "proccessemail-3.png",
            //   "ContentID": "cid:processemail-3.png",
            //   "Content": fs.readFileSync("./assets/images/processemail-3.png").toString('base64'),
            //   "ContentType": "image/png"
            // },

        ],
    });
    res.json(req.body.email);
    console.log(req.body)
};