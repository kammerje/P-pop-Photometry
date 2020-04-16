"""
# =============================================================================
# P-POP PHOTOMETRY
# A photometry tool for P-POP
# =============================================================================
"""


# =============================================================================
# IMPORTS
# =============================================================================

import numpy as np
import urllib

import Filter


# =============================================================================
# SVO
# =============================================================================

def getFilter(SVOid,
              SummaryPlots):
    """
    Parameters
    ----------
    SVOid: str
        Filter identifier from the Spanish Virtual Observatory.
    SummaryPlots: bool
            If True, makes summary plots after importing a module.
    
    Returns
    -------
    Filter: instance
        Instance of class Filter.
    """
    
    if ('F560W' in SVOid):
        temp = np.load('Filters/F560W.npy', allow_pickle=True)
        Name = 'F560W'
    elif ('F1000W' in SVOid):
        temp = np.load('Filters/F1000W.npy', allow_pickle=True)
        Name = 'F1000W'
    elif ('F1500W' in SVOid):
        temp = np.load('Filters/F1500W.npy', allow_pickle=True)
        Name = 'F1500W'
    
    Wavel = temp[0]*1e-6 # m
    Trans = temp[1]
    Mean = temp[2]*1e-6 # m
    Width = temp[3]*1e-6 # m
    
    tempFilter = Filter.Filter(Name,
                               Wavel,
                               Trans,
                               Mean,
                               Width)
    if (SummaryPlots == True):
        tempFilter.SummaryPlot()
    
    return tempFilter
