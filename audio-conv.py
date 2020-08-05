# this is python 3.8

import os, argparse, subprocess

from_format = ".flac"
to_format = ".aiff"
ffmpeg = "ffmpeg.exe"

def conv(dir, preserve=False):
	for root, dirs, files in os.walk(dir):
		for file in files:
			if file.endswith(from_format):
				fpath = os.path.join(root, file)
				try:
					subprocess.check_call([ffmpeg, "-i", fpath, "-write_id3v2", "1", "-c:v", "copy", fpath.replace(from_format, to_format)])
				except:
					print("ERROR: Error converting {}".format(fpath))
					continue
				if preserve:
					continue
				os.remove(fpath)

def main():
	parser = argparse.ArgumentParser(description='Convert all the things.')
	parser.add_argument('root_dir', help="Directory containing files to convert.")
	parser.add_argument('--preserve', action="store_true", help="Preserve files after converting them.")
	args = parser.parse_args()
	conv(args.root_dir, args.preserve)

if __name__ == "__main__":
	main()