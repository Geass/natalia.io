import time
import datetime


def countdown(stop):
    while True:
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            print("Już pora skarbek")
            break
        print('Zostało jeszcze: '
              + str(difference.days) + " dni "
              + str(count_hours) + " godzin "
              + str(count_minutes) + " minut "
              + str(count_seconds) + " sekund"
              )
        time.sleep(1)


end_time = datetime.datetime(2021, 9, 1, 12, 0, 0)
countdown(end_time)
