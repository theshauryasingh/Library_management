const express = require('express');
const multer = require('multer');
const path = require('path');

const router = express.Router();

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, Date.now() + '-' + file.originalname);
  }
});

const upload = multer();

router.post('/upload-cover', upload.single('coverImage'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded.');
  }
  const filePath = path.join(__dirname, '..', 'uploads', req.file.filename);
  res.status(200).json({
    message: 'File uploaded successfully!',
    filePath: filePath
  });
});

module.exports = router;

