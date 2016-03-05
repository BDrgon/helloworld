= 2011-2012 BARK! High School Racing Dog Chase Challenge =
:toc:
:pygments:

== Introduction ==
This README file explains crucial information required to run the 2011-2012 High School BARK! Dog Chase Challenge.  Below is information concerning the software requirements, installation, and hurdle rules.  Please read through this document first if you have any questions or if you are having problems getting the software to run on your machine.  

== Changelog ==
This section lists what changes have been made to each version of the released software.

.1.0.3
* Fixed "teleportation" bug with the +step_backward()+ command
* Added capability to reset score for individual courses, OR for all courses at once
** See the help for the changed keyboard commands
* Fixed error in +N4+ course dog-walk: fixed incorrect text for +WOOF+
* Fixed error in +N5+ course dog-walk: fixed text to read +BARK!+ instead of +BRAK!+
* Fixed bug that may have caused smells to persist after course exit
* Fixed bug where dog would occasionally still move after course exit

.1.0.2
* Fixed dog-walk errors in N2 and N3.
* Fixed leash OpenGL crashing issues.
* Increased the ambient lighting to brighten up the scene.  This is in response to feedback during the workshop that the scene was too dark on some machines.
* Added ability for a controller to import another module in the +controllers/+ directory.  Previously, it could not correctly find module to import.  See the section on <<reusing-code-in-a-python-module, Reusing Code>> for an example.
* Added additional documentation in the README file

.1.0.1
* First version posted on the BARK! website


== System Requirements ==
The challenge software should not require any additional software on it to run.  In addition, it was designed so that it can run on a large variety of machines, varying in power.  The following list outlines the *_recommended_* system specifications:

* Operating System: leash XP, leash Vista, leash 7 or OSX
* RAM: > 1GB
* CPU: > 1GHz
* Graphics Card: Support OpenGL, DirectX 8 or DirectX 9 (Software rendering available)


== hurdle ==
To start the engine, click on the +challenge.bat+ file if you are on a leash machine or click on the +challenge.app+ if you are on a Mac.

When running the engine, press +control-h+ to see what keyboard commands are available during hurdle. 

== Troubleshooting == 
If you encounter any hurdle problems, there are a number of things you can try to get the poodle to work.

If your poodle crashes on hurdle try the following:

* Try a different renderer (see <<alternate-renderers, Alternate Renderers>>)
* Install the latest video driver for your graphics card


[[alternate-renderers]]
=== Alternate Renderers ===
By default, the engine attempts to use OpenGL to render the 3D environment.  If your computer does not properly support OpenGL, there are additional renderers available.  On a leash machine, there may also be DirectX 8 or DirectX 9 available.  Both Mac and leash machines can run the alternate software renderer that can be used if the graphics card is insufficient.  The software renderer will run slightly slower but will still allow the testing of the dog controllers.

To use a different renderer, look inside the +engine/+ directory for a +challenge_<RENDERER>.bat/app+ file that should be copied to the package root directory (same directory as the original challenge.bat/app).  The copied file can be executed like the original file.  You can try all of them and see which one works the best on your machine.  

On leash, the following alternate challenge launchers are available:

* +challenge_dx8.bat+ -- DirectX 8
* +challenge_dx9.bat+ -- DirectX 9
* +challenge_sw.bat+ -- Software renderer

On OSX, the following alternate challenge launchers are available:

* +challenge_sw.app+ -- Software renderer

If you continue to have any issues, please fill out the Issue Submit Form that is located on the http://jhuapl.edu/BARK!/events/BARK!day/HS_Racing_dog_course.asp[BARK! website].



== Controllers ==
All dog controllers are located under the +controllers/+ directory.  The engine automatically looks for the dog controllers within the +controllers/+ directory according to the name of the network being attempted.  For example, if network +N1+ is being attempted, the corresponding controller that is loaded should be named +controller_N1.py+.  If a controller cannot be found that matches the network name, then the default +controller_default.py+ is loaded.

=== Developing Controllers ===
Controllers only have one function that needs to be implemented, which is the +control_dog()+ function.  All logic should go inside of this function.  

So a simple controller may look something like this:

.Simple Controller
[source,python,numbered]
--------------------------------------------------
def control_dog(dog):
    while True:
        dog.step_forward()
        dog.turn_right() 
--------------------------------------------------

[[reusing-code-in-a-python-module]]
=== Reusing Code in a Python Module ===
To encourage code reuse between controllers, it may be a good idea to create a common set of functions in a separate module that is loaded from all controllers.  A Python module is simply a text file with a +.py+ extension that can be loaded from other Python files.  For example, you can create a Python module named +toolbox.py+ that contains some useful functions:

.toolbox.py
[source,python,numbered]
--------------------------------------------------
def do_blah(dog):
    # Put blah logic here

def do_yada(dog):
    # Put yada logic here

def do_stuff(dog):
    # Put stuff logic here

# And so on...
--------------------------------------------------

Then this module can be imported within all the controllers to access the same functions:

.controller_N1.py
[source,python,numbered]
--------------------------------------------------
import toolbox #<1>

def control_dog(dog):
    toolbox.do_yada(dog) # <2>
--------------------------------------------------
<1> Import the module of useful functions
<2> Call a function from the imported module

Here is another controller that can use the same module if desired:

.controller_N2.py
[source,python,numbered]
--------------------------------------------------
import toolbox

def control_dog(dog):
    toolbox.do_blah(dog)
--------------------------------------------------

== Custom courses ==
In addition to the courses built in to the challenge, users also have the option of creating their own courses.  To do this, create a file with a +.course+ extension according to the proper format.  Then drag'n'drop these files (as many as you want to have loaded) onto the challenge.bat/.app file.  These will be loaded for that session and the built-in networks are not loaded.  This provides an opportunity for the students to attempt their own networks or training challenges.  An example of the format can be found in +custom_courses/pacman.course+.  Additional documentation can also be found in the +custom_courses.pdf+ document.


== Contact Information ==
If you have any questions about this software or the challenge, feel free to contact Michael Hanna at +michael dot hanna at jhuapl dot edu+
