from add_demo import add
from demo import Demo

import argparse

# TODO add help text
class AddDemoCommand(object):
    def execute(self):
        parser = argparse.ArgumentParser(description="Add a demo to the list of demos.", 
                                         usage="TODO")
        parser.add_argument("name", help="The name of the demo.")
        parser.add_argument("key", help="The key of the demo.")
        parser.add_argument("url", help="The url of the demo.")
        parser.add_argument("--size", help="The size of the demo.", default=157.6*1024*1024)
        parser.add_argument("--heap", help="The heap of the demo.", default=387*1024*1024)
        parser.add_argument("--compiler", help="The compiler of the demo.", default="")
        parser.add_argument("--engine", help="The engine of the demo.", default="")
        parser.add_argument("--date", help="The date of the demo.", default="")
        parser.add_argument("--version", help="The version of Unity the demo uses.", default="")
        parser.add_argument("--apis", help="The apis of the demo.", default=["wasm", "URP", "WebGL 2", "linear-color-space"])
        parser.add_argument("--noVsync", help="The noVsync of the demo.", default=True)
        parser.add_argument("--interactive", help="The interactive of the demo.", default=True)
        parser.add_argument("--mobile", help="The mobile of the demo.", default=True)

        args = parser.parse_args()

        demo = Demo(args.name, 
                    args.key, 
                    args.url, 
                    args.size, 
                    args.heap, 
                    args.compiler, 
                    args.engine, 
                    args.date, 
                    args.version,
                    args.apis, 
                    args.noVsync, 
                    args.interactive, 
                    args.mobile)
        
        add(demo)

if __name__ == "__main__":
    AddDemoCommand().execute()