# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:48:17 2024

@author: smithlt
"""


import fenics
from fenics import *
import numpy as np
import pyCOMSOL
import matplotlib.pyplot as plt
import mpi4py

mesh = UnitSquareMesh(64,64)

V = FunctionSpace(mesh, 'P', 1)
W = FunctionSpace(mesh, 'P', 1)

epsilon_r = Expression('1 + 0.5*sin(x[0]*x[1])', degree=2)
mu_r = Expression('1 + 0.5*cos(x[0]*x[1])', degree=2)

#source
E_in = Constant(1.0)

#boundary conditions
boundary = DirichletBC(V, E_in, 'on_boundary')

u = TrialFunction(V)
v = TestFunction(V)
a = inner(epislon_r*grad(u), grad(v)) * dx
L = inner(Constant(0), v) * dx

E = Function(V)
solve(a == L, E, boundary)

plt.plot(E)
plt.show()