# POSSIBLE TECHNIQUE TO GET CHUNKS
# End a chunk based on decibles... So if my voice is quiet or silent it will send a chunk.

#-#-# Possible Reuse Code #-#-#

# Can use the below code to make another webpage

# @app.route('/test/')
# def test():
#     return "Backend Test Service is Running"

# def transcribe_speech(audio_file):
#     client = speech.SpeechClient()
#     with io.open(audio_file, "rb") as audio:
#         content = audio.read()
#     audio = speech.RecognitionAudio(content=content)
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=16000,
#         language_code="en-US",
#     )
#     response = client.recognize(config=config, audio=audio)
#     for result in response.results:
#         print("Transcript: {}".format(result.alternatives[0].transcript))
#         return result.alternatives[0].transcript

# @app.route('/')
# def home():
#     return "Backend Service is Running"