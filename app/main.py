import pyautogui as pya
from scripts.writer import output_chunks
from scripts.prompts import prompt_chunks

pya.click(1025, 845)  # first click changes to GPT screen
pya.sleep(1)
pya.click(1025, 845)  # second click activates writting bar

prompt = prompt_chunks()

# pre-typing prompt:
pya.typewrite(prompt, interval=0.02)
pya.sleep(1)
pya.press('enter')
pya.sleep(2)

chunks = output_chunks()

for chunk in chunks:
    pya.typewrite(chunk, interval=0.005)
    pya.sleep(1)
    pya.press('enter')

# post-typing prompt:
pya.typewrite("end-of-prompt:  ")
