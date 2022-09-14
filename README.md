# Source codes of the "Engineering mathematics and simulation illustrations" videos

## About

This repository contains the source codes of the animations in the ["Engineering mathematics and simulation illustrations"](https://www.youtube.com/playlist?list=PL6fjYEpJFi7V9eDVEWeeYCB-NXI8ieqct) series. The codes are developed using the [Manim community](https://www.manim.community/) package in Python.

After installing Manim, you can simply build and run the animations with this command:
```Shell
manim -pqh pde_animation.py PDE
```

or this one for producing a low quality video.
```Shell
manim -pql pde_animation.py PDE
```

## Source files

The following list shows the Manim source files used to produce the animations:

* `pde_animation.py`: used for the video "[Partial differential equations (PDEs) in engineering mathematics: introduction and classification](https://www.youtube.com/watch?v=CiWcp1apu8Q&ab_channel=TuxRiders)"

* `scenes_rda.py`: used for the mathematical part of the video "[Parabolic PDEs and Reaction-Diffusion-Advection equation](https://www.youtube.com/watch?v=6wNf7dflkl0&ab_channel=TuxRiders)"

* `scenes_rda_extra.py`: used for the first scene of the above video
