# Newton solver

[![Build Status](https://github.com/olivierverdier/newton/actions/workflows/python_package.yml/badge.svg?branch=main)](https://github.com/olivierverdier/newton/actions/workflows/python_package.yml?query=branch%3Amain)
![Python version](https://img.shields.io/badge/Python-3.9,_3.10,_3.11,_3.12-blue.svg?logo=python)
[![codecov](https://codecov.io/github/olivierverdier/newton/graph/badge.svg?token=Ea4XsTXw6A)](https://codecov.io/github/olivierverdier/newton)

A simple nonlinear solver which uses [`fsolve`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html#fsolve) in general, and switches to a homemade Newton solver in case `fsolve` fails.
