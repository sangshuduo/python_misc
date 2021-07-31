from time import sleep
from progress.spinner import MoonSpinner

with MoonSpinner('Processing…') as bar:
    for i in range(100):
        sleep(0.02)
        bar.next()
