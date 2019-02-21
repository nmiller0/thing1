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
                print("Say 'chess.'")
                keycheck = listen(0.1)
                keyphrase = keycheck.split()
                #change test word here 
                if "chess" in keyphrase:
                        print("Say a move.")
                        command = listen(.5)
                        print("I heard: ", command)
                        print("Is that correct?")
                        keycheck1 = listen(0.5)
                        keyphrase1 = keycheck1.split()
                        if "yes" in keyphrase1:
                                print("Move has been made!")
                                return command
                                break
def parseCommand(command):
    splitCommand = command.lower().split()
    print(splitCommand)

def main():
        command = get_Command()
        parseCommand(command)
        
main()

