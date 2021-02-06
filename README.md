# audio-conv
convert thing

## Installation

`python3`: https://www.python.org/downloads/

`ffmpeg` ([Windows](https://www.thewindowsclub.com/how-to-install-ffmpeg-on-windows-10), [Mac](http://jollejolles.com/install-ffmpeg-on-mac-os-x/))

## Example usage

Convert all files in `.` from FLAC to AIFF:

`python3 audio-conv.py .`

Preserve old files after conversion:

`python3 audio-conv.py . --preserve`
