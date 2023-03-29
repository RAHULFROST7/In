from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import soundcard as sc
import soundfile as sf
import numpy as np

options = Options()
#<---------Directing to default chrome proafile---------->
options.add_argument("user-data-dir=C:\\Users\\hp\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome (service=Service(ChromeDriverManager().install()),
options=options) 
driver.get("https://meet.google.com/dfr-sxzd-giq")
#<---------Clicking join now button in meet---------->
join_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Join now')]"))
)

# Click the "Join now" button
join_button.click()

OUTPUT_FILE_NAME = "out.wav"    # file name.
SAMPLE_RATE = 48000              # [Hz]. sampling rate.
DURATION = None                  # [sec]. duration recording audio.

with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
    # record audio with loopback from default speaker.
    frames = []
    while True:
        try:
            # find the element that contains the text
            element = driver.find_element(By.XPATH, "//*[contains(text(), 'Returning to home screen')]")

            # if the text is found, run your specific script here
            print("Text is found")
            # replace this with your own code to run your specific script
            break  # break the loop once the text is found
        except:
            pass  # do nothing if the text is not found yet
        # record audio and append the frames to a list
        frame = mic.record(numframes=None)
        frames.append(frame)
        if DURATION and sum(len(f) for f in frames) >= DURATION * SAMPLE_RATE:
            break
    # combine the frames into a single numpy array
    data = np.concatenate(frames, axis=0)
    # change "data=data[:, 0]" to "data=data", if you would like to write audio as multiple-channels.
    sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)