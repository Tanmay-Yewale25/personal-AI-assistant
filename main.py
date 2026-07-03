
from pydoc import text
from tkinter import Image
from google import genai
import os
from scipy.io.wavfile import write
import AppOpener as ao
import mss
from recognition.recognition1 import recognize_speech
from speak.speaking import speaking
from AI_integration.gemini_api import AI_response_text
from conversion_history.conversation import User_Conversation
from Automation.mouse import Mouse
from Automation.window import Window
from PIL import Image
from App_opening.app_list import app_list
from Automation.keyboard import keyboard
from datetime import datetime

mouse = Mouse()
conversation = User_Conversation()     
window_act =Window()
key = keyboard()

client = genai.Client(api_key="AQ.Ab8RN6IMS0fUPyOMMk0N_6VaKU1nmvsbG80FDfTPCYFs6RtG5w")


while(True): 
    print("Listening for 'Hey Jarvis'...")
    
    try:      

       
        command = recognize_speech(6)
        if(command is None):
            continue
        
        
        
        if("jarvis" in command.lower()):
            speaking("Hey Tanmay, I am your AI voice assistant. How can I help you ?")
 
            break
            
            
    
        
    except Exception as e :
        print(str(e))
        continue
                

while(True):
    # Recording

    main_command = recognize_speech(30)
    if(main_command is None):
        continue

        
        
    if((main_command.lower() == "exit") or (main_command.lower() == "end communication") or (main_command.lower() == "goodbye" or main_command.lower() == "good bye") or (main_command.lower() == "bye") or (main_command.lower() == "quit") or (main_command.lower() == "stop") or (main_command.lower() == "terminate") or (main_command.lower() == "close") or (main_command.lower() == "close communication") or (main_command.lower() == "close conversation") or (main_command.lower() == "close chat") or (main_command.lower() == "close session") or (main_command.lower() == "end session") or (main_command.lower() == "end chat") or (main_command.lower() == "quit conversation") or (main_command.lower() == "quit chat") or (main_command.lower() == "quit session") or (main_command.lower() == "terminate conversation") or (main_command.lower() == "terminate chat") or (main_command.lower() == "terminate session")):
        speaking("Thank you for your valuable time. See you soon ......")
        break
    
    # elif("open" in main_command.lower()):
    #     app_name = main_command.lower().replace("open", "").strip()
        
    #     print(f"Opening {app_name}...")
        
    #     speaking(f"Opening {app_name}...")
    #     if(os.path.exists(f"{app_name}.exe") or os.path.isfile(app_name)):
    #         ao.open(f"{app_name}.exe")
            
    #     else:
    #         print(f"Application '{app_name}' not found.")
    #         speaking(f"Application '{app_name}' not found. Please give me the correct name of the application.")

