const express = require('express');
const spawn = require('child_process').spawn;
var cors = require('cors')

const app = express();
const port = process.env.PORT || 9999;
app.use(cors())

app.get('/', (req, res) => {
    const email = req.query.email; // Retrieve the user's message from the query string
    const auth = spawn('python',['./auth.py', email]);
    let authCode = '';

    auth.stdout.setEncoding('utf8');
    auth.stdout.on('data', (data)=>{
        authCode += data;
    })

    auth.on('close', (code)=>{
        res.send(authCode);
    })

});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});