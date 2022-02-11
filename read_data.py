import serial
import time
import keyboard

import csv
from datetime import datetime

BAUD_RATE = 115200

arduinoData = serial.Serial('com3', BAUD_RATE)

is_collecting = False
save_data = False
run = True
collect_current_data = True

count = 0
time.sleep(1)

header = ['Timestamp', 'Sensor_id_s', 'ax', 'ay', 'az', 'mx', 'my', 'mz', 'gx', 'gy', 'gz', 'Sensor_id_e']

while run:

    data_raw = []
    while collect_current_data:
        while (arduinoData.inWaiting() == 0):
            pass

        # detect key: c: collecting data. s: save
        if keyboard.is_pressed('c'):
            is_collecting = True
            save_data = False
        if keyboard.is_pressed('s'):
            is_collecting = False
            save_data = True

        # collect data
        if is_collecting:
            print('collecting')
            dataPacket = arduinoData.readline()
            dataPacket = str(dataPacket, 'utf-8')
            start = dataPacket.find("START")
            end = dataPacket.find("END")

            # only collect data in list when data is useful, i.e when data start with START
            if start != -1:  # start
                dataList = [time.time(), dataPacket[start+5]]
                dataPacket = dataPacket[start+7:end-1]
                dataList.extend(dataPacket.split(' '))
                dataList.append(dataList[1])
                print(dataList)
                timestamp = datetime.now()
                data_raw.append(dataList)



        # print(filename_csv)

        # save data
        if save_data:
            path = "data/straight_sample_{count}.csv".format(count=count)

            print(path)
            with open(path,'w',newline='') as csv_file:
                print(path)
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(header)
                for data in data_raw:
                    csv_writer.writerow(data)
                    print(data)
            save_data = False
            collect_current_data = False

            time.sleep(1)
    count += 1
    # collect next data sample
    collect_current_data = True

    if keyboard.is_pressed('z'):
        run = False



