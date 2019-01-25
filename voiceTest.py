#File: voiceTest.py

import speech_recognition as sr

def listen(x):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.pause_threshold = x
		r.non_speaking_duration = x
		r.adjust_for_ambient_noise(source, duration = x)
		audio = r.listen(source)
	try:
		command = r.recognize_google(audio)
	#Loops until something is understood
	except sr.UnknownValueError:
		command = listen(x)
	return command

def get_Command():
        while True:
                print("Say 'move'")
                keycheck = listen(0.7)
                keyphrase = keycheck.split()
                #change test word here 
                if "move" in keyphrase:
                        print("Yell at me!")
                        command = listen(0.4)
                        break
   

def main():
    command = get_Command()
    print("Got it!")
    
main()
