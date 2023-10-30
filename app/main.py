import pyautogui as pya
from scripts.writer import output_chunks

pya.click(1025, 845)
pya.sleep(1)
pya.click(1025, 845)

chunks = output_chunks()

for chunk in chunks:
    # chunk = chunk.replace('\n', '\t\n')  # Replace line breaks with "Shift + Enter" (Tab + Enter)
    pya.typewrite(chunk, interval=0.02)
    pya.sleep(2)
    pya.press('enter')


    # pya.click(1402, 844) 
    # pya.click(1025, 845) # submit button



