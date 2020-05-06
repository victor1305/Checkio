from datetime import datetime
formato = "%H:%M"

def sun_angle(time):

   hhmm = datetime.strptime(time, formato)
   hours = hhmm.hour
   minut = hhmm.minute
   dayMinut = hours * 60 + minut

   if dayMinut >= 360 and dayMinut <= 1080:
       angle = (dayMinut - 360) * 0.25

       return angle

   else:

       return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
