import time

def tick_tock(seconds):
    """
    simulates the sound of a clock by alternating printing 'tick' and 
    'tock' for every second that passes
    """
    while seconds > 0:
        print('tick...')
        seconds -= 1
        time.sleep(1)
        if seconds == 0:
            break
        print('tock...')
        seconds -= 1
        time.sleep(1)

tick_tock(7)

