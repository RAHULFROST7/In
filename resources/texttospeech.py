import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init('sapi5')

# Set the desired voice (you can use an index or the voice's ID)
voices = engine.getProperty('voices')
engine.setProperty('rate', 160)
engine.setProperty('pitch',0)
engine.setProperty('voice', voices[1].id)

# Convert text to speech
engine.say(" Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms and statistical models that enable computers to automatically improve their performance on a specific task, based on experience or data.In other words, machine learning algorithms are designed to analyze and learn from data, and then use this knowledge to make predictions or decisions about new data. This can include tasks like image recognition, natural language processing, speech recognition, and predictive analytics.")

# Play the speech
engine.runAndWait()
