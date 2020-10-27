# Emunittest Unity Browser WebAssembly Benchmark Suite

This repository contains a test suite for benchmarking WebAssembly based Unity content in web browsers.

It consists of a number of classic Unity and Dots/Tiny Unity compiled demos, that have been converted to run deterministically in the browser. This enables comparing browser performance, and testing against bugs.

The result data that emunittest provides looks something like this

```
 Run Date         | Test Name                             | Total time (lower is better) |   FPS | CPU Time |   WebGL CPU Time | WebGL calls/frame| CPU Idle | Page load time | # of janked frames | Used JS Mem
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 2020-10-27 10:39 | Skelebuddies wasm 2020-10-2020-10-26  |                      13335ms |160.68 |  10882ms |    (not tracked) |    (not tracked) |   11.22% |       575.98ms |                  5 |     165.6MB
 2020-10-27 10:40 |Skelebuddies wasm2js 2020-10-2020-10-26|                      46217ms | 44.84 |  43569ms |    (not tracked) |    (not tracked) |    1.91% |      1311.37ms |                 67 |     203.8MB
 2020-10-27 10:40 |Tiny3D Unity Classic 2020-04-2020-04-20|                       7976ms |225.97 |   4785ms |    (not tracked) |    (not tracked) |   16.55% |      1816.50ms |                 10 |     114.7MB
 2020-10-27 10:40 | Tiny3D-2020-03-01                     |                       5697ms |179.19 |   1047ms |    (not tracked) |    (not tracked) |   77.75% |       419.03ms |                  6 |     192.0MB
 2020-10-27 10:41 | Lost Crypt-2019-12-20                 |                      29554ms | 76.90 |  24513ms |    (not tracked) |    (not tracked) |    4.27% |      3268.80ms |                 16 |     647.6MB
 2020-10-27 10:41 | TinyRacing v3 wasm 2020-03-2020-03-18 |                      10399ms |140.04 |   7349ms |    (not tracked) |    (not tracked) |   16.07% |       902.09ms |                  6 |     162.5MB
 2020-10-27 10:41 |TinyRacing v3 wasm2js 2020-03-2020-03-17|                      15088ms | 92.36 |  12896ms |    (not tracked) |    (not tracked) |    6.17% |       687.71ms |                 25 |     172.7MB
 2020-10-27 10:42 |TinyRacing v3 fc wasm 2020-03-2020-03-17|                       9539ms |149.28 |   6854ms |    (not tracked) |    (not tracked) |   16.27% |       596.57ms |                 13 |     160.2MB
 2020-10-27 10:42 |TinyRacing v3 fc asmjs 2020-03-2020-03-17|                      11242ms |131.68 |   8708ms |    (not tracked) |    (not tracked) |    8.20% |      1141.37ms |                 10 |     147.6MB
 2020-10-27 10:42 | TinyRacing v2 RC 2020-01-2020-01-24   |                      19038ms | 71.03 |  17319ms |    (not tracked) |    (not tracked) |    3.03% |       518.88ms |                  5 |     152.0MB
 2020-10-27 10:42 | TinyRacing v1 2019-12-2019-12-12      |                      11765ms |118.29 |  10086ms |    (not tracked) |    (not tracked) |    5.14% |       470.14ms |                  4 |     157.4MB
 2020-10-27 10:42 | Tanks-2019-10-04                      |                      11664ms |161.89 |   7868ms |    (not tracked) |    (not tracked) |    9.82% |      2092.05ms |                 14 |     168.5MB
 2020-10-27 10:43 | Microgame - FPS-2019-09-22            |                      12289ms |104.24 |   7884ms |    (not tracked) |    (not tracked) |   14.26% |      2382.84ms |                 15 |     349.2MB
 2020-10-27 10:43 | Ruby's Adventure-2019-07-22           |                       8653ms |230.58 |   4676ms |    (not tracked) |    (not tracked) |   20.77% |      1822.72ms |                  6 |     131.3MB
 2020-10-27 10:43 | The Explorer-2019-07-23               |                      18985ms |109.56 |  10284ms |    (not tracked) |    (not tracked) |    8.72% |      6806.36ms |                 12 |     720.8MB
 2020-10-27 10:43 | LWRPTemplate-2019-09-19               |                       7142ms |105.20 |   3378ms |    (not tracked) |    (not tracked) |   14.58% |      1970.85ms |                  7 |     196.2MB
 2020-10-27 10:44 | Microgame - Kart-2019-07-25           |                      19159ms |118.25 |  11714ms |    (not tracked) |    (not tracked) |   28.41% |      1992.76ms |                 11 |     331.1MB
 2020-10-27 10:44 | BoatAttack-2019-07-22                 |                      43762ms | 54.19 |  35437ms |    (not tracked) |    (not tracked) |    2.58% |      6480.85ms |                 25 |     667.1MB
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

# Contact

For bugs and feedback, contact `jukkajATunity3dDOTcom`.
