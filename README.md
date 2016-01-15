# LibreMechanicalDesign

https://aurelienpierre.github.io/LibreMecaDesign/

LibreMecaDesign is at first a librairy and then a complete software to assist mechanical engineers to perform computations and analyses in machine design and materials selection.

Written in Python, it is intended to be used either as a librairy in Python script or as a stand-alone GUI software.

The software architecture is layer-style :
* Layer 0 : properties of materials and fluids - gathered in a database and accessible through a simple search (Google style) whose results are stored in a class for later use
* Layer 1 : properties of mechanical objects (beams, gears, etc.) stored into classes and connected by formal equations
        * geometrical properties
        * material properties
        * intern stresses properties
        * external forces properties
* Layer 2 : procedures to compute and connect properties gathered into modules
* Layer 3 : numeric, symbolic and finite differences solver
* Layer 4 : GUI
