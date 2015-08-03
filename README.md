# Mouse Recorder
###A cheap, modular, behavior recording program
![](http://s16.postimg.org/yek83sdv9/Mouserecord_logo.jpg 2)

# Purpose

The program's is designed to record rodent behavior at specific intervals of time, based on the initiation of a trigger event (e.g., the press of a lever.) Moreover, the program operates through Raspberry Pi-based system to significantly reduce cost as opposed to conventional recording apparatus.

# Building

To install, use standard python installation procedure:
    python setup.py install
    



# Testing


# Usage

Once desired arguments are provided by the user -recording times-before and after in seconds- and directory, the program will initiate. Simply run `docker run -it <NAME>`. This will start up `bash`. In the case of an automated build, `<NAME>` is `jakirkham/ubuntu_conda`.


##Sample Usage
Execution of the program consists of the program name and respectve arguments: time to record before trigger event (in seconds), time to record after (in seconds), and directory of the file to be saved into. An example is shown below:

`./mouse_recorder.py 2 2 /home/pi/Desktop/`
