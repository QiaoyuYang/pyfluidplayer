import fluidsynth
import numpy
import pyaudio
import wave
import os
import argparse

CHANNELS = 2
RATE = 44100
FORMAT = pyaudio.paInt16
out_len_in_s = 30

def synthesize(instrument, part):

    os.makedirs("output", exist_ok=True)

    with wave.open(f'output/{part}.wav', 'wb') as wf:
        
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(pyaudio.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        fs = fluidsynth.Synth()
        fs.custom_router_callback = None

        sfid = fs.sfload(f"soundfonts/{instrument}.sf2")
        fs.program_select(0, sfid, 0, 0)

        fs.play_midi_file(f"bc_no2_mv1/bc_no2_mv1_{part}.mid")

        # Generate seconds of audio into s
        s = []
        for _ in range(out_len_in_s):
            s = numpy.append(s, fs.get_samples(RATE))
            if fluidsynth.fluid_player_get_status(fs.player) != fluidsynth.FLUID_PLAYER_PLAYING:
                break
        fs.delete()
            
        samps = fluidsynth.raw_audio_string(s)
        
        wf.writeframes(samps)

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--instrument", type=str, default="trombone", help="The instrument of the track")
    parser.add_argument("-p", "--part", type=str, default="trombone", help="The part name of the track")
    args = parser.parse_args()
    instrument = args.instrument
    part = args.part
    
    synthesize(instrument, part)


if __name__ == "__main__":
    main()