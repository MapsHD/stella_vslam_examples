# Build notes (mwlasiuk)

Clone repository recursively : 
``` sh
git clone --recursive https://github.com/mwlasiuk/stella_vslam_examples.git
```

Enter repository and run dependencies configuration script :
``` sh
cd stella_vslam_examples
chmod +x prepare.sh
sudo ./prepare.sh
```

NOTE : If you get deprecation warning screen just wait for 20 seconds and then you will get another waning screen and after 60 seconds script will continue.

Build stella_vslam_examples and its submodules :
``` sh
cd stella_vslam_examples
mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build . -j 4
```

Built binaries are available inside build directory :
``` sh
michal@LAPTOP-20I7RCHU:~/stella_vslam_examples/build$ ls -lah
total 16M
drwxr-xr-x  4 michal michal 4.0K Aug 15 10:00 .
drwxr-xr-x  8 michal michal 4.0K Aug 15 10:10 ..
-rw-r--r--  1 michal michal  29K Aug 15 09:27 CMakeCache.txt
drwxr-xr-x 12 michal michal 4.0K Aug 15 10:01 CMakeFiles
-rw-r--r--  1 michal michal  21K Aug 15 10:00 Makefile
-rw-r--r--  1 michal michal 1.8K Aug 15 09:27 cmake_install.cmake
-rwxr-xr-x  1 michal michal 2.3M Aug 15 09:41 run_camera_slam
-rwxr-xr-x  1 michal michal 2.3M Aug 15 09:41 run_euroc_slam
-rwxr-xr-x  1 michal michal 2.4M Aug 15 09:41 run_image_slam
-rwxr-xr-x  1 michal michal 2.3M Aug 15 09:41 run_kitti_slam
-rwxr-xr-x  1 michal michal 2.0M Aug 15 09:42 run_loop_closure
-rwxr-xr-x  1 michal michal 2.4M Aug 15 09:42 run_tum_rgbd_slam
-rwxr-xr-x  1 michal michal 2.4M Aug 15 09:41 run_video_slam
drwxr-xr-x  6 michal michal 4.0K Aug 15 10:00 stella_vslam
```

Orb vocabulary is located in __stella_vslam_examples/assets__

Sampe camera configs are located in __stella_vslam_examples/stella_vslam/example__

To unpck map file use
```sh
python3 extract.py --map_path PATH_TO_MAP
```

### License

This module was originally included in xdspacelab/openvslam. Therefore, the license follows the original license of xdspacelab/openvslam (BSD 2-Clause).

The following files are derived from third-party libraries.

- `./3rd/filesystem` : [gulrak/filesystem](https://github.com/gulrak/filesystem) (MIT license)
- `./3rd/popl` : [badaix/popl \[v1.2.0\]](https://github.com/badaix/popl) (MIT license)
