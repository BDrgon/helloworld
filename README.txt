= 2011-2012 MESA High School Virtual Robot Challenge =
:toc:
:pygments:

== Introduction ==
This README file explains crucial information required to run the 2011-2012 High School MESA Cyber Challenge.  Below is information concerning the software requirements, installation, and execution rules.  Please read through this document first if you have any questions or if you are having problems getting the software to run on your machine.  

== Changelog ==
This section lists what changes have been made to each version of the released software.

.1.0.3
* Fixed "teleportation" bug with the +step_backward()+ command
* Added capability to reset score for individual levels, OR for all levels at once
** See the help for the changed keyboard commands
* Fixed error in +N4+ maze cipher: fixed incorrect ciphertext for +OCEAN CITY+
* Fixed error in +N5+ maze cipher: fixed ciphertext to read +INNJTOM+ instead of +INMJROM+
* Fixed bug that may have caused sensor beams to persist after level exit
* Fixed bug where robot would occasionally still move after level exit

.1.0.2
* Fixed cipher errors in N2 and N3.
* Fixed Windows OpenGL crashing issues.
* Added ability to run challenge engine with different rendering options (OpenGL=default, DirectX 8, Directx 9, Software).  See the section on <<alternate-renderers, Alternate Renderers>>.
* Increased the ambient lighting to brighten up the scene.  This is in response to feedback during the workshop that the scene was too dark on some machines.
* Added ability for a controller to import another module in the +controllers/+ directory.  Previously, it could not correctly find module to import.  See the section on <<reusing-code-in-a-python-module, Reusing Code>> for an example.
* Added additional documentation in the README file

.1.0.1
* First version posted on the MESA website


== System Requirements ==
The challenge software should not require any additional software on it to run.  In addition, it was designed so that it can run on a large variety of machines, varying in power.  The following list outlines the *_recommended_* system specifications:

* Operating System: Windows XP, Windows Vista, Windows 7 or OSX
* RAM: > 1GB
* CPU: > 1GHz
* Graphics Card: Support OpenGL, DirectX 8 or DirectX 9 (Software rendering available)


== Execution ==
To start the engine, click on the +challenge.bat+ file if you are on a Windows machine or click on the +challenge.app+ if you are on a Mac.

When running the engine, press +control-h+ to see what keyboard commands are available during execution. 

== Troubleshooting == 
If you encounter any execution problems, there are a number of things you can try to get the program to work.

If your program crashes on execution try the following:

* Try a different renderer (see <<alternate-renderers, Alternate Renderers>>)
* Install the latest video driver for your graphics card


[[alternate-renderers]]
=== Alternate Renderers ===
By default, the engine attempts to use OpenGL to render the 3D environment.  If your computer does not properly support OpenGL, there are additional renderers available.  On a Windows machine, there may also be DirectX 8 or DirectX 9 available.  Both Mac and Windows machines can run the alternate software renderer that can be used if the graphics card is insufficient.  The software renderer will run slightly slower but will still allow the testing of the robot controllers.

To use a different renderer, look inside the +engine/+ directory for a +challenge_<RENDERER>.bat/app+ file that should be copied to the package root directory (same directory as the original challenge.bat/app).  The copied file can be executed like the original file.  You can try all of them and see which one works the best on your machine.  

On Windows, the following alternate challenge launchers are available:

* +challenge_dx8.bat+ -- DirectX 8
* +challenge_dx9.bat+ -- DirectX 9
* +challenge_sw.bat+ -- Software renderer

On OSX, the following alternate challenge launchers are available:

* +challenge_sw.app+ -- Software renderer

If you continue to have any issues, please fill out the Issue Submit Form that is located on the http://jhuapl.edu/mesa/events/mesaday/HS_Virtual_Robot_Maze.asp[MESA website].



== Controllers ==
All robot controllers are located under the +controllers/+ directory.  The engine automatically looks for the robot controllers within the +controllers/+ directory according to the name of the network being attempted.  For example, if network +N1+ is being attempted, the corresponding controller that is loaded should be named +controller_N1.py+.  If a controller cannot be found that matches the network name, then the default +controller_default.py+ is loaded.

=== Developing Controllers ===
Controllers only have one function that needs to be implemented, which is the +control_robot()+ function.  All logic should go inside of this function.  

So a simple controller may look something like this:

.Simple Controller
[source,python,numbered]
--------------------------------------------------
def control_robot(robot):
    while True:
        robot.step_forward()
        robot.turn_right() 
--------------------------------------------------

[[reusing-code-in-a-python-module]]
=== Reusing Code in a Python Module ===
To encourage code reuse between controllers, it may be a good idea to create a common set of functions in a separate module that is loaded from all controllers.  A Python module is simply a text file with a +.py+ extension that can be loaded from other Python files.  For example, you can create a Python module named +toolbox.py+ that contains some useful functions:

.toolbox.py
[source,python,numbered]
--------------------------------------------------
def do_blah(robot):
    # Put blah logic here

def do_yada(robot):
    # Put yada logic here

def do_stuff(robot):
    # Put stuff logic here

# And so on...
--------------------------------------------------

Then this module can be imported within all the controllers to access the same functions:

.controller_N1.py
[source,python,numbered]
--------------------------------------------------
import toolbox #<1>

def control_robot(robot):
    toolbox.do_yada(robot) # <2>
--------------------------------------------------
<1> Import the module of useful functions
<2> Call a function from the imported module

Here is another controller that can use the same module if desired:

.controller_N2.py
[source,python,numbered]
--------------------------------------------------
import toolbox

def control_robot(robot):
    toolbox.do_blah(robot)
--------------------------------------------------

== Custom Mazes ==
In addition to the mazes built in to the challenge, users also have the option of creating their own mazes.  To do this, create a file with a +.maze+ extension according to the proper format.  Then drag'n'drop these files (as many as you want to have loaded) onto the challenge.bat/.app file.  These will be loaded for that session and the built-in networks are not loaded.  This provides an opportunity for the students to attempt their own networks or crypto challenges.  An example of the format can be found in +custom_mazes/pacman.maze+.  Additional documentation can also be found in the +custom_mazes.pdf+ document.


== Contact Information ==
If you have any questions about this software or the challenge, feel free to contact Michael Hanna at +michael dot hanna at jhuapl dot edu+