# Gemini AI Integration

    elif(("search" in main_command.lower()) or ("find" in main_command.lower()) or ("look for" in main_command.lower()) or ("what" in main_command.lower()) or ("who" in main_command.lower()) or ("tell me about" in main_command.lower()) or ("information" in main_command.lower()) or ("details" in main_command.lower()) or ("where" in main_command.lower()) or ("when" in main_command.lower()) or ("how" in main_command.lower()) or ("why" in main_command.lower()) or ("whome" in main_command.lower()) or ("which" in main_command.lower()) or ("give me" in main_command.lower()) or ("show me" in main_command.lower()) or ("explain" in main_command.lower()) or ("describe" in main_command.lower()) or ("define" in main_command.lower()) or ("list" in main_command.lower()) or ("compare" in main_command.lower()) or ("analyze" in main_command.lower()) or ("summarize" in main_command.lower())):
        
        
        full_history = conversation.get()
        history = full_history[-5:]  # Get the last 5 entries from the history

        # Ask Gemini about it
        
        TEXT = AI_response_text(f"{main_command}. If you want past prompt history, use this: {history}").replace("**", "").replace("*", "")
        speaking(TEXT)
        print(TEXT)
        conversation.add(main_command)
        conversation.save()
        
    elif("screenshare" in main_command.lower() or "screen share" in main_command.lower() or ("share" in main_command.lower() and "screen" in main_command.lower())):
        

        speaking("Starting screen sharing...")
        
        while True:
        # Store output in a variable
            screen_command = recognize_speech(50)
            if(screen_command is None):
                continue
            
            if(("stop" in screen_command.lower()) or ("end" in screen_command.lower()) or ("exit" in screen_command.lower()) or ("quit" in screen_command.lower())):
                speaking("Stopping screen sharing...")
                break
            
            if os.path.exists("screen.png"):    
                os.remove("screen.png")
            
            
            with mss.MSS() as sct:
                sct.shot(output="screen.png")

            # Upload the screenshot
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
            
            
            
    elif("automate" in main_command.lower() or "automation" in main_command.lower() or "automate my work" in main_command.lower() or "automate my tasks" in main_command.lower()):
        speaking("Starting automation...")
        
        while True:
            try:
            # Store output in a variable
                automate_command = recognize_speech(40)
                if(automate_command is None):
                    continue
                
                def coords():
                    with mss.MSS() as sct:
                        sct.shot(output="automate_screen.png")
                    # Ask Gemini about it
                    

                    image = Image.open("automate_screen.png")

                    # Ask Gemini about it
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[
                            image,
                            f"I give you screenshot and user command as : {automate_command}. give me coordinates of mouse click. If user want to select any text then give me starting and ending coordinates, my screen size is Screen Width: 1920 and Screen Height: 1080. Note that give me only coordinates seperated by comma not any another text beacuse i will get as it is from your response.If you have to give me text selection coordinates then give me in this format : start_x,start_y,end_x,end_y"
                        ]
                    )
                    return response.text
                
                
                if(("stop" in automate_command.lower()) or ("end" in automate_command.lower()) or ("exit" in automate_command.lower()) or ("quit" in automate_command.lower())):
                    speaking("Stopping automation...")
                    break
                
                elif("click" in automate_command.lower()):
                    # Extract coordinates from the AI response
                    coordinates = coords().split(',')
                    if len(coordinates) == 2:
                        x, y = map(int, coordinates)
                        mouse.click(x, y)
                        
                    os.remove("automate_screen.png")
                        
                elif("select" in automate_command.lower() or "copy" in automate_command.lower()):
                    # Extract coordinates from the AI response
                    coordinates = coords().split(',')
                    if len(coordinates) == 4:
                        start_x, start_y, end_x, end_y = map(int, coordinates)
                        mouse.copy_text(start_x, start_y, end_x, end_y)
                        
                    os.remove("automate_screen.png")
                        
                
                elif("scroll up" == automate_command.lower()):
                    mouse.scroll(400)  # Scroll up
                elif("scroll down" == automate_command.lower()):
                    mouse.scroll(-400)  # Scroll down
                    
                    
                elif(("close window" in automate_command.lower() and "current" in automate_command.lower()) or ("close" in automate_command.lower() and "current" in automate_command.lower() and "window" in automate_command.lower()) or ("close" in automate_command.lower() and "active" in automate_command.lower() and "window" in automate_command.lower())or("close" in automate_command.lower() and "application" in automate_command.lower() and "current" in automate_command.lower()) or ("close" in automate_command.lower() and "application" in automate_command.lower() and "active" in automate_command.lower())):
                    speaking("Closing current window...")
                    window_act.close_window()

                
                elif(("minimise window" in automate_command.lower() and "current" in automate_command.lower()) or (("minimise" in automate_command.lower() or "minimize" in automate_command.lower()) and "current" in automate_command.lower() and "window" in automate_command.lower()) or (("minimize" in automate_command.lower() or "minimise" in automate_command.lower()) and "active" in automate_command.lower() and "window" in automate_command.lower())or(("minimize" in automate_command.lower() or "minimise" in automate_command.lower()) and "application" in automate_command.lower() and "current" in automate_command.lower()) or ("minimize" in automate_command.lower() and "application" in automate_command.lower() and "active" in automate_command.lower())):
                    speaking("Minimizing current window...")
                    window_act.minimize_window()
                    
                elif(("open" in automate_command.lower() and "window" in automate_command.lower()) or ("open" in automate_command.lower() and "application" in automate_command.lower()) or ("open" in automate_command.lower())):
                    app_name = automate_command.lower().replace("open", "").replace("window", "").replace("application", "").strip()
                    apps = app_list()
                    for app in apps:
                        if app_name.lower() in app.lower():
                            speaking(f"Opening {app}...")
                            ao.open(app)
                            break
                        
                elif(("close" in automate_command.lower() and "window" in automate_command.lower()) or ("close" in automate_command.lower() and "application" in automate_command.lower()) or ("close" in automate_command.lower())):
                    app_name = automate_command.lower().replace("close", "").replace("window", "").replace("application", "").strip()
                    apps = app_list()
                    for app in apps:
                        if app_name.lower() in app.lower():
                            speaking(f"Closing {app}...")
                            window_act.close_window(app)
                            break
                    
                elif(("maximize" in automate_command.lower()) or ("maximize" in automate_command.lower() and "window" in automate_command.lower()) or ("maximize" in automate_command.lower() and "application" in automate_command.lower())):
                    app = automate_command.lower().replace("maximize", "").replace("window", "").replace("application", "").strip()
                    speaking(f"Maximizing {app}...")
                    window_act.maximize_window(app)
                    
                elif((automate_command.lower() == "next") or (automate_command.lower() == "next picture") or (automate_command.lower() == "next photo") or (automate_command.lower() == "next image") or (automate_command.lower() == "next slide") or (automate_command.lower() == "next window") or (automate_command.lower() == "switch window") or (automate_command.lower() == "switch to next window") or(automate_command.lower() == "skip") ):
                    key.next()
                    print("Next window or slide or image or picture or photo or next command executed.")
                    
                elif((automate_command.lower() == "previous") or (automate_command.lower() == "previous picture") or (automate_command.lower() == "previous photo") or (automate_command.lower() == "previous image") or (automate_command.lower() == "previous slide") or (automate_command.lower() == "switch to previous window") or (automate_command.lower() == "switch to last window") or (automate_command.lower() == "last window") ):
                    key.previous()
                    print("Previous window or slide or image or picture or photo or previous command executed.")
                    
                elif(("multitasking" in automate_command.lower() or "multitask" in automate_command.lower() or "multi tasking" in automate_command.lower()) and ("2" in automate_command.lower() or "two" in automate_command.lower() or "2nd" in automate_command.lower() or "second" in automate_command.lower() or "to" in automate_command.lower() or "too" in automate_command.lower())):
                    key.multitasking_2()
                    print("Multitasking 2 command executed.")
                    
                elif(("multitasking" in automate_command.lower() or "multitask" in automate_command.lower() or "multi tasking" in automate_command.lower()) and ("3" in automate_command.lower() or "three" in automate_command.lower() or "3rd" in automate_command.lower() or "third" in automate_command.lower())):
                    key.multitasking_3()
                    print("Multitasking 3 command executed.")
                    
                elif(("multitasking" in automate_command.lower() or "multitask" in automate_command.lower() or "multi tasking" in automate_command.lower()) and ("4" in automate_command.lower() or "four" in automate_command.lower() or "4th" in automate_command.lower() or "fourth" in automate_command.lower())):
                    key.multitasking_4()
                    print("Multitasking 4 command executed.")
                    
                elif(("enter" in automate_command.lower() and "key" in automate_command.lower()) or ("enter" in automate_command.lower() and "button" in automate_command.lower()) or ("enter" in automate_command.lower() and "press" in automate_command.lower()) or ("enter" in automate_command.lower() and "hit" in automate_command.lower()) or ("enter" in automate_command.lower() and "click" in automate_command.lower()) or ("enter" in automate_command.lower())):
                    key.enter()
                    print("Enter key command executed.")
                    
                elif(("time" in automate_command.lower() and "now" in automate_command.lower()) or ("current time" in automate_command.lower()) or ("what is the time" in automate_command.lower()) or ("what's the time" in automate_command.lower()) or ("tell me the time" in automate_command.lower()) or ("show me the time" in automate_command.lower())):
                    
                    now = datetime.now()
                    current_time = now.strftime("%H:%M")
                    speaking(f"The current time is {current_time}.")
                    print(f"The current time is {current_time}.")

            except Exception as e:
                print(str(e))
                if os.path.exists("automate_screen.png"):
                    os.remove("automate_screen.png")
                continue
