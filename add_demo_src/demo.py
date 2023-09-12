class Demo:
    def __init__(self, 
                 name, 
                 key, 
                 url, 
                 size=157.6*1024*1024, 
                 heap=387*1024*1024, 
                 compiler="", 
                 engine="", 
                 date="", 
                 apis=['wasm', 'URP', 'WebGL 2', 'linear-color-space'], 
                 noVsync=True, 
                 interactive=True, 
                 mobile=True):
        self.name = name
        self.key = key
        self.url = url
        self.size = size
        self.heap = heap
        self.compiler = compiler
        self.engine = engine
        self.date = date
        self.apis = apis
        self.noVsync = noVsync
        self.interactive = interactive
        self.mobile = mobile