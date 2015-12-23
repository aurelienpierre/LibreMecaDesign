LibreMecaDesign : Developpers introduction
################################################

Goal and purpose
================

When it comes to engineering and scientific computing, you have many choices between proprietary solutions :

*	CATIA is probably the best CAD software, with a finite elements computing module,
*	Hypermesh is very convenient as a standalone finite elements computing software,
*	EES (Engineering Equations Solver) is very convenient to solve specific (thermofluid) problems with an extensive fluids properties database and asynchronous solver
*	Matlab is an efficient general-purpose matrix computing with built-in IDE

But :

*	None of this programs communicates with the others, which means you have to import/export yourself your programs,
*	All of them are closed-sources softwares, which is pretty bad as an engineer is responsible for his designs and may not want to trust blindly a third-party software,
*	All of them attach the user into their own IDE/GUI making it impossible to use them as librairies or in another IDE,
*	CATIA is heavy and does not work on Linux,
*	EES is quite specific, old and not ready for parallel or cloud computing
*	Matlab does not allow computation with units

I wanted to have a nice computing software with :

*	Extensive materials database,
*	Unit computing,
*	Symbolic computing,
*	A very versatile base with an objective architecture and independant modules,
*	Some open doors for the future, like parallel and cloud computing, CAD, optimization and stuff

Here we are...

LibreMecaDesign is currently in its very basic developpement phase. As it is intended to be easily extensible, every part has to stay minimalist.
Thus, it will be organized into layers, from low level to top level.

Coding Philosophy
=================

1.	**One task = One function**. 

	*	Only inputs and outputs matter
	*	Code should be factorized

2.	**Everything stay a symbolic object**.

	*	Thanks to sympy, it's now possible to handle algebraic and symbolic equations into Python
	*	Keeping symbolic equations until the last moment avoid intermediate approximations and allow algebraic solving in some cases
	*	Some users may want formal solutions
	*	Figures are put into the symbols just in time for solving

3.	**Information should be human-readable**.

	*	The revolution of Google was to connect human and knowledge in a fast and easy way
	*	The next revolution will be to connect knowledge and advanced processing the same way (inspired by Stefan Wolfram and the Wolfram Language)

4.	**Every piece of code should be documented before beeing written**
	
	*	An undocumented function is useless and makes a program tricky to debug
	*	When you are able to explain your function before writting it, chances are that your code will be clear and simple

Code layers
===========

Layer 0 : database
******************

First step : creating a nice API to allow anyone to add data in the librairies - DONE !

A module has been written to allow every dummy user to add materials properties just from a template with a simple Excel Spreadsheet and exporting it to CSV. Then, the module take care of the database building while performing some verifications.

Second step : create a search engine to retrieve every material properties from a simple text query (Google-like) and store them for any use - IN PROGRESS

Syntax is outdated and information should be quickly accessible just with words. Especially when your computing is intended to find a material that suits your requirements, you don't want to scroll the table to find your needed yield tensile strength. Materials properties will be accessible without fancy parameters.

Layer 1 : classes and container
*******************************

Each object will be described by a container or meta-class. This container will gather classes that will store properties as numbers or symbolic equations :

#.	Class Geometry
#.	Class Materials
#.	Class Forces
#.	Class Constraints
#.	Class whatever...

Layer 2 : modules
*****************

The modules will allow users to set operating conditions such as forces, torques, moments thus equations that build links between the properties of the object.

#.  beams
#.  shafts
#.  couplings
#.  bearings
#.  gears
#.  springs
#.  screws and bolts
#.  clutches and brakes
#.	Castigliano method

Layer 3 : solver
****************

Layer 4 : GUI
*************

Layer 5 : CAD
*************

