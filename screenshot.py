#!/usr/bin/env python
import subprocess
import argparse
import webkit2png

import sys

def webkit2png( stack=[] ):
    if 0 == len( stack ):
        print "function webkit2png called with no arguments"
        sys.exit( 1 )

    #hardcoded options, and the command
    stack.insert( 0, "-F" )
    stack.insert( 0, "webkit2png" )
    subprocess.call( stack )

def main():
    stack = [] #collects options

    #sets up command
    parser = argparse.ArgumentParser(description="Wrapper around webkit2png. Allows it to be called in a loop")
    parser.add_argument( "url",
                    action="store",
                    help="http://www.google.com")
    parser.add_argument( "-W", "--width",
                    action="store",
                    help="initial (and minimum) width of browser (default: 800)")
    parser.add_argument( "-H", "--height",
                    action="store",
                    help="initial (and minimum) height of browser (default: 600)")
    parser.add_argument( "-z", "--zoom",
                    action="store",
                    help="full page zoom of browser (default: 1.0)")
    parser.add_argument( "-o", "--filename",
                    action="store",
                    help="save images as NAME-full.png,NAME-thumb.png etc")
    parser.add_argument( "-D", "--dir",
                    action="store",
                    help="save images as NAME-full.png,NAME-thumb.png etc")
    args = parser.parse_args()

    #collects options - can fix any issues here
    #TODO
    #subprocess.call doesnt' like paths starting with a ~ it would be nice to substitute that
    for a in [ "width", "height", "zoom", "filename", "dir"]:
        if args.__dict__[a]:
            stack.append( "--" + a )
            stack.append( args.__dict__[a] )
    stack.append( args.url )

    webkit2png( stack )

if __name__ == "__main__":
    main()