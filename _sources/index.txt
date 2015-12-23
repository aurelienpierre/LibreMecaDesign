.. . documentation master file, created by
   sphinx-quickstart on Tue Dec 22 19:03:23 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. |LibreMecaDesign| LMD

Welcome to LibreMecaDesign documentation!
###############################################

LibreMecaDesign is a multi-level library to solve mechanical engineering problems and to help engineers to choose materials for their design. It will :

*  describe mechanical objects with properties :

   *  geometric properties : dimensions, section area, centroids, momentums, etc.
   *  materials properties : elasticity, rigidity, tensile strength, Poissin's ration, etc.
   *  external constrains : forces, momentums, reactions, etc.
   *  internal constrains : stress, strain, shear

*  supercharge these properties with symbolic equations and/or numeric values with units through modules :

   *  beams
   *  shafts
   *  couplings
   *  bearings
   *  gears
   *  springs
   *  screws and bolts
   *  clutches and brakes

*  determine materials properties to solve equations or determine expected properties to chose materials, based on a extensive library
*  gather all properties equations and all properties parameters to solve them :

   *  symbolically to get an input/output relation parameter depending (for a third party use)
   *  formally to get an analytical result without numeric aproximations (if the problem is simple enough)
   *  numerically if the solution is not analytical, by optimization or finite elements

The whole software is intended to be used either as a library in scripts or through an upcoming GUI. Its main goal is to remain as simple and as light as possible, written in an objective way with extensible modules, and higher level methods built on lower level methods, in a multi-layer architecture where only inputs and outputs matter.


Developpers & users reference:

.. toctree::
   
   DEV

Functions reference:

.. toctree::
   
   LMD


Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

