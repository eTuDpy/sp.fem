# -*- coding: utf-8 -*-
"""
Some linear solvers for the system Ax=b.

@author: Tom Gustafsson
"""

import scipy.sparse as sp
import scipy.sparse.linalg as spl
import numpy as np

def cg(A,b,tol,maxiter,pc="diag",verbose=True):
    print "Starting conjugate gradient with preconditioner \""+pc+"\"..."
    
    def callback(x):
        print "- Vector-2 norm: "+str(np.linalg.norm(x))

    if pc=="diag":
        # diagonal preconditioner
        M=sp.spdiags(1/(A.diagonal()),0,A.shape[0],A.shape[1])
    
    if verbose:
        u=spl.cg(A,b,maxiter=maxiter,M=M,tol=tol,callback=callback)
    else:
        u=spl.cg(A,b,maxiter=maxiter,M=M,tol=tol)

    if verbose:
        if u[1]==0:
            print "Achieved tolerance "+str(tol)+"."
        elif u[1]>0:
            print "Maximum number of iterations "+str(maxiter)+" reached."
        
    return u[0]