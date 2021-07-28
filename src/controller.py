import time
import rtmidi
import mido
import keyboard
import json
import pyfiglet

banner = pyfiglet.figlet_format("Midi Controller")
exit_banner = pyfiglet.figlet_format("Goodbye in 3")

ports = mido.get_input_names()

outport = mido.open_output('testPort 1')
a_pressed = False

effects= {
    'distortion': False,
    'overdrive': False,
    'compression': False,
    'chorus': False,
    'flanger': False
}

# dist -> 0 -> d
# od -> 1 -> o
# compression -> 2 -> c
# chorus -> 3 -> x
# flanger -> 4 -> f

wait_time = 0.5

print(banner)
print("----------------------------------------------------------------")

while True:
    if keyboard.is_pressed("d"):
        if not effects['distortion']:
            effects['distortion'] = True
            msg = mido.Message("note_on", note=0, velocity=100, time=10)
            outport.send(msg)
            time.sleep(wait_time)
        elif effects['distortion']:
            effects['distortion'] = False
            msg = mido.Message("note_on", note=0, velocity=100, time=10)
            outport.send(msg)
            time.sleep(wait_time)
        print(json.dumps(effects, indent = 4))
    
    if keyboard.is_pressed("o"):
        if not effects['overdrive']:
            effects['overdrive'] = True
            msg = mido.Message("note_on", note=1, velocity=100, time=10)
            outport.send(msg)
            time.sleep(wait_time)
        elif effects['overdrive']:
            effects['overdrive'] = False
            msg = mido.Message("note_on", note=1, velocity=100, time=10)
            outport.send(msg)
            time.sleep(wait_time)

        print(json.dumps(effects, indent = 4))
    
    if keyboard.is_pressed("c"):
        if not effects['compression']:
            effects['compression'] = True
            msg = mido.Message("note_on", note=2, velocity=100, time=10)
            outport.send(msg)
            time.sleep(wait_time)
        elif effects['compression']:
            effects['compression'] = False
            msg = mido.Message("note_on", note=2, velocity=100, time=10)
            outport.send(msg)
            time.sleep(wait_time)

        print(json.dumps(effects, indent = 4))

    if keyboard.is_pressed("x"):
        if not effects['chorus']:
            effects['chorus'] = True
            msg = mido.Message("note_on", note=3, velocity=100, time=10)
            outport.send(msg)
            time.sleep(wait_time)
        elif effects['chorus']:
            effects['chorus'] = False
            msg = mido.Message("note_on", note=3, velocity=100, time=10)
            outport.send(msg)
            time.sleep(wait_time)

        print(json.dumps(effects, indent = 4))

    if keyboard.is_pressed("f"):
        if not effects['flanger']:
            effects['flanger'] = True
            msg = mido.Message("note_on", note=4, velocity=100, time=10)
            outport.send(msg)
            time.sleep(wait_time)
        elif effects['flanger']:
            effects['flanger'] = False
            msg = mido.Message("note_on", note=4, velocity=100, time=10)
            outport.send(msg)
            time.sleep(wait_time)

        print(json.dumps(effects, indent = 4))
        
    if keyboard.is_pressed("tab"):
        print(exit_banner)
        time.sleep(3)
        exit()
