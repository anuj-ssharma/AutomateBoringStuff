import time

#Display the program's instructions
print "Press Enter to begin. Afterwards, press Enter to click the stopwatch. Press Ctrl-C to quit"

raw_input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

#TODO Start tracking the lap times

try:
    while True:
        raw_input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time() - startTime,2)
        print 'Lap #%s: %s (%s)' %(lapNum,totalTime,lapTime)
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print "\nDone"