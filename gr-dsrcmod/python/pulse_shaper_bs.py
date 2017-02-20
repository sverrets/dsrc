#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 Jonathan Hansen.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class pulse_shaper_bs(gr.interp_block):
    """
    docstring for block pulse_shaper_bs
    """
    def __init__(self, v_min, v_max, phase, pulse_shaper_interpolation):
        gr.interp_block.__init__(self,
            name="pulse_shaper_bs",
            in_sig=[numpy.int8],
            out_sig=[numpy.short], interp=pulse_shaper_interpolation)
	self.min = v_min
	self.max = v_max
	self.phase = phase
	self.ps_interpolation = pulse_shaper_interpolation


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
	ninput_items = len(output_items[0]) / self.ps_interpolation
	
	#print "ps_interpolation = "+str(self.ps_interpolation)
	#print "ninput_items = "+str(ninput_items)

	HALF_SIN_LENGTH = 256
	half_sin = (0,   25,   50,   75,  100,  125,  150,  175, \
	200,  225,  250,  275,  300,  325,  349,  374, \
	399,  423,  448,  472,  497,  521,  545,  569, \
	593,  617,  641,  665,  688,  712,  735,  759, \
	782,  805,  828,  851,  874,  896,  919,  941, \
	963,  985, 1007, 1029, 1050, 1072, 1093, 1114, \
	1135, 1155, 1176, 1196, 1216, 1236, 1256, 1276, \
	1295, 1315, 1334, 1352, 1371, 1389, 1408, 1426, \
	1443, 1461, 1478, 1495, 1512, 1529, 1545, 1561, \
	1577, 1593, 1608, 1624, 1639, 1653, 1668, 1682, \
	1696, 1710, 1723, 1736, 1749, 1762, 1774, 1786, \
	1798, 1810, 1821, 1832, 1843, 1853, 1863, 1873, \
	1883, 1892, 1901, 1910, 1919, 1927, 1935, 1942, \
	1949, 1956, 1963, 1970, 1976, 1981, 1987, 1992, \
	1997, 2002, 2006, 2010, 2014, 2017, 2020, 2023, \
	2025, 2027, 2029, 2031, 2032, 2033, 2034, 2034, \
	2034, 2034, 2033, 2032, 2031, 2029, 2027, 2025, \
	2023, 2020, 2017, 2014, 2010, 2006, 2002, 1997, \
	1992, 1987, 1981, 1976, 1970, 1963, 1956, 1949, \
	1942, 1935, 1927, 1919, 1910, 1901, 1892, 1883, \
	1873, 1863, 1853, 1843, 1832, 1821, 1810, 1798, \
	1786, 1774, 1762, 1749, 1736, 1723, 1710, 1696, \
	1682, 1668, 1653, 1639, 1624, 1608, 1593, 1577, \
	1561, 1545, 1529, 1512, 1495, 1478, 1461, 1443, \
	1426, 1408, 1389, 1371, 1352, 1334, 1315, 1295, \
	1276, 1256, 1236, 1216, 1196, 1176, 1155, 1135, \
	1114, 1093, 1072, 1050, 1029, 1007,  985,  963, \
	941,  919,  896,  874,  851,  828,  805,  782, \
	759,  735,  712,  688,  665,  641,  617,  593, \
	569,  545,  521,  497,  472,  448,  423,  399, \
	374,  349,  325,  300,  275,  250,  225,  200, \
	175,  150,  125,  100,   75,   50,   25,    0)

	half_sin2 = (25,   50,   75,  100,  126,  151,  176,  201, \
     226,  251,  276,  301,  325,  350,  375,  400, \
     424,  449,  473,  498,  522,  546,  570,  595, \
     619,  642,  666,  690,  714,  737,  760,  784, \
     807,  830,  853,  876,  898,  921,  943,  965, \
     988, 1009, 1030, 1052, 1073, 1095, 1116, 1137, \
    1158, 1178, 1199, 1219, 1239, 1259, 1279, 1298, \
    1318, 1337, 1356, 1374, 1393, 1411, 1429, 1447, \
    1465, 1482, 1499, 1516, 1533, 1550, 1566, 1582, \
    1598, 1614, 1629, 1644, 1659, 1673, 1688, 1702, \
    1716, 1729, 1743, 1756, 1768, 1781, 1793, 1805, \
    1817, 1828, 1839, 1850, 1861, 1871, 1881, 1891, \
    1901, 1910, 1919, 1927, 1936, 1944, 1951, 1959, \
    1966, 1973, 1979, 1986, 1992, 1997, 2003, 2008, \
    2012, 2017, 2021, 2025, 2028, 2032, 2035, 2037, \
    2039, 2041, 2043, 2045, 2046, 2046, 2047, 2047, \
    2047, 2046, 2046, 2045, 2043, 2041, 2039, 2037, \
    2035, 2032, 2028, 2025, 2021, 2017, 2012, 2008, \
    2003, 1997, 1992, 1986, 1979, 1973, 1966, 1959, \
    1951, 1944, 1936, 1927, 1919, 1910, 1901, 1891, \
    1881, 1871, 1861, 1850, 1843, 1834, 1826, 1818, \
    1810, 1802, 1793, 1784, 1776, 1769, 1761, 1753, \
    1745, 1738, 1731, 1726, 1720, 1714, 1709, 1704, \
    1698, 1693, 1688, 1682, 1677, 1672, 1667, 1662, \
    1657, 1652, 1648, 1643, 1638, 1633, 1629, 1624, \
    1620, 1616, 1611, 1607, 1603, 1599, 1595, 1591, \
    1587, 1583, 1580, 1576, 1572, 1569, 1565, 1562, \
    1559, 1555, 1552, 1549, 1546, 1543, 1540, 1538, \
    1535, 1532, 1530, 1527, 1525, 1523, 1520, 1518, \
    1516, 1514, 1512, 1511, 1509, 1507, 1506, 1504, \
    1503, 1502, 1500, 1499, 1498, 1497, 1496, 1495, \
    1495, 1494, 1494, 1493, 1493, 1492, 1492, 1492)

	#print half_sin
	#print half_sin2

	step_length = (HALF_SIN_LENGTH * 2) / self.ps_interpolation
	#print "Step length (128): "+str(step_length) 
	TABLE_LEVEL = 2047
	scaling = float(self.max - self.min) / (TABLE_LEVEL *2)
	#print "Scaling(1): "+str(scaling)
	DC_offset = float(self.min) + TABLE_LEVEL * scaling + 0.5
	#print "DC_offset(0.5): "+str(DC_offset)

	#Verify that the interpolation factor is within range
  	assert (self.ps_interpolation >= 4 and self.ps_interpolation <= 512)
  	#Verify that the interpolation factor is dividable by 2
  	assert (self.ps_interpolation % 2 == 0)
  	#and that (HALF_SIN_LENGTH * 2) / interpol_fac is a valid int
  	assert ((HALF_SIN_LENGTH * 2) % self.ps_interpolation == 0)
  	#Verify that "sign" has a correct value
  	assert (self.phase == -1 or self.phase == 1)

        # <+signal processing here+>

	for i in range(ninput_items):
		if(in0[i]==0):
			for j in range(self.ps_interpolation/2):
				out[self.ps_interpolation*i+j] = half_sin[step_length*j] * self.phase * scaling + DC_offset
				if(out[self.ps_interpolation*i+j] < 0):
					out[self.ps_interpolation*i+j] = out[self.ps_interpolation*i+j] - 1
			for j in range(self.ps_interpolation/2, self.ps_interpolation):
				out[self.ps_interpolation*i+j] = -half_sin[step_length*j - HALF_SIN_LENGTH] * self.phase * scaling + DC_offset
				if(out[self.ps_interpolation*i+j] < 0):
					out[self.ps_interpolation*i+j] = out[self.ps_interpolation*i+j] - 1
		elif(in0[i]==1):
			for j in range(self.ps_interpolation/2):
				out[self.ps_interpolation*i+j] = half_sin2[step_length*j] * self.phase * scaling + DC_offset
				if(out[self.ps_interpolation*i+j] < 0):
					out[self.ps_interpolation*i+j] = out[self.ps_interpolation*i+j] - 1
			for j in range(self.ps_interpolation/2, self.ps_interpolation):
				out[self.ps_interpolation*i+j] = half_sin2[HALF_SIN_LENGTH*2 - step_length*j -1] * self.phase * scaling + DC_offset
				if(out[self.ps_interpolation*i+j] < 0):
					out[self.ps_interpolation*i+j] = out[self.ps_interpolation*i+j] - 1
			self.phase = -self.phase

        #out[:] = in0
	#print out
        return len(output_items[0])

