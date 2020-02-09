#!/usr/bin/env python
from flask import Flask, request, jsonify
import random
import time

app = Flask(__name__)

current_position=random.randint(-2, 3)

@app.route('/')
def current_place():
    position = random.randint(-2, 3)
    return  jsonify({"current place": str(position)}), 200

def MoveOD(current_position, destination):
    if current_position==destination:
        wai_time=0
    else:
        if destination*current_position>0:
            distance =abs(destination-current_position)
        else:
            distance=abs(destination-current_position)-1
        T_moving=5
        wai_time=distance*T_moving

    print("move from: ", current_position, "to: ", destination, "; waiting time: ",wai_time)

    while destination!=current_position:
        print("current position:", current_position, "destination:", destination)
        time.sleep(T_moving)
        if destination>current_position:
            current_position+=1
        else:
            current_position-=1

    return current_position

@app.route('/destination', methods=['POST'])
def move():
    global current_position
    print("current place:" + str(current_position))

    dep=request.json['departure']
    des=request.json['destination']

    print("departure, destination", str(dep), str(des))

    current_position= MoveOD(current_position, dep)

    if current_position==dep:
        print("arrived at departure floor: ",dep)

    current_position= MoveOD(current_position, des)

    if current_position==des:
        print("arrived at destination floor: ",des)

    return request.get_data(), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
