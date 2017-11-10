hardlopen = open('hardlopers.txt', 'a')
import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %y")

nu = datetime.datetime.now()
t = nu.strftime('%H:%M:%S')


def nieuwe (loper):
    hardlopen.write(s + ' , ' + t + ' , ' + ' ' + loper + '\n')
nieuwe(input('Geef je naam: '))

hardlopen.close()
