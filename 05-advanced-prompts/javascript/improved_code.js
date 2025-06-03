// Here are three improvements for your Express.js application:

// Error Handling Middleware: Add proper error handling to make 
// your application more robust and provide useful error responses.

// Environment Variable for Port: Use environment variables for 
// configuration to make your app more flexible across different 
// environments.

// Input Validation and Query Parameter Support: Add support for 
// query parameters with validation to make your endpoint more 
// functional.

// Suggestions provided by Claude 3.7 Sonnet on 2025-5-15

const express = require('express');

const app = express();
// Improvement 2: Use environment variable for port with fallback
const PORT = process.env.PORT || 3000;

// Improvement 3: Add query parameter support with validation
app.get('/', (req, res) => {
  // Get name from query parameter or use default
  const name = req.query.name || 'World';
  
  // Basic input validation
  if (typeof name !== 'string') {
    return res.status(400).json({ error: 'Name must be a string' });
  }
  
  res.send(`Hello, ${name}!`);
});

// Improvement 1: Add error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something went wrong!');
});

app.listen(PORT, () => {
  console.log(`Example app listening on port ${PORT}!`);
});