# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 23:37:13 2022

Program creates interface to observe standing waves based on standing wave 
equation. Interface assumes only legal answers will be submitted.

@author: linh
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim 

x = np.linspace(0, 10, 1000) 
fig = plt.figure() 
subplot = plt.axes(xlim=(0, 10), xlabel=("x"), ylim=(-2, 2), 
ylabel=("y")) 
line1, = subplot.plot([], [], lw=2) # standard wave
line2, = subplot.plot([], [], lw=2) # standard wave with the opposite angular 
                                    # frequency
line3, = subplot.plot([], [], lw=2) # superposition of the two previous waves  
lines = [line1, line2, line3]

DEFAULT_AMP = 1
DEFAULT_WAVE_NUM = np.pi/2
DEFAULT_ANG_FREQ = 2*np.pi

# values that will be put into the wave calculations
given_amp = DEFAULT_AMP
given_wave_num = DEFAULT_WAVE_NUM
given_ang_freq = DEFAULT_ANG_FREQ


def sineWave_y(position, time, amp, wave_num, ang_freq):
    return amp * (np.sin(wave_num*position - ang_freq*time))

def initialize():
    for i in range(len(lines)):
        lines[i].set_data([], []) 
    return lines
        
def animate(i):
    y1 = sineWave_y(x, 0.1*i, given_amp, given_wave_num, given_ang_freq)
    if len(lines) > 1:
        y2 = sineWave_y(x, 0.1*i, given_amp, given_wave_num, -given_ang_freq)
    if len(lines) == 3:
        y3 = y1+y2
        waveFunctions = [[x,y1],[x,y2],[x,y3]]
        
    if len(lines) == 1:
        waveFunctions = [[x,y1]]
    elif len(lines) == 2:
        waveFunctions = [[x,y1],[x,y2]]
                         
    for i in range(len(lines)):
        lines[i].set_data(waveFunctions[i][0], waveFunctions[i][1])
        
    return lines

def gen_animation():
    animation = anim.FuncAnimation(fig, animate, init_func=initialize, 
                               frames=200, interval=20, blit=True) 
    return animation
    
def main():
    end_program = False
    while not(end_program):
        print("Default wave values: \nAmplitude = 1\nWave Number = pi/2")
        print("Angular Frequency = 2pi")
        print("Graph will show standing waves with default angular frequency,",
              "opposite angular frequency and superposition of both waves.")
        print("Guide:\nBlue line = Standing wave with given angular frequency",
              "\nOrange Line = Standing wave with opposite angular frequency",
              "\nGreen Line = Superposition wave")
        response = input("Show default value animation(y/n)? ")
        if response == "n":
            given_amp = float(input("Wave amplitude: "))
            given_ang_freq = float(input("Angular Frequency: "))
            given_wave_num = float(input("Wave number: "))
        response = input("Show all 3 waves? y/n")
        if response == "n":
            lines = [line1]
            if input("Show wave with negative angular frequency(y/n)? ") == "y":
                lines = lines + [line2]
                if input("Show wave with superposition(y/n)? ") == "y":
                    lines = lines + [line3]
        animation = gen_animation()
        plt.show()
        response = input("Continue generating standing waves(y/n)? ")
        if response == "y":
            given_amp = DEFAULT_AMP
            given_ang_freq = DEFAULT_ANG_FREQ
            given_wave_num = DEFAULT_WAVE_NUM
        else:
            end_program = True
    return 0

main()


    