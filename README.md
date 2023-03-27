# Emunittest Unity Browser WebAssembly Benchmark Suite

This repository contains a test suite for benchmarking WebAssembly based Unity content in web browsers.

It consists of a number of classic Unity and Dots/Tiny Unity compiled demos, that have been converted to run deterministically in the browser. This enables comparing browser performance, and testing against bugs.

The result data that emunittest provides looks something like this

```
 Run Date         | Test Name                             | Total time (lower is better) |   FPS | CPU Time |   WebGL CPU Time | WebGL calls/frame| CPU Idle | Page load time | # of janked frames | Used JS Mem
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 2020-10-27 10:55 | Skelebuddies wasm-2020-10-26          |                      13348ms |154.00 |  11622ms |    (not tracked) |    (not tracked) |    8.71% |       237.25ms |                  6 |     166.0MB
 2020-10-27 10:56 | Skelebuddies wasm2js-2020-10-26       |                      46688ms | 43.87 |  44544ms |    (not tracked) |    (not tracked) |    1.83% |       904.22ms |                 86 |     214.4MB
 2020-10-27 10:56 | Tiny3D Unity Classic-2020-04-20       |                       7162ms |241.14 |   4487ms |    (not tracked) |    (not tracked) |   16.15% |      1626.30ms |                  5 |     114.4MB
 2020-10-27 10:56 | Tiny3D-2020-03-01                     |                       4859ms |207.34 |   1921ms |    (not tracked) |    (not tracked) |   53.81% |       309.47ms |                 17 |     190.6MB
 2020-10-27 10:56 | Lost Crypt-2019-12-20                 |                      29535ms | 75.74 |  24952ms |    (not tracked) |    (not tracked) |    4.03% |      2976.06ms |                 20 |     649.9MB
 2020-10-27 10:57 | TinyRacing v3 wasm-2020-03-18         |                      10376ms |130.01 |   8210ms |    (not tracked) |    (not tracked) |   13.36% |       220.37ms |                  8 |     145.7MB
 2020-10-27 10:57 | TinyRacing v3 wasm2js-2020-03-17      |                      16528ms | 81.74 |  14795ms |    (not tracked) |    (not tracked) |    4.35% |       460.43ms |                 48 |     174.7MB
 2020-10-27 10:57 | TinyRacing v3 fc wasm-2020-03-17      |                       9145ms |148.95 |   6657ms |    (not tracked) |    (not tracked) |   18.57% |       257.60ms |                  4 |     147.5MB
 2020-10-27 10:57 | TinyRacing v3 fc asmjs-2020-03-17     |                      11687ms |123.55 |   9013ms |    (not tracked) |    (not tracked) |   11.11% |      1007.01ms |                  6 |     168.5MB
 2020-10-27 10:58 | TinyRacing v2 RC-2020-01-24           |                      17712ms | 75.16 |  16193ms |    (not tracked) |    (not tracked) |    3.65% |       256.10ms |                  4 |     159.9MB
 2020-10-27 10:58 | TinyRacing v1-2019-12-12              |                      11353ms |118.14 |   9858ms |    (not tracked) |    (not tracked) |    7.14% |       212.35ms |                  5 |     164.9MB
 2020-10-27 10:58 | Tanks-2019-10-04                      |                       8477ms |198.45 |   6338ms |    (not tracked) |    (not tracked) |   10.25% |       743.25ms |                  4 |     168.8MB
 2020-10-27 10:58 | Microgame - FPS-2019-09-22            |                      10975ms |107.29 |   7679ms |    (not tracked) |    (not tracked) |   13.42% |      1468.69ms |                 14 |     345.2MB
 2020-10-27 10:58 | Ruby's Adventure-2019-07-22           |                       8320ms |243.49 |   4210ms |    (not tracked) |    (not tracked) |   24.59% |      1866.00ms |                  6 |     137.9MB
 2020-10-27 10:59 | The Explorer-2019-07-23               |                      17610ms | 98.13 |  11624ms |    (not tracked) |    (not tracked) |    7.39% |      4098.70ms |                 12 |     718.1MB
 2020-10-27 10:59 | LWRPTemplate-2019-09-19               |                       6836ms |104.52 |   3566ms |    (not tracked) |    (not tracked) |   11.86% |      1818.85ms |                  6 |     260.5MB
 2020-10-27 10:59 | Microgame - Kart-2019-07-25           |                      18888ms |119.61 |  11037ms |    (not tracked) |    (not tracked) |   31.48% |      1950.83ms |                 13 |     330.3MB
 2020-10-27 11:00 | BoatAttack-2019-07-22                 |                      43921ms | 51.81 |  37067ms |    (not tracked) |    (not tracked) |    2.62% |      5093.16ms |                 22 |     667.2MB
                  |                                       |                              |       |          |                  |          |                |                    |            
```

