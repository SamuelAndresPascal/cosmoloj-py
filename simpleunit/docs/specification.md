# Simple Unit - specification

Whereas most of the unit converter tools proposes conversions between a defined set of units, *Simple Unit* 
[@simpleunit] only represents *what* units are and *how* they are defined, allowing the library consumer to define 
its own units. So, the user is not limited by a predefined set of units neither by a string representation. Units are 
simply represented by objects in the code.

There are three kind of units defined by the *Simple Unit* specification. A *fundamental unit* is defined by itself. A
*transformed unit* is defined from another unit (called its *reference unit*), applying an affine operation. The
*reference* can be a unit of any kind (fundamental, transformed or derived). A *derived unit* is defined from a set 
(a product) of units raised to a rational power. Each unit raised to a rational power is called a *factor*. All the 
units *are* factor of themselves raised to the rational power 1.

Although the *Simple Unit* specification is lighter than the Unit API Java specification, the principle of unit
representation is the same : units and converters are objects that have to be defined by the user.

