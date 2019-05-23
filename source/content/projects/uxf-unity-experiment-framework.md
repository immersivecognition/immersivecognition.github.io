---
name: UXF: Unity Experiment Framework
description: An open source package for the Unity3D game engine that can be used to assist the development of virtual reality human behaviour experiments.
image: uxf.png
github: immersivecognition/unity-experiment-framework
website: https://immersivecognition.github.io/unity-experiment-framework/
---


![](/static/files/uxf-banner.png)

# Studying Human Behaviour with Virtual Reality: The Unity Experiment Framework

Virtual Reality systems offer a powerful tool for human behaviour research. The ability to create three-dimensional visual scenes and measure responses to the visual stimuli enables the behavioural researcher to test hypotheses in a manner and scale that were previously unfeasible. For example, a researcher wanting to understand interceptive timing behaviour might wish to violate Newtonian mechanics, so objects move in novel 3D trajectories. The same researcher may wish to collect such data with hundreds of participants outside the laboratory, and the use of a VR headset makes this a realistic proposition. The difficulty facing the researcher is that sophisticated 3D graphics engines (e.g. Unity) have been created for game designers rather than behavioural scientists.

In order to overcome this barrier, we have created a set of tools and programming syntaxes that allow logical encoding of the common experimental features required by the behavioural scientist. The Unity Experiment Framework (UXF) allows the researcher to readily implement several forms of data collection, and provides researchers with the ability to easily modify independent variables. UXF does not offer any stimulus presentation features, so the full power of the Unity game engine can be exploited. We use a case study experiment, measuring postural sway in response to an oscillating virtual room, to show how UXF can replicate and advance upon behavioural research paradigms. We show that UXF can simplify and speed up development of VR experiments created in commercial gaming software and facilitate the efficient acquisition of large quantities of behavioural research data.

Read the full [paper](https://link.springer.com/article/10.3758%2Fs13428-019-01242-0) on UXF in Behaviour Research Methods!

# Features

* **Data collection:** Automates the process of collecting the variables you define within your task, and stores them simple CSV files.
* **Continuous measures:** Time-series data such as the position and rotation of an object can be easily acquired and split into one file per trial.
* **Settings system:** Allows you to programmatically define independent variables for your session, blocks and trials.
* **User Interface:** Includes a pre-built UI for allowing the researcher to view and enter information about the session.
* **Multithreaded:** All file IO tasks are performed concurrently in a separate thread to avoid any drops in framerate.
* **Built for VR:** UXF works with any Unity project but is designed specifically for virtual reality human behaviour experiments.


### Example experiment built in UXF

In this experiment, we are manipulating the error and reward rates of two targets. We are investigating how people learn from mistakes, i.e. which types of error cause people to change their decision? VR allows us to easily hide the participant's hand, so we can effectively manipulate errors. With UXF we can simplify the creation of these experiments and easily obtain the behavioural and kinematic data that we require.

<video controls>
  <source src="/static/files/uxf-example-task.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

