const express = require('express');
const app = express();
const fs = require('fs');
const path = require('path');

app.use(express.urlencoded({ extended: true }));

// Define a route to handle the form submission
app.post('/save-form-data', (req, res) => {
  // Extract the form data from the request body
  const { name, email, message } = req.body;

  // Create a new file path to save the form data
  const filePath = path.join(__dirname, 'data.txt');

  // Format the form data as a string
  const formDataString = `Name: ${name}\nEmail: ${email}\nMessage: ${message}\n`;

  // Save the form data to the file
  fs.writeFile(filePath, formDataString, (err) => {
    if (err) {
      console.error('Error:', err);
      res.status(500).send('Failed to save form data.');
    } else {
      console.log('Form data saved successfully.');
      res.send('Form data saved successfully.');
    }
  });
});

// Start the server
app.listen(9029, () => {
  console.log('Server running on http://localhost:9029');
});

