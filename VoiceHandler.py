from voicevox import Client
import json
import sounddevice as sd 
import numpy as np
import requests
from termcolor import colored
#Taken straight from the documenation..
class Audio_System():
      def __init__ (self):
            self.host = "127.0.0.1"
            self.port = "50021"
            self.speaker =  "0"

      def post_audio_query(self,text: str) -> dict:
            self.params = {"text": text, "speaker": self.speaker}

            self.res = requests.post(
        f"http://{self.host}:{self.port}/audio_query",
        params=self.params,
    )

            self.query_data = self.res.json()
    # query_data["speedScale"] = 1.5

    # print(query_data)

            return self.query_data
      

      def post_synthesis(self,query_data: dict) -> bytes:
    # 音声合成を実行する
            self.params = {"speaker": self.speaker}
            self.headers = {"content-type": "application/json"}

            self.res = requests.post(
            f"http://{self.host}:{self.port}/synthesis",
            data=json.dumps(query_data),
            params=self.params,
            headers=self.headers,
    )

            return self.res.content
      
      def play_wavfile(self,wav_data: bytes):
    # 音声を再生する
            self.sample_rate = 24000  # サンプリングレート
            self.wav_array = np.frombuffer(wav_data, dtype=np.int16)  # バイトデータをnumpy配列に変換
            sd.play(self.wav_array, self.sample_rate, blocking=True)  # 音声の再生

      def text_to_voice(self,text):
            while True:
                  if text == "q":
                        break

                  self.res = self.post_audio_query(text)
                  self.wav = self.post_synthesis(self.res)
                  print(colored("Playing Audio File","green"))
                  self.play_wavfile(self.wav)
                  break
