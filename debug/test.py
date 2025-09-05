import numpy as np
from ase.io import read, write
import time
from fairchem.core import pretrained_mlip, FAIRChemCalculator

from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
from ase.md import Langevin


import os

predictor = pretrained_mlip.get_predict_unit("uma-s-1", device="cuda", expose_feat=True)

calc = FAIRChemCalculator(predictor, task_name="omat", expose_feat=True)

snap = read("H2O.xyz")

snap.calc = calc

snap.get_potential_energy()
snap.get_forces()
print(snap.calc.results)

