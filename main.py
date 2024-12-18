import os 
import pytesseract
import cv2
import json

workouts = []

tesseract_path = os.path.join(os.path.dirname(__file__), 'Tesseract-OCR', 'tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path

img_dir_path = "media"
images = []

for file in os.listdir(img_dir_path):
    file_path = os.path.join(img_dir_path, file)
    
    images.append(file_path)

for image in images:
    workout = {}

    img = cv2.imread(image)
    # cv2.imshow("Image", img)

    date = img[100:180, 220:500]
    date_text = pytesseract.pytesseract.image_to_string(date)
    formatted_date = date_text.split(",")[1].strip()
    workout["Date"] = formatted_date

    main_stats = img[320:520, 0:img.shape[0]]
    main_stats_text = pytesseract.pytesseract.image_to_string(main_stats, lang='eng')
    main_stats_text = main_stats_text.split("\n")
    main_stats_data = main_stats_text[0]
    distance, duration, calories = main_stats_data.split(' ')[0], main_stats_data.split(' ')[1], main_stats_data.split(' ')[2]
    workout["Distance"] = distance
    workout["Duration"] = duration
    workout["Calories"] = calories

    other_stats_content = img[500:1160, 120:img.shape[0]]

    start_y = 0
    x0, x1 = other_stats_content.shape[1] // 2, other_stats_content.shape[1]
    section_height = 130

    for i in range(3):
        stat = other_stats_content[start_y: start_y + section_height, x0: x1]
        stat_text = pytesseract.pytesseract.image_to_string(stat, lang='eng')

        
        value = stat_text.split(" ")[0].strip()
        
        if i == 0:
            # cv2.imshow("Average Pace", stat)
            workout["Average Pace"] = value
        elif i == 1:
            workout["Average Speed"] = value
        elif i == 2:
            workout["Max Speed"] = value
 
        start_y = start_y + section_height

    
    start_time = img[1430:1570, img.shape[1] - 150:img.shape[1]]
    start_time_text = pytesseract.pytesseract.image_to_string(start_time)
    workout["Start Time"] = start_time_text.strip()

    workouts.append(workout)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


with open('data.json', 'w') as json_file:
    json.dump(workouts, json_file, indent=4)