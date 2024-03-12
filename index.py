from ultralytics import YOLO
from playsound import playsound
from gtts import gTTS
import winsound
frequency = 2500 
duration = 1000  


model = YOLO("model.pt")
results = model.predict(source='0', show=True)
for detection in results.xyxy[0]:
    class_id = int(detection[4])
    confidence = detection[5]  
    if class_id == 1 and confidence > 0.2:  
        winsound.Beep(frequency, duration)
    elif class_id == 3 and confidence > 0.2: 
        winsound.Beep(frequency, duration)
    elif class_id == 4 and confidence > 0.2: 
        winsound.Beep(frequency, duration)
    elif class_id == 5 and confidence > 0.2: 
        winsound.Beep(frequency, duration)
    elif class_id == 6 and confidence > 0.2: 
        winsound.Beep(frequency, duration)
print("Plastic detector",results)


