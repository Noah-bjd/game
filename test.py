#!/usr/bin/env python3

# use screen capture to interactively select region of screen to
# capture, and then save that .png to the Desktop (default)

# Coordinates (in Safari 14.0.3) set to capture "Apple Support Communities Site Map" from
# https://discussions.apple.com/productsitemap.jspa

import subprocess
import os
import sys


def main():
    outfile = os.path.expanduser('~/Desktop/captured.png')
    outcmd = "{} {} {} {}".format('screencapture', '-x', '-R332,330,770,75', outfile)

    # traditional date/time stamped screen capture file to the default desktop
    # outcmd = "{} {} {} {}".format('screencapture', '-x', '-R332,330,770,75', '-p')

    try:
        # ordinarily we would not use shell=True due to security concerns
        subprocess.check_output([outcmd], shell=True)
    except subprocess.CalledProcessError as e:
        print('Python error: [%d]\n{}\n'.format(e.returncode, e.output))


if __name__ == '__main__':
    sys.exit(main())
