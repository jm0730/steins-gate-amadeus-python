import speech_recognition as sr
import webbrowser
from amadeuslogin import amadeus_login
from playsound import playsound
def amadeus_command(a, f):
    print(a)
    playsound(f)
amadeus_login()
print('연결중...')
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('한국어로 말하세요.')
        audio = r.listen(source)
    try:
        print("당신은 말했습니다." + r.recognize_google(audio, language="ko-KR"))
        if '안녕' in r.recognize_google(audio, language="ko-KR"):
            amadeus_command('안녕하세요.', '.\\voice\\hello.wav')
        elif '무엇을 할 수 있' in r.recognize_google(audio, language="ko-KR"):
            amadeus_command('모든 커맨드를 보시려면 \nhttps://download.amadeuspython.ml/command.html을 참조해 주세요.', 'command.wav')
        elif '도움' in r.recognize_google(audio, language="ko-KR"):
            amadeus_command('도움말은 이쪽입니다.\nhttps://download.amadeuspython.ml/help.html', '.\\voice\\help.wav')
        elif '너의 이름' in r.recognize_google(audio, language="ko-KR"):
            amadeus_command('제 이름은 유즈리 유카리입니다.', '.\\voice\\name.wav')
    except sr.UnknownValueError:
        print("질문을 이해할 수 없습니다.")
        playsound('nounderstand.wav.')
        
