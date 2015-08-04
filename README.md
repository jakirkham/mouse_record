# Mouse Recorder
###A cheap, modular, behavior recording program
![](http://s16.postimg.org/yek83sdv9/Mouserecord_logo.jpg 2)

# Purpose

The program's is designed to record rodent behavior at specific intervals of time, based on the initiation of a trigger event (e.g., the press of a lever.) Moreover, the program operates through Raspberry Pi-based system to significantly reduce cost as opposed to conventional recording apparatus.

# Building

To install, use standard python installation procedure:
    `python setup.py install`
Additionally, the program requires installation of `setuptools`; the link to the installation instructions is as follows: <https://pypi.python.org/pypi/setuptools>


# Development
`git clone https://github.com/bnhwa/mouse_record`
`git develop`



# Testing
not implemented yet


# Usage

Once desired arguments are provided by the user -recording times-before and after in seconds- and directory, the program will initiate. Once the program is running, please run the program for at least 30 seconds (to allow the program to prevent extra seconds from entering the buffer).


##Sample Usage

Execution of the program consists of the program name and respectve arguments: time to record before trigger event (in seconds), time to record after (in seconds), and directory of the file to be saved into. An example is shown below:

`mouse-record 2 2 /home/pi/Desktop/`
