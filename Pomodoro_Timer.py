import time

def pomodoro_timer():
    work_duration = 25 * 60  # 25 minutes in seconds
    break_duration = 5 * 60  # 5 minutes in seconds

    while True:
        print("Work for 25 minutes")
        time.sleep(work_duration)

        print("Take a 5-minute break")
        time.sleep(break_duration)

pomodoro_timer()
