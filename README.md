# audio-conv
convert thing

## Installation

`python3`: https://www.python.org/downloads/

`ffmpeg` ([Windows](https://www.thewindowsclub.com/how-to-install-ffmpeg-on-windows-10), [Mac](http://jollejolles.com/install-ffmpeg-on-mac-os-x/))

## Example usage

Convert all AIFF files in `~/Music` and its subdirectories to FLAC (deleting original files):

`python3 audio-conv.py ~/Music`

Preserve old files after conversion:

`python3 audio-conv.py ~/Music --preserve`
