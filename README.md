# pyfluidplayer
A music player based on pyfluidsynth to play midi files with given patches for each track

## Install
### 1. Install FluidSynth
* [MacOS/Linux](https://github.com/FluidSynth/fluidsynth/wiki/Download#distributions)
* [Windows/Android](https://github.com/FluidSynth/fluidsynth/releases)

### 2. Setup Python Environment
```
pip install -r requirements.txt
```
## Synthesize
#### Currently the system only supports the instrumental tracks of Switched on Bach by Wendy Carlos. To synthesize a specific track, run
```
python synthesize_sob.py -i [instrument] -p [part_name]
```
#### The list of candidates instruments are:
* trombone
* flute
* oboe
* violin
* violinEnsemble
* viola
* doubleBass
* cello
#### The output audio files will be saved in /output
