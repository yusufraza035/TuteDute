const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const FLASK_BACKEND_URL = process.env.FLASK_BACKEND_URL || 'http://backend:5000';

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// GET - Render the form
app.get('/', (req, res) => {
  res.render('index', { result: null, error: null, formData: null });
});

// POST - Handle form submission and forward to Flask
app.post('/submit', async (req, res) => {
  const { name, email, age, subject, message, gender, interest } = req.body;

  const formData = { name, email, age, subject, message, gender, interest };

  try {
    const response = await axios.post(`${FLASK_BACKEND_URL}/process`, formData, {
      headers: { 'Content-Type': 'application/json' },
      timeout: 10000,
    });

    res.render('index', {
      result: response.data,
      error: null,
      formData,
    });
  } catch (error) {
    const errMessage =
      error.response?.data?.error ||
      error.message ||
      'Failed to connect to the backend service.';
    res.render('index', {
      result: null,
      error: errMessage,
      formData,
    });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', service: 'frontend', timestamp: new Date().toISOString() });
});

app.listen(PORT, () => {
  console.log(`✅ Frontend server running on http://localhost:${PORT}`);
  console.log(`🔗 Connected to Flask backend at: ${FLASK_BACKEND_URL}`);
});
