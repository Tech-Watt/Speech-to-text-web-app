import streamlit as st
import time 
import speech_recognition as sr
import playsound
import pyttsx3

# defining some global varibles
global pause_rate
global option
global start_button
global stop_button
global text
global gender
global audio_name

# Speech to text function
def take_commands(pause_rate):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        st.write('Listening')
        print('Listening')
        r.pause_threshold = pause_rate 
        audio = r.listen(source)
        try:
            st.write("PROCESSING VOICE")
            coundownrec(101)
            # for listening the command in indian english
            Query = r.recognize_google(audio, language='en-in')
            # print("the query is printed='", Query, "'")
            st.write(Query)
        except Exception as e:
            st.write('"Restart again and make sure you have strong internet connection"')
            return "None"     
    return Query

# Text to speech function
def Speak(audio,gender,speed,audio_name):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[gender].id)
    engine.setProperty('rate',speed)
    engine.say(audio)
    if audio_name.endswith('3'):
        engine.save_to_file(audio,audio_name)
    engine.runAndWait()
def coundownrec(t):
    st.write('Processing percentage')
    countbar = st.progress(0)
    for i in range(t):
        countbar.progress(i)
        time.sleep(0.01)


# count down function
def coundown(t):
    st.write('Start After Count Down Bar Is Full',)
    countbar = st.progress(0)
    for i in range(t):
        countbar.progress(i)
        time.sleep(0.01)
    
# Streamlit app
with st.sidebar:
    st.title('Speech To Text And Text To Speech App')
    st.image('app_files\speeckimage.png')
    option = st.radio('Options',['Speech to Text',"Text to Speech"])
    start_button = st.button('Start')
    stop_button = st.button('Stop')
if stop_button:
    st.write('')

# For speech to text
if option == 'Speech to Text':
    st.write('Speech to text requires internet connection')
    pause_rate = st.number_input('Pause Rate',0.5,1.0)
    if start_button:
        coundown(101)
        take_commands(pause_rate)

# For text to speech
if option == 'Text to Speech':
    gender = st.radio('VOICE TO READ',['Male','Female'])
    save  = st.radio('SAVE TEXT AS AUDIO',['Yes','No'])
    if save == 'Yes':
        audio_name = st.text_input('Audio Name',placeholder='save file as:')
        audio_name = audio_name+'.mp3'
    else:audio_name = ''
    print(audio_name)
    speed = st.number_input('Reading Speed',90,200)
    if gender == 'Male':
        gender = 0
    elif gender == "Female":
        gender = 1
    else: gender =0        
    text = st.text_area('Text Input',placeholder='Type or paste your text here and click start')
    if start_button:
        coundown(101)
        st.title('Output Text')
        st.write(text)
        Speak(text,gender,speed,audio_name)
       

          
        
        
   
















 
