# Workout OCR Tracker

__Workout OCR Tracker__ is a Python-based tool that uses Optical Character Recognition (OCR) technology to automatically extract and organize workout data from images. The project leverages the power of Tesseract OCR and OpenCV to recognize text from workout screenshots, such as exercise duration, distance, calories burned, and other fitness metrics.

## Features

- Extract workout data (distance, duration, calories, pace, speed, start time) from images.
- Supports automatic processing of multiple images in a directory.
- Organizes extracted data into a structured JSON format.
- Compatible with workout data screenshots typically captured from Adidas Running.

## Technologies Used

- __Python__
- __OpenCV__: For image manipulation and processing
- __Tesseract OCR__: An open-source OCR engine used to extract text from images
- __JSON__: Data is organized and saved in JSON format

## Project Structure

```
Workout-OCR-Tracker/
│
├── media/                  # Directory containing workout images
│   ├── workout1.png
│   └── workout2.png
│
├── main.py                 # Python script for extracting and processing data
├── requirements.txt        # Dependencies for the project
└── README.md         
```

## How it Works

1. __Image Processing__: OpenCV is used to read and extract regions of interest (ROI) from the workout images. These regions correspond to the different pieces of workout data like distance, time, and calories.

2. __OCR Extraction__: Tesseract OCR processes the extracted regions and converts the image-based text into actual text. This is done for key sections of the workout image.

3. __Data Parsing__: The text extracted from the image is parsed to isolate the relevant values such as distance, duration, and calories burned.

4. __JSON Output__: The structured workout data is saved into a JSON file for further use.