# Installation

To install the suite for local use, run

```
git clone https://github.com/Unity-Technologies/emunittest.git
cd emunittest
python install.py
```

To update an existing installation to a newer version, run

```
cd /path/to/emunittest
git pull
python install.py
```

# Running

After installing, launch `start_server.bat` (or `./start_server` on Linux and macOS) to spin up an ad hoc web server at `http://localhost:6932/` to host the content.

Then navigate to `http://localhost:6932/` to visit the launcher.

There are three main ways to run:

1. Run the full suite by clicking on `Run tests` button in the launcher. **Be sure to allow popups to help the tests to run through**
2. Run a single test by clicking on `Test` to the right side of the test name.
3. Run a single demo in interactive mode by clicking on `Launch` button next to a test. In this mode the content runs unmodified to the original build from Unity.

Additionally there are a few options to customize how the content is run, e.g. one can disable vsync (uses postMessage() to self to render instead of rAF()), embed a CPU frametime profiler graph, or run the suite in a torture test mode.

# Automation
This suite can be run from the command line, via the 'emrun' browser automation tool.

Getting Started
---------------

To manually run the full suite and capture results to a file on a single browser instance, type

    python run.py [--browser=/path/to/firefox] > results_file.txt 2>&1

For more command line options that can be passed to run.py, type

    python emrun.py --help

Notes:

  - When running with Firefox, a clean temporary Firefox profile is used (hack emrun.py or run.py if this is not desirable)
  - If --browser=xxx is not specified, the default system browser is launched.
  - results_file.txt receives a full test results after each test is run, so only the last printed matrix at the end of the file is generally interesting.
  - If you run into any issues, email jjylanki@mozilla.com.

Running a single test
---------------------

To run a single test N number of times in a custom browser, execute

   python run.py --browser=/path/to/firefox -- selectedTests=a,b,c numtimes=N

This will spawn a new Firefox browser instance in a new profile, and after the tests are run, Firefox browser quits.

Note that the '--' is deliberately detached via a space character from "selectedTests" directive above, as the '--' symbol is used to distinguish between params to emrun
from params to the page.

To find the names of the tests, open the index.html and look for the "key" field in the definition of the tests array.

Launching the test suite HTTP server without running any tests
--------------------------------------------------------------

Sometimes it is useful to just host the test suite over HTTP without immediately launching a browser process. To fire up a HTTP server
in the root directory of the emunittest suite, run the start_server(.bat) script. Then navigate a browser to the shown HTTP address,
typically http://localhost:6931/

Configuring test run mode
-------------------------

It is possible to pass parameters to the index.html page to automatically choose options for how to run. These parameters come after the
'--' delimiter on the command line.

For example, to run all tests without WebGL vsync enabled, run

   python run.py --browser=/path/to/firefox -- novsync

To enable torture test mode (infinitely reruns the suite after finishing), execute

  python run.py --browser=/path/to/firefox -- tortureMode

In parallel torture mode, multiple tests are run at the same time in several tabs:

  python run.py --browser=/path/to/firefox -- paralleltorturemode novsync

This run is best chained with novsync, since that flag is needed to update rendering on the background tabs (with novsync, postMessage()
will be used instead of requestAnimationFrame to pump the rendering)

Running the suite on an automatically downloaded Firefox Nightly
----------------------------------------------------------------

The emunittest suite can also run in an automated/unattended manner where the suite harness downloads versions of Firefox Nightly and executes the suite on them.
The benchmark_firefox.py script is used for that purpose. There are a few different ways to run this:

 - To download latest Firefox and run the harness through it, type

     python benchmark_firefox.py latest

 - To download and test the newest Firefox Nightly version that hasn't yet been tested, run

     python benchmark_firefox.py latest_untested

   In this mode, the harness keeps track of any earlier tested Nightly versions (located in .benchmarks.done subdirectory) to make sure it only tests the newest one.
   The individual tags in the subdirectory .benchmarks.done can be freely deleted to make the harness re-test Firefox Nightly from a particular date.

 - To continuously keep downloading and testing the newest Firefox Nightly versions in a sequence, run

     python benchmark_firefox.py all_untested

   This script will loop over all recent Nightlies up to 180 days in the past.

Avoiding redownloading browser versions
---------------------------------------

If there is a need to benchmark the same browser version multiple times, it is possible to keep the downloaded zip files in a cache directory, to avoid having to
redownload it later. To do this, pass the command line parameter --no_delete_zip to benchmark_firefox.py. To keep the whole browser subdirectory on disk, one can
also pass the --no_delete command line parameter to benchmark_firefox.py. For example,

    python benchmark_firefox.py all_untested --no_delete_zip

