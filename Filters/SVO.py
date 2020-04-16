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
    
    url = 'http://svo2.cab.inta-csic.es/theory/fps/getdata.php?format=ascii&id='+SVOid
    f = urllib.urlopen(url)
    DataLines = f.readlines()
    
    Wavel = [] # m
    Trans = []
    for i in range(len(DataLines)):
        tempLine = DataLines[i].split(' ')
        Wavel += [float(tempLine[0])*1e-10] # m
        Trans += [float(tempLine[1][:-2])]
    Wavel = np.array(Wavel) # m
    Trans = np.array(Trans)
    
    tempFilter = Filter.Filter(SVOid,
                               Wavel,
                               Trans)
    if (SummaryPlots == True):
        tempFilter.SummaryPlot()
    
    return tempFilter
