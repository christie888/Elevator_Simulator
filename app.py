from flask import Flask,request, jsonify
import random
import time


app = Flask(__name__)

current_position=random.randint(-2, 3)
#position=[]

@app.route('/')
def hello_world():
    position= random.randint(-2, 3)
    return "current place:"+str(position)


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
def create_article():
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

    return request.get_data()

    #return str(current_position)

    #if not request.json or not 'title' in request.json:

    #articles.append(article)
    #return jsonify({'article': article}), 201

#@app.route('/start')
#def start():


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
