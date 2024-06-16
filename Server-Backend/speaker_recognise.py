# speaker_recognition.py

import os
import numpy as np
import pickle
from scipy.io.wavfile import read
from speakerfeatures import extract_features

def load_speaker_models(modelpath):
    gmm_files = [os.path.join(modelpath, fname) for fname in os.listdir(modelpath) if fname.endswith('.gmm')]
    models = [pickle.load(open(fname, 'rb')) for fname in gmm_files]
    speakers = [fname.split("\\")[-1].split(".gmm")[0] for fname in gmm_files]
    return models, speakers

def recognize_speaker(models, speakers, audio_file):
    sr, audio = read(audio_file)
    vector = extract_features(audio, sr)
    log_likelihood = np.zeros(len(models)) 
    
    for i, gmm in enumerate(models):
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
    print(log_likelihood)  
    winner = np.argmax(log_likelihood)
    return speakers[winner]
