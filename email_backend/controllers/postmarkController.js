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
                            // let base64Image = `data:${response.headers['content-type']};base64,` + Buffer.from(response.data).toString('base64');
                            let base64Image = Buffer.from(response.data, 'binary').toString('base64');
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

async function sendEmail (req, res){

    let imageArray = await fetchAirtableRecords();
    let date = new Date();

    // console.log( typeof imageArray[0])

    res.header("Access-Control-Allow-Origin", "*");
    client.sendEmail({
        "From": process.env.FROM_EMAIL,
        "To": process.env.TO_EMAIL,
        "Subject": `Santa Cruz Sunset on ${date.toLocaleDateString()}`,
        // "Tag": req.body.type,
        "HtmlBody": fs.readFileSync("./templates/daily-sunset-template.html", "utf8"),
        "TrackOpens": true,
        "TrackLinks": "HtmlAndText",
        "MessageStream": "outbound",
        "Attachments":[

            {
                "Name": "image-1.jpg",
                "ContentID": "cid:image-1.jpg",
                "Content": imageArray[0],
                "ContentType": "image/jpeg"
            },

            {
                "Name": "image-2.jpg",
                "ContentID": "cid:image-2.jpg",
                "Content": imageArray[1],
                "ContentType": "image/jpeg"
            },

            {
                "Name": "image-3.jpg",
                "ContentID": "cid:image-3.jpg",
                "Content": imageArray[2],
                "ContentType": "image/jpeg"
            },

            {
                "Name": "image-4.jpg",
                "ContentID": "cid:image-4.jpg",
                "Content": imageArray[3],
                "ContentType": "image/jpeg"
            },

            {
                "Name": "image-5.jpg",
                "ContentID": "cid:image-5.jpg",
                "Content": imageArray[4],
                "ContentType": "image/jpeg"
            },

        ]

    });


    res.json(req.body.email);
    // console.log(req.body)
}


module.exports.sendEmail = sendEmail;