will test Nightlies up to 180 days in history, while keeping all downloaded Firefox Nightly zip files in the subdirectory .browsers (feel free to delete the cache
directory at any given time)

If the system hardware configuration changes
--------------------------------------------

To identify the system across multiple runs so that it is possible to graph a timeline view from runs from the same machine, a unique identifier is generated to the
user home directory, in location ~/.emrun.generated.guid. If the system hardware setup is modified, e.g. changing GPUs, or updating the major version of an operating
system, or similar, it can be desirable to make the updated system appear as a completely new hardware. To reset the identifier, simply delete ~/.emrun.generated.guid,
after which the system will appear as a uniquely new system.


# Unity Instructions
To make a Unity WebGL build compatible with emunittest harness:
---------------------------------------------------------------

1. Copy the exported Unity WebGL build into a subdirectory, say my_webgl_game/
2. Manually edit my_webgl_game/index.html to adjust the game HTML file to be compatible with emunittest. A diff of needed
   changes is shown below:

diff --git a/original_index.html b/emunittest_compatible_index.html
--- a/original_index.html
+++ b/emunittest_compatible_index.html
@@ -21,5 +16,15 @@
         <div class="title">My WebGL Game</div>
       </div>
     </div>
+    <script src='../cpuprofiler.js'></script>
+    <script>var emtimerOptions = { numFramesToRender: 500 }; </script>
+    <script src="../emtimer.js"></script>
+    <script src="inputstream.js"></script>
   </body>
 </html>

3. Customize 'numFramesToRender' field above to choose the length of the demo, in # of frames.
4. While this step is not strictly necessary, it helps with the visual HTML page layout to work better with emunittest: Edit file TemplateData/style.css and add the following lines at the end of that file:

body { margin: 0; overflow: hidden; }
html, body, .webgl-content, #gameContainer, #unityContainer, canvas { width: 100% !important; height: 100% !important; }
.footer { display: none; }
.webgl-content { position: static !important; top: 0% !important left: 0% !important; -webkit-transform: translate(0%, 0%); transform: translate(0%, 0%); }

5. Edit emunittest's index.html to add a new entry in the 'var tests = [..]' list, e.g.

var tests = [
  ...
{ name: "My WebGL game", key: 'my_webgl_game', url: "my_webgl_game/index.html", size: 0, heap: 0, compiler: '', engine: '', date: '', apis: [''], noVsync: true, interactive: true, mobile: true },
  ...
];

You may populate any fields in the above entry, they will be shown in the UI for visual posterity.

After these steps, the new demo is now compatible to run in emunittest suite.

To record a keyboard+mouse input stream for a demo:
---------------------------------------------------

This step is only needed if you need to get keyboard or mouse input into the built page. If the page is good to go without injected interaction, this step can be skipped.

1. Start the emunittest server, and navigate to http://localhost:6932/my_webgl_game/index.html?record
2. Play the game, recording keyboard and mouse events
3. Once the specified number of frames has elapsed, the game canvas will disappear, and the recorded input stream function will appear on the page.
   Copy-paste these contents to a new file emunittest/my_webgl_game/inputstream.js

After creating the inputstream.js file, the keyboard and mouse input should now play back automatically when the test is run via the test harness.

# Tiny Unity Instructions

To make a DOTS/Tiny Unity web build compatible with emunittest harness:
-----------------------------------------------------------------------

1. Copy the exported web build into a subdirectory, say my_webgl_game/
2. Manually edit my_webgl_game/my_webgl_game.html to adjust the game HTML file to be compatible with emunittest. Find the location of the *first* <script> tag in the file, and before that <script> element, add in the following four script lines:

    <script src='../cpuprofiler.js'></script>
    <script>var emtimerOptions = { numFramesToRender: 500 }; </script>
    <script src="../emtimer.js"></script>
    <script src="inputstream.js"></script>

3. Customize 'numFramesToRender' field above to choose the length of the demo, in # of frames.

4. Edit emunittest's index.html to add a new entry in the 'var tests = [..]' list, e.g.

var tests = [
  ...
{ name: "My WebGL game", key: 'my_webgl_game', url: "my_webgl_game/index.html", size: 0, heap: 0, compiler: '', engine: '', date: '', apis: [''], noVsync: true, interactive: true, mobile: true },
  ...
];

You may populate any fields in the above entry, they will be shown in the UI for visual posterity.

After these steps, the new demo is now compatible to run in emunittest suite.

To record a keyboard+mouse input stream for a demo:
---------------------------------------------------

This step is only needed if you need to get keyboard or mouse input into the built page. If the page is good to go without injected interaction, this step can be skipped.

1. Start the emunittest server, and navigate to http://localhost:6932/my_webgl_game/index.html?record
2. Play the game, recording keyboard and mouse events
3. Once the specified number of frames has elapsed, the game canvas will disappear, and the recorded input stream function will appear on the page.
   Copy-paste these contents to a new file emunittest/my_webgl_game/inputstream.js

