import pyttsx3
import time
import schedule
from win10toast import ToastNotifier

# start pyttsx3 moduleprint("hello
sara = pyttsx3.init()
# choose the voice i want
v = sara.getProperty('voices')
sara.setProperty('voice', v[1].id)

# function to control the rate of saying it


def R(r):
	rate = sara.getProperty('rate')
	sara.setProperty('rate', rate - r)

# function to control the volume sound of saying it


def xo(o):
	volume = sara.getProperty('volume')
	sara.setProperty('volume', volume - o)


T = ToastNotifier()


# function that write messages

def code():
	T.show_toast("Hey", 'Code Time', threaded=True, icon_path=None, duration=3)
	R(123)
	xo(0.89)
	sara.say("Code Time")
	sara.runAndWait()

# the first parameters u can change it to make it say what u want
def code2():
	T.show_toast("Hey", 'CODE CODE CODE CODE!', threaded=True, icon_path=None, duration=3)
	R(123)
	xo(0.89)
	sara.say("CODE CODE CODE CODE!")
	sara.runAndWait()


def timie():
	T.show_toast("Hey", "أذكار الصباح", threaded=True, icon_path=None, duration=3)


def timie2():
	T.show_toast("Hey", "أذكار المساء", threaded=True, icon_path=None, duration=3)


def bed_time():
	T.show_toast("Hey", "Bed Time", threaded=True, icon_path=None, duration=3)
	R(123)
	xo(0.89)
	sara.say("Bed Time")
	sara.runAndWait()


def workout():
	T.show_toast("Hey", "It is Workout time BEAST!", threaded=True, icon_path=None, duration=3)
	R(123)
	xo(0.89)
	sara.say("It is Workout time BEAST!")
	sara.runAndWait()


def fri():
	T.show_toast("Hey", "صلاة الجمعة", threaded=True, icon_path=None, duration=10)


# schedule module, change time for another time and in the do function do the function u want to excute at that time
schedule.every().day.at("15:10").do(code)

schedule.every(20).minutes.do(code2)

schedule.every().day.at("05:36").do(timie)

schedule.every().day.at("16:16").do(timie2)

schedule.every().day.at("23:00").do(workout)

schedule.every().day.at("06:30").do(bed_time)

schedule.every().friday.at("12:30").do(fri)

sara.runAndWait()

while T.notification_active():
	time.sleep(0.1)

# Loop so that the scheduling task keep on running all the time.
while True:
	# Check whatever is schedule task is pending to run or not every 1 sec.
	schedule.run_pending()
	time.sleep(1)
