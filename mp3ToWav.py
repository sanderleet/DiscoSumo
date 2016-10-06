from pydub import AudioSegment
sound = AudioSegment.from_mp3("/home/sander/PycharmProjects/DiscoSumo/katse.mp3")
sound.export("/home/sander/PycharmProjects/DiscoSumo/test", format="wav")