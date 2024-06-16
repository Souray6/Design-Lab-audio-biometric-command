# Design-Lab-audio-biometric-command

The audio-based biometry / security and command prompt project was a team project done by Atash, Sumajit, Kowshik, Shreekrishna and myself.

The idea of the project is as follows. We have a certain security vault / command box which can only be operated by authorized users (Here, the 5 of us) to execute certain tasks. We have to ensure that

i. Only the 5 of us can operate the box and none other
ii. The audio commands spoken by us are executed properly.

It is divided into 3 modules:

1. The ML-Model,  which extracts the spectral features (MFCC) of each user, collected from 5 audio samples each, and makes the Gaussian Mixture Model (GMM). To predict who the current speaker is, the model calculates the maximum likelihood score for the audio to be tested against each of the classes, the maximum score being the winner. However, if it does not clear a particular threshold of similarity, the speaker is discarded as foreign.

2. The Interface: An interactive interface with pygame has been designed so when the speaker speaks, the audio waveform is visible. This frontend application then connects with the backend which returns the verdict.

3. Server-Backend: This contains the pretrained GMM model with all the users' data. Once a new audio is received, it tries to match it to one of the classes by computing the maximum likelihood score. Thereafter, the verdict as calculated from (1) is sent back to the interface (2) and if access is granted, the command executes.

This section also contains the command palette. If access is granted, the user can now speak a command which is converted to text by inbuilt APIs. Thereafter, this sentence is matched either verbatim or keyword wise, to execute the command. Eg. If the user speaks "open google chrome", the function which starts the google chrome process is invoked from the CLI of Windows OS itself. Thereafter, the user can work on it normally, since controlling an application or navigating a browser entirely by audio is very difficult. Similarly "close google chrome" kills the process if it is running. Functions to play music or open/close inbuilt applications also exist. Finally, using "go to" and "backtrack" commands, we can entirely navigate all directories of the computer through audio alone - as long as the folders are recognizable English words. This gives the user maximum usability of the audio based command interface.
