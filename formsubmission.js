const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));

// Define a route to handle the form submission
app.post('/save-form-data', (req, res) => {
  // Extract the form data from the request body
  const { name, email, message } = req.body;

  // Perform desired actions with the form data (e.g., save to a database, write to a file, etc.)

  // Return a response indicating the success or failure of the form submission
  res.send('Form data saved successfully.');
});

// Start the server
app.listen(9999, () => {
  console.log('Server running on http://localhost:9999');
});