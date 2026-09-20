#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 12:25:46 2026
@author: oddi80
"""

"""
Beregningsgrunnlag for kostnader el/bensin bil
"""
km_per_år = 10000         #km

forsikring_el = 5000      # kr/år
forsikring_bensin = 7500  # kr/år

avgift_el = 8.38          # kr/dag
avgift_bensin = 8.38      # kr/dag

forbruk_el = 0.2          # kWh/km
strømpris  = 2.0          # kr/kWh
forbruk_bensin = 1.0      # kr/km

bomavgift_el = 0.1        # kr/km
bomavgift_bensin = 0.3    # kr/km

"""
Årlige totalkostnader for el/bensin bil per år
pluss kostnadsdifferansen.
"""
total_el = forsikring_el \
         + avgift_el * 365 \
         + bomavgift_el * km_per_år \
         + forbruk_el * km_per_år * strømpris
         
total_bensin = forsikring_bensin \
    + avgift_bensin \
    + bomavgift_bensin \
    + forbruk_bensin * km_per_år
    
differanse = total_bensin - total_el

print("Årlige kostnader for el-bil: ", total_el, "kr")
print("Årlige kostnader for bensin-bil: ", total_bensin, "kr")
print("Kostnadsdifferense bensin - el-bil:", differanse,"kr")