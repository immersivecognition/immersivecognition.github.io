---
name: Human-Like Computing
description: A project aiming to investigate the potential of human-like approaches in computation and robotics problems.
image: hlc.png
website: https://github.com/m-hasan-n/hlp
---

# Human-Like Computing (HLC)

## Background

How do you grasp a bottle of milk, nestling behind some yoghurt pots, within a cluttered fridge. Humans are able to easily and rapidly plan such actions using visual information, while robots struggle.
While artificial intelligence has made great leaps in beating humans in tasks such as chess, the planning and execution abilities of today's robots are trumped by the average toddler.
Given the complex and unpredictable world we live in, these apparently trivial tasks are the product of highly sophisticated neural computations that generalise and adapt to changing situations: continually engaged in a process of selecting between multiple goals and actions.

Our aim is to investigate how such computations could be transferred to robots to enable them to manipulate objects more efficiently, in a ore human-like way than is presently the case, and to be able to perform manipulation presently beyond the state of the art.

## Implementation

To investigate how humans interact with cluttered environments, a virtual reality (VR) scenario was created. 
VR has many advantages over traditional experimental setups, elaborated on in the UXF project. 
The Unity game engine and UXF were used to create a scenario where participants move obstacles on a table to reach a target and retrieve it to an end point.
The participant's hand, elbow and shoulder were tracked using a HTC Vive VR system and 2x HTC Vive trackers.
See the video below for an example of the scenario:

<video controls>
  <source src="/static/files/cluttered-environment-task.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

Experimental data was collected for 20 participants, each performing 120 trials where we manipulated the setup of the obstacles to investigate certain behaviours. 
In conjunction with the data collection, a computational model was created to describe a high level process by which humans could select which obstacles to move given a layout, which works on assessing where the gaps between obstacles are and whether the participant needs to interact with obstacles to give a useable path to the target.

Read the full [paper](https://ieeexplore.ieee.org/abstract/document/9196665) on Human-Like Computing in the 2020 IEEE International Conference on Robotics and Automation (ICRA)!