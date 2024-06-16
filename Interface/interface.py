import keyboard
import requests
import json
import sounddevice as sd
import wavio

if __name__ == "__main__":
    print("Interface Started...")
    while True:
        if keyboard.is_pressed("m"):
            RATE=48000
            CHANNEL=2
            DURATION = 5  # seconds
            print("Recording Audio for "+str(DURATION)+" seconds")
            myrecording = sd.rec(DURATION * RATE, samplerate=RATE, channels=CHANNEL, dtype='float64')
            sd.wait()
            print("Audio recording complete , Play Audio")
            wavio.write("testsent.wav",data=myrecording,rate=RATE,sampwidth=2)
            print(myrecording)
            base_url = "http://10.145.122.143:5050"
            
            response = requests.post(base_url, data={
                "data": myrecording.tolist()
            })
            if response.status_code == 200:
                print("Request successful!")
                print("Response:", response.json())
        
            else:
                print("Request failed with status code:", response.status_code)
                print("Response:", response.text)
            
