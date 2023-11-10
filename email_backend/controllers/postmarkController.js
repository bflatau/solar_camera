const postmark = require("postmark");
const fs = require('fs');
var Airtable = require('airtable');
const axios = require('axios');


var base = new Airtable({ apiKey: process.env.AIRTABLE_API_KEY }).base(process.env.AIRTABLE_BASE_ID);



function fetchAirtableRecords(){

    return new Promise((resolve, reject) => {

        let sunsetImages;
  
        base('Table 1').select({
            // Selecting the first 5 records in Grid view:
            maxRecords: 5,
            view: "Grid view"
        }).eachPage(function page(records, fetchNextPage) {
            // This function (`page`) will get called for each page of records.

            sunsetImages = records.map(function (record) {


                return new Promise((resolve, reject) => {
                    axios.get(`${record.get('Image_URL')}.jpg`, { responseType: 'arraybuffer' })
                        .then(response => {
                           let base64Image = `data:${response.headers['content-type']};base64,` + Buffer.from(response.data).toString('base64');
                           resolve(base64Image);
                            // console.log('<img src="' + base64Image + '"/>');
                        })
                        .catch(error => console.log(error));    
                })

                // return record.get('Image_URL')
            })

            // records.forEach(function (record) {
            //     console.log('Retrieved', record.get('Image_URL'));
            //     console.log('Retrieved', record.get('Created'));
            // });

            // To fetch the next page of records, call `fetchNextPage`.
            // If there are more records, `page` will get called again.
            // If there are no more records, `done` will get called.
            fetchNextPage();

        }, function done(err) {
            // console.log(sunsetImages)
            if (err) { console.error(err); return; }


            Promise.all(sunsetImages).then(function (results) {
                // console.log(results)
                // sunsetImages = results;
                resolve(results)
            })



        });

    });


}



/// SETUP POSTMARK ///
const client = new postmark.ServerClient(process.env.POSTMARK_API_KEY);

async function testEmail (req, res){


    let imageArray = await fetchAirtableRecords();

    console.log('this is image array', imageArray)


    // res.header("Access-Control-Allow-Origin", "*");
    // client.sendEmail({
    //     "From": process.env.FROM_EMAIL,
    //     "To": process.env.TO_EMAIL,
    //     "Subject": `Today's Santa Cruz Sunset`,
    //     // "Tag": req.body.type,
    //     "HtmlBody": fs.readFileSync("./templates/test-email.html", "utf8"),
    //     "TrackOpens": true,
    //     "TrackLinks": "HtmlAndText",
    //     "MessageStream": "outbound",
    //     // "Attachments":[

    //     //     {
    //     //         "Name": "image-1.jpg",
    //     //         "ContentID": "cid:image-1.jpg",
    //     //         "Content": 'https://res.cloudinary.com/dubqxoatm/image/upload/image_11_09_2023_17:02:53.jpg'.toString('base64'),
    //     //         "ContentType": "image/jpg"
    //     //     },

    //     // ]

    // });
    res.json(req.body.email);
    // console.log(req.body)
}

// https://res.cloudinary.com/dubqxoatm/image/upload/image_11_09_2023_17:02:53.jpg

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


module.exports.testEmail = testEmail;





