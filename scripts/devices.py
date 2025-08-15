import pyaudio

p = pyaudio.PyAudio()

devices = p.get_device_count()

for i in range(devices):
   device_info = p.get_device_info_by_index(i)
   if device_info.get('maxInputChannels') > 0:
      print(f"Microphone: {device_info.get('name')} , Device Index: {device_info.get('hostApi')}")