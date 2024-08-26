import wave

obj = wave.open("audio.wav", "rb")
print("Number of channels: ", obj.getnchannels())
print("Sample width: ", obj.getsampwidth())
print("Frame rate: ", obj.getframerate())
print("Params: ", obj.getparams())
print("Number of frames: ", obj.getnframes())

time_audio = obj.getnframes() / obj.getframerate()
print("Time: ", time_audio)

frames = obj.readframes(-1)
print('frame:', frames)
print(type(frames), type(frames[0]))
print(len(frames)/2)

obj.close()

