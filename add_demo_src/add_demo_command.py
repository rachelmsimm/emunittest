from add_demo import add
from demo import Demo

import argparse

class AddDemoCommand(object):
    def execute(self):
        parser = argparse.ArgumentParser(description="Add a demo to the list of demos to be run by Emunittest")
        parser.add_argument("name", help="The name of the demo (must be unique)")
        parser.add_argument("key", help="The key of the demo (must be unique)")
        parser.add_argument("url", help="The path to the demo, usually to its index.html page, relative to the root of Emunittest")
        parser.add_argument("--size", help="The disk size of the demo in MB", default=157.6*1024*1024)
        parser.add_argument("--heap", help="The heap size of the demo in MB", default=387*1024*1024)
        parser.add_argument("--compiler", help="The compiler used to compile the build", default="")
        parser.add_argument("--engine", help="The version of Unity that was used", default="")
        parser.add_argument("--date", help="The date the demo was created or added", default="")
        parser.add_argument("--apis", help="The APIs used by the build/demo", default=["wasm", "URP", "WebGL 2", "linear-color-space"])
        parser.add_argument("--noVsync", help="Whether or not no Vsync is used", default=True)
        parser.add_argument("--interactive", help="Whether or not the demo is interactive (interactive demos have inputstream.js files)", default=True)
        parser.add_argument("--mobile", help="Whether the demo/build is meant to be run on mobile or not", default=True)

        args = parser.parse_args()

        demo = Demo(args.name, 
                    args.key, 
                    args.url, 
                    args.size, 
                    args.heap, 
                    args.compiler, 
                    args.engine, 
                    args.date, 
                    args.apis, 
                    args.noVsync, 
                    args.interactive, 
                    args.mobile)
        
        add(demo)

if __name__ == "__main__":
    AddDemoCommand().execute()