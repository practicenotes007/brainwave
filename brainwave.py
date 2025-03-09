import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound

class Brainwave:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        # self.recognizer.energy_threshold = 100

    def record_audio(self):
        """
        录制语音
        """
        with sr.Microphone() as source:
            print("请说话...")
            try:
                # 设置 phrase_time_limit 为 10 秒，即最多录制 10 秒
                audio = self.recognizer.listen(source, phrase_time_limit=30)
            except sr.WaitTimeoutError:
                print("等待语音输入超时")
                return None
        return audio

    def speech_to_text(self, audio):
        """
        语音识别为文本
        """
        try:
            text = self.recognizer.recognize_google(audio, language='zh-CN')
            print(f"识别结果: {text}")
            return text
        except sr.UnknownValueError:
            print("无法识别语音")
        except sr.RequestError as e:
            print(f"请求错误; {e}")
        return None

    def text_to_speech(self, text):
        """
        文本转换为语音并播放
        """
        print("开始输出声音...")
        tts = gTTS(text=text, lang='zh-CN')
        tts.save("output.mp3")
        playsound("output.mp3")
        os.remove("output.mp3")
        print("结束，清理临时文件...")

    def run(self):
        """
        运行语音转换工具
        """
        while True:
            audio = self.record_audio()
            print("开始转换...call->speech_to_text")
            text = self.speech_to_text(audio)
            if text:
                self.text_to_speech(text)

            # 询问用户是否继续
            user_input = input("是否继续？(输入 'n' 退出，其他任意键继续): ")
            if user_input.lower() == 'n':
                break
if __name__ == "__main__":
    brainwave = Brainwave()
    brainwave.run()