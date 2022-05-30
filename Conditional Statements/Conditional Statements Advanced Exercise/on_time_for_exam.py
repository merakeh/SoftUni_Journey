
exam_hour = int(input())
exam_minutes = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())

exam_time_minutes = (exam_hour * 60) + exam_minutes
arrival_time_minutes = hour_arrival * 60 + minutes_arrival
difference_time = abs(exam_time_minutes - arrival_time_minutes)

if exam_time_minutes < arrival_time_minutes:
    print("Late")
    if difference_time >= 60:
        hour = difference_time // 60
        minutes = difference_time % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours after the start")
        else:
            print(f"{hour}:{minutes} hours after the start")
    else:
        print(f"{difference_time} minutes after the start")
elif exam_time_minutes == arrival_time_minutes or difference_time <= 30:
    print("On time")
    if 0 < difference_time <= 30:
        print(f"{difference_time} minutes before the start")
else:
    print("Early")
    if difference_time >= 60:
        hour = difference_time // 60
        minutes = difference_time % 60
        if minutes < 10:
            print(f"{hour}:0{minutes} hours before the start")
        else:
            print(f"{hour}:{minutes} hours before the start")
    else:
        print(f"{difference_time} minutes before the start")
