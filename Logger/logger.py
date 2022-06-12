from datetime import datetime

def logWriter(dogadjaj, componentName):
    moment = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('Log.txt', 'a') as log:
        log.write(str(moment))
        log.write(' ')
        log.write(componentName)
        log.write(' :  ')
        log.write(dogadjaj)
        log.write('\n')

        log.close()
        pass

#logWriter('Uradio sam nesto ne znam sta')

logWriter("Uradio sam nesto ne znam sta", "READER")