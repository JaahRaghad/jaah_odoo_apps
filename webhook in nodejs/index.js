const express = require('express');
const bodyParser = require('body-parser');

const app = express().use(bodyParser.json());

app.listen(3100, () => {
    console.log("Webhook is listining");
});