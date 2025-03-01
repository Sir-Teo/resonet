
import glob
import os

"""
Some constants and file paths for simulations
"""

# this file contains the P1 amplitudes used to simulate diffraction
# these files are slow to read: TODO convert and store in high symmetry and use CCTBX
# to convert to P1

dirname = os.environ.get("RESONET_SIMDATA")

# these are scattering profiles for random plastics (from James Holton)
RANDOM_STOLS = glob.glob(os.path.join(dirname, "randomstols/*stol"))
# scattering profiles for air and water
AIR_STOL = os.path.join(dirname, "air.stol")
WATER_STOL = os.path.join(dirname, "water.stol")
STOL_MIN = 0.025
STOL_MAX = 0.35
STOL_RNG = STOL_MAX-STOL_MIN

BEAM_SIZE_MM = 0.03
FLUX = 4e11  # photons per pulse
DIVERGENCE_MRAD = 0.02
XTALSIZE_MM = 0.025
DOMAINSIZE_MM = 5e-5
VOL = (XTALSIZE_MM / DOMAINSIZE_MM)**3  # scales the diffraction
FIX_RES = None # 0.5/.29989  # optionally fix the resolution for all simulations ...


# these are the PDB folders containing pdb files and P1.hkl files
RANDOM_PDBS = [d for d in glob.glob(os.path.join(dirname, "pdbs/*")) if len(os.path.basename(d))==4 and os.path.isdir(d)]

# mosaicity bounds (degrees)
MOS_MIN = 0.001
MOS_MAX = 0.01

