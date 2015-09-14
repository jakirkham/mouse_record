[![Code Health](https://landscape.io/github/DudLab/mouse_record/master/landscape.svg?style=flat)](https://landscape.io/github/DudLab/mouse_record/master)

# Mouse Recorder

###A cheap, modular, behavior recording program

![Mouserecord_logo.jpg](Mouserecord_logo.jpg)


# Purpose

The program's is designed to record rodent behavior at specific intervals of time, based on the initiation of a trigger event (e.g., the press of a lever.


# Installation

Installation requires [`setuptools`](https://pypi.python.org/pypi/setuptools); install using the following command (may require `sudo`):

    python setup.py install

# Testing

Test the program using the following command:

    python setup.py tests

# Usage

##Picture Usage

Execution of the program consists of the program name and a single argument, the directory in which the picture is to be saved into.

    mouse-picture ~/Destkop

##Preview Usage

Execution of the program consists of the program name and a single argument: the time desired length of the camera preview (in seconds). Additionally, the user can exit at any time by entering `Ctrl + c`

    mouse-preview 60

##Recorder Usage

Execution of the program consists of the program name and respectve arguments: time to record before trigger event (in seconds), time to record after (in seconds), and directory of the file to be saved into. An example is shown below:

    sudo mouse-record 2 2 /home/pi/Desktop

Also, as mentioned before, the program will end when a `KeyboardInterrupt`(Ctrl + c) is entered into the terminal.

