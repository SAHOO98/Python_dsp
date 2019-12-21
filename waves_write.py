import numpy as np
import wave
import matplotlib.pyplot as plt
import struct

#Sine_params
frequency = 1
amplitude = int(2**14)
sample_rate = 48000.0
no_of_samples = int(5*sample_rate) # no of samples = sampling rate * time interval we need

#file_details
file_name = 'Sin_'+str(frequency)+'.wav'

#wav_file_details
nframes=no_of_samples
comptype="NONE" #compressed_type
compname="not compressed" #compressed_type
nchannels=1 #mono
sampwidth=2 #16_bit

def main():
    sin_wave = [np.sin(2*np.pi* frequency *(x/sample_rate)) for x in range(no_of_samples)]
    #+ np.sin(2*np.pi* (frequency+500) * (x/sample_rate))
    #plt.plot(np.arange(no_of_samples), sin_wave);
    #plt.show();

    #print(sin_wave)
    print('Sin wave is calculated and opening wav file.')
    wav_file = wave.open(file_name, 'wb')
    wav_file.setparams((nchannels, sampwidth, int(sample_rate), nframes, comptype, compname))
    #size = len(sin_wave)
    #i = 0;
    print('Writing in the file.')
    for s in sin_wave:
        #percentage = i/size *100
        #print('Percentage complete: ', percentage,'%.')
        wav_file.writeframes(struct.pack('h', int(s*amplitude)))
    #    i = i+1

    wav_file.close()
    print("Done Creating Wave file.")

if __name__ == '__main__':
    main()
