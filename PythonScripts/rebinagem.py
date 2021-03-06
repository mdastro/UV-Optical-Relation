#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Data Reduction and Adjustments
    @author:  Maria Luiza Linhares Dantas
    @date:    2016.07.06
    @version: 0.0.3
    This program makes the new binning for one all the spectra of our sample.
    
    This version: paths updated, as well as filelist. 
"""
# ======================================================================================================================

from __future__ import division
import numpy as np
import scipy.interpolate as s
import os

# ======================================================================================================================

# Main thread ----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    spec_files_path = '/home/mldantas/Dropbox/MSc_paper/Dataset/Individual_Spectra'
    new_specs_path  = '/home/mldantas/Dropbox/MSc_paper/Dataset/Rebinned_Spec_SelfZ'
    filelist        = '/home/mldantas/Dropbox/MSc_paper/Dataset/filelist_individual_spectra.txt'

    filelist = np.loadtxt(filelist, dtype=str)

    for spec_file in filelist:
        basename = os.path.split(spec_file)[-1]              # Get filename
        basename = os.path.splitext(basename)[0]           # Remove file extension

        wavelength = np.loadtxt(os.path.join(spec_files_path, spec_file), usecols=[0])
        flux = np.loadtxt(os.path.join(spec_files_path, spec_file), usecols=[1])

        interp_function = s.interp1d(wavelength, flux)
        new_wavelength = np.linspace(wavelength.min(), wavelength.max(), 9000)
        new_wavelength = np.arange(wavelength.min(), wavelength.max(), 1)
        new_flux = np.arange(flux.min(), flux.max(), 9000)
        new_flux = interp_function(new_wavelength)

        np.savetxt((os.path.join(new_specs_path, basename+'.txt')), np.column_stack((new_wavelength, new_flux)),
                   fmt='%s', delimiter='       ', header='wavelength   flux', comments='#')

__author__ = 'mldantas'
