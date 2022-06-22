from datetime import datetime

def logWriter(dogadjaj, componentName):
    moment = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('C:/Users/Nemanja/Desktop/SonarQube/sonar-scanner-4.7.0.2747-windows/bin/TIM-6-RES-2022/Logger/Log.txt', 'a') as log:
        log.write(str(moment))
        log.write(' ')
        log.write(componentName)
        log.write(' :  ')
        log.write(dogadjaj)
        log.write('\n')

        log.close()
        pass