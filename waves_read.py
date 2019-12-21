import numpy as np
from matplotlib import pyplot as plt
import wave
import struct

def main():

    fp = wave.open('Sin_1.wav', 'rb')
    sampling_rate = fp.getframerate()
    n_frames = fp.getnframes()
    sample_width = fp.getsampwidth()
    time_lenght = n_frames/sampling_rate
    frames = []
    print('Sampling rate: ', sampling_rate,' frames per second.')
    print('Number of frames: ', n_frames)
    print('Lenght: ',time_lenght, 's')
    print('Sample Width: ', sample_width, ' byte')
    for x in range(n_frames):
        d = fp.readframes(1)
        temp = struct.unpack('h', d)
        frames.append(temp[0]/(2**(8*sample_width-1)))

    #print(type(frames))

    plt.plot(np.arange(n_frames), frames)
    plt.show();
    print(max(frames))



if __name__ == '__main__':
    main()
