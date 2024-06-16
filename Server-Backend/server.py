# server.py

import numpy as np
import wavio
from flask import Flask, request

from speaker_recognise import load_speaker_models, recognize_speaker
from audio_recognise import recognize_speech_from_wav

app = Flask(__name__)

# Path to training data
PATH = "D:\\ClassKGP\\Autumn23\\Design lab\\Test Model\\" 
modelpath = "speaker_models\\"
models, speakers = load_speaker_models(modelpath)

@app.route("/", methods=['POST'])
def authenticate_speaker():
    try:
        print("Request received. Being processed...\n")
        data = request.form.getlist('data')

        processed_data = (np.array(data).astype(np.float64)).reshape(-1, 2)
        wavio.write("test.wav", processed_data, 48000, sampwidth=2)
        

        speaker = recognize_speaker(models, speakers, PATH + "test.wav")
        print("\tdetected as - " + speaker)

        text = recognize_speech_from_wav(PATH + "test.wav")
        print("Speaker Told: ",text)
        # run_command(text)
        return {"message": speaker}
    except:
        return {"error": "Request must contain JSON data"}, 400

if __name__ == "__main__":
    print("\nServer Started... :)\n")
    app.run(host='0.0.0.0', port=5050, debug=True)
