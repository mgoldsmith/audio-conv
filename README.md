# audio-conv
Convert FLAC files to AIFF.

## Installation

`python3`: https://www.python.org/downloads/

`ffmpeg` ([Windows](https://www.thewindowsclub.com/how-to-install-ffmpeg-on-windows-10), [Mac](http://jollejolles.com/install-ffmpeg-on-mac-os-x/))

## Example usage

Convert all FLAC files in `~/Music` and its subdirectories to AIFF (deleting original files):

`python3 audio-conv.py ~/Music`

Preserve old files after conversion:

`python3 audio-conv.py ~/Music --preserve`
