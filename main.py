
from pydoc import text
from google import genai
import os
import sounddevice as sd
from scipy.io.wavfile import write
import AppOpener as ao
import mss
from recognition.recognition1 import recognize_speech
from speak.speaking import speaking
from AI_integration.gemini_api import AI_response_text
from conversion_history.conversation import User_Conversation



conversation = User_Conversation()     

while(True): 
    print("Listening for 'Hey Jarvis'...")
    
    try:      

       
        command = recognize_speech(6)
        
        
        
        if("jarvis" in command.lower()):
            speaking("Hey Tanmay, I am your AI voice assistant. How can I help you ?")
 
            break
            
            
    
        
    except Exception as e :
        print(str(e))
        continue
                

while(True):
    # Recording

    main_command = recognize_speech(30)

        
        
    if((main_command.lower() == "exit") or (main_command.lower() == "end communication") or (main_command.lower() == "goodbye" or main_command.lower() == "good bye") or (main_command.lower() == "bye")):
        speaking("Thank you for your valuable time. See you soon ......")
        break
    
    elif("open" in main_command.lower()):
        app_name = main_command.lower().replace("open", "").strip()
        
        print(f"Opening {app_name}...")
        
        speaking(f"Opening {app_name}...")
        if(os.path.exists(f"{app_name}.exe") or os.path.isfile(app_name)):
            ao.open(f"{app_name}.exe")
            
        else:
            print(f"Application '{app_name}' not found.")
            speaking(f"Application '{app_name}' not found. Please give me the correct name of the application.")

# Gemini AI Integration

    elif(("search" in main_command.lower()) or ("find" in main_command.lower()) or ("look for" in main_command.lower()) or ("what" in main_command.lower()) or ("who" in main_command.lower()) or ("tell me about" in main_command.lower()) or ("information" in main_command.lower()) or ("details" in main_command.lower()) or ("where" in main_command.lower()) or ("when" in main_command.lower()) or ("how" in main_command.lower()) or ("why" in main_command.lower()) or ("whome" in main_command.lower()) or ("which" in main_command.lower()) or ("give me" in main_command.lower()) or ("show me" in main_command.lower()) or ("explain" in main_command.lower()) or ("describe" in main_command.lower()) or ("define" in main_command.lower()) or ("list" in main_command.lower()) or ("compare" in main_command.lower()) or ("analyze" in main_command.lower()) or ("summarize" in main_command.lower())):
        
        
        full_history = conversation.get()
        history = full_history[-5:]  # Get the last 5 entries from the history

        # Ask Gemini about it
        
        TEXT = AI_response_text(f"{main_command}. If you want past prompt history, use this: {history}")
        speaking(TEXT)
        print(TEXT)
        conversation.add(main_command)
        conversation.save()
        
    elif("screenshare" in main_command.lower() or "screen share" in main_command.lower() or ("share" in main_command.lower() and "screen" in main_command.lower())):
        

        speaking("Starting screen sharing...")
        
        while True:
        # Store output in a variable
            screen_command = recognize_speech(30)
            
            
            with mss.MSS() as sct:
                sct.shot(output="screen.png")

            # Upload the screenshot
            client = genai.Client(api_key="AQ.Ab8RN6I6eblupH2zFn68SNBF0Z854_HoIlkmBFUoCWVnAc3hGw")
            uploaded_file = client.files.upload(file="screen.png")

            # Ask Gemini about it
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[
                    uploaded_file,
                    f"Describe in short: {screen_command}"
                ]
            )

            print(response.text)
            os.remove("screen.png")

            speaking(response.text.replace("**", "").replace("*", "")  )
            
            if(("stop" in screen_command.lower()) or ("end" in screen_command.lower()) or ("exit" in screen_command.lower()) or ("quit" in screen_command.lower())):
                speaking("Stopping screen sharing...")
                break