#!/usr/bin/env python2


import qi
import time
import sys
import argparse
import game

def run():
    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
        parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

        args = parser.parse_args()
        try:
            # Initialize qi framework.
            connection_url = "tcp://" + args.ip + ":" + str(args.port)
            app = qi.Application(["Hangman", "--qi-url=" + connection_url])
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)

        hangman = game.Hangman(app)
        hangman.play()

if __name__ == "__main__":
    run()
