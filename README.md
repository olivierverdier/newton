# Newton solver

[![Build Status](https://img.shields.io/travis/olivierverdier/newton/master.svg)](https://travis-ci.org/olivierverdier/newton) [![Coverage Status](https://img.shields.io/coveralls/olivierverdier/newton/master.svg)](https://coveralls.io/r/olivierverdier/newton?branch=master)

A simple nonlinear solver which uses [`fsolve`](http://docs.scipy.org/doc/scipy-0.7.x/reference/generated/scipy.optimize.fsolve.html) in general, and switches to a homemade Newton solver in case `fsolve` fails.