After creating the inputstream.js file, the keyboard and mouse input should now play back automatically when the test is run via the test harness.

# Demo Requirements

The following requirements should be met for a game demo to be included to the suite:

1. The demo should have a mode to run autonomously without any user interaction required. This mode should be easy to trigger, e.g. press a key on the keyboard after the demo starts up, or even automatic. Optionally, the demo can have an interactive mode that allows the user to play with it.

2. Render using requestAnimationFrame(), and not setTimeout/setInterval/setImmediate or other event-based mechanisms.

3. Only register exactly one rAF loop. If two are needed, register one global one and route the calls to both.

4. Application should statically create the canvas to render to on the main html page, i.e.

   <canvas id='myCanvas'></canvas>

as opposed to creating it dynamically inside library code. This is because the harness will need to inject to the canvas for profiling purposes before the application starts, so the canvas should be available beforehand.

5. Don't resize the visible CSS size of the canvas to custom values e.g. based on browser window size. The harness controls the presentation size by embedding the demo page in an iframe.

6. Use a fixed WebGL render target size for rendering, and preferably set the render target size in the main .html file. The size 1033x581 pixels is preferred, although if a different aspect ratio is desired, the pixel size should be smaller than this value both in width and height.

7. Don't use synchronous blocking loops that depend on time to proceed as their exit condition. That is, the following style of code should be forbidden:

   var t0 = performance.now();
   while(performance.now() - t0 < 1000) {
      // Do something;
   }

These types of loops will result in an application deadlock. The reason for this is that the test harness forces the demo to run in a "timedemo" manner, where time is advanced by a fixed 1/60th of a second each frame to make the executed computations identical on all tested systems for the results to be comparable.

Likewise, don't use performance.now() or Date.now() to generate random numbers, but use Math.random() or some other PRNG. PRNGs can be seeded from performance.now() or Date.now(), but applications should not assume that the seeds would change on subsequent seedings.

8. Prefer loading all assets up front at startup. This allows preloading the assets so that the demo test results times will not include any loading times.

9. The total maximum downloaded amount of assets should be less than 150MB.

10. Do not download content from online sources. The demo must run fully offline (unless the aim of the demo is to specifically test an online server component).

11. Create a global "Module" object in the main HTML file which defines the interaction of the demo with the harness. This object can configure how the harness works on the demo:

var Module = {
	// Name of this game demo
	key: 'uniqueIdentifierForTheDemoInQuestion'

	// Options that the demo can pass to the harness: (the values set below show the default choices for the options, if the option is not present)

	// If true, this demo provides requestAnimationFrame() integration for emunittest built-in. Generally this needs to be false, unless the app was specially built with emunittest support enabled.
	providesRafIntegration: false,

	// If true, this demo needs a faked Date.now()&performance.now() that advance after each call. If false, they can advance after each game frame. Generally set to false, unless game has problems with it.
	needsFakeMonotonouslyIncreasingTimer: false,

	// Specifies the time scale factor how fast time advances. If not specified, defaults to 1. Use this to scale the demo to advance faster or slower if necessary.
	fakeTimeScale: 1.0,

	// If true, Date.now()&performance.now() should not be faked at all for this demo, but the demo maintains the fixed timesteps itself. Generally always set to false, unless demo has been crafted with this specifically.
	dontOverrideTime: false,

	// If set to a > 0 value, this overrides the default number of frames that the test harness renders, which is 2000. This can further be overridden in the URL via '?numframes=<integer>' parameter for a single run.
	overrideNumFramesToRender: 2000,

	// Set this to true for demos that utilize the Emscripten html5.h input API. Defaults to false.
	usesEmscriptenHTML5InputAPI: false,

	// If true, the harness should intercept all XHRs to provide transparent caching of assets and a progress bar. Defaults to false.
	injectXMLHttpRequests: false,

	// This function is used to filter out certain XHRs from being fired at all. For the application perspective, it is as if they always time out.
	xhrFilter: function(url) {
		// If the function returns false, the XHR is ok to run and doesn't need to be discarded. If true, the XHR should be filtered out. If this function is not defined, all XHRs are ok to run.
		return false;
	},

	// If true, 'resize' events of the browser window should get through to the game demo. By default the demo does not see browser window resizes.
	pageNeedsResizeEvent: false,

	// Optional: Application can implement this function to provide a hook to the harness to fade out the audio volume when the demo is about to finish. This
	//           allows a nice exit to the demo when the audio doesn't sharply cut off.
	globalMasterVolumeSetCallback: function(volume) {
		// Set master volume to a value between 0.0 - 1.0.
	}
};


# Contact

For bugs and feedback, contact `jukkajATunity3dDOTcom`.
