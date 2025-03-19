const express = require('express');
const cors = require('cors');
const fetch = require('node-fetch');

const app = express();
app.use(cors());

app.get('/proxy', async (req, res) => {
    const url = req.query.url;
    if (!url) return res.status(400).send('URL is required');
    
    try {
        const response = await fetch(url);
        const text = await response.text();
        res.send(text);
    } catch (error) {
        res.status(500).send('Error fetching the page');
    }
});

app.listen(3000, () => console.log('Proxy server running on port 3000'));
