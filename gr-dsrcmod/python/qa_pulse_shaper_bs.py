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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from pulse_shaper_bs import pulse_shaper_bs

class qa_pulse_shaper_bs (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
	print "-------TEST 1------------"
        # set up fg
	src_data = (0, 1, 0, 1, 0)
	expected_result = (0, 2034, 0, -2034, 25, 2047, 1492, 2047, 0, -2034, 0, 2034, -25, -2047, -1492, -2047, 0, 2034, 0, -2034)
	src = blocks.vector_source_b (src_data)
	pulse_shaper = pulse_shaper_bs (-2047, 2047, 1, 4) # (v_min, v_max, sign[+/-1], interpolation)
	dst = blocks.vector_sink_s ()
	self.tb.connect (src, pulse_shaper)
	self.tb.connect (pulse_shaper, dst)

        self.tb.run ()
        # check data
	result_data = dst.data ()
	self.assertEqual (expected_result, result_data)

    def test_002_t (self):
	print "-------TEST 2------------"
        # set up fg
	src_data = (0, 1, 0, 1, 0)
	expected_result = ( \
			0,	399,	782,  1135,	 1443,	1696,  1883,  1997, \
			 2034,	1992,  1873,  1682,	 1426,	1114,	759,   374, \
			0,	-399,  -782, -1135, -1443, -1696, -1883, -1997, \
			-2034, -1992, -1873, -1682, -1426, -1114,  -759,  -374, \
			   25,	 424,	807,  1158,	 1465,	1716,  1901,  2012, \
			 2047,	2003,  1881,  1745,	 1657,	1587,  1535,  1503, \
			 1492,	1504,  1538,  1591,	 1662,	1753,  1891,  2008, \
			 2047,	2008,  1891,  1702,	 1447,	1137,	784,   400, \
			0,	-399,  -782, -1135, -1443, -1696, -1883, -1997, \
			-2034, -1992, -1873, -1682, -1426, -1114,  -759,  -374, \
			0,	 399,	782,  1135,	 1443,	1696,  1883,  1997, \
			 2034,	1992,  1873,  1682,	 1426,	1114,	759,   374, \
			  -25,	-424,  -807, -1158, -1465, -1716, -1901, -2012, \
			-2047, -2003, -1881, -1745, -1657, -1587, -1535, -1503, \
			-1492, -1504, -1538, -1591, -1662, -1753, -1891, -2008, \
			-2047, -2008, -1891, -1702, -1447, -1137,  -784,  -400, \
			0,	 399,	782,  1135,	 1443,	1696,  1883,  1997, \
			 2034,	1992,  1873,  1682,	 1426,	1114,	759,   374, \
			0,	-399,  -782, -1135, -1443, -1696, -1883, -1997, \
			-2034, -1992, -1873, -1682, -1426, -1114,  -759,  -374)
	src = blocks.vector_source_b (src_data)
	pulse_shaper = pulse_shaper_bs (-2047, 2047, 1, 32) # (v_min, v_max, sign[+/-1], interpolation)
	dst = blocks.vector_sink_s ()
	self.tb.connect (src, pulse_shaper)
	self.tb.connect (pulse_shaper, dst)

        self.tb.run ()
        # check data
	result_data = dst.data ()
	self.assertEqual (expected_result, result_data)

    def test_003_t (self):
	print "-------TEST 3------------"
        # set up fg
	src_data = (0, 1, 0, 1, 0)
	expected_result = (1500, 1997, 1500, 1003, 1506, 2000, 1864, 2000, 1500, \
			1003, 1500, 1997, 1494, 1000, 1136, 1000, 1500, 1997, 1500, 1003)
	src = blocks.vector_source_b (src_data)
	pulse_shaper = pulse_shaper_bs (1000, 2000, 1, 4) # (v_min, v_max, sign[+/-1], interpolation)
	dst = blocks.vector_sink_s ()
	self.tb.connect (src, pulse_shaper)
	self.tb.connect (pulse_shaper, dst)

        self.tb.run ()
        # check data
	result_data = dst.data ()
	self.assertEqual (expected_result, result_data)

    def test_004_t (self):
	print "-------TEST 4------------"
        # set up fg
	src_data = (0, 1, 0, 1, 0)
	expected_result = ( \
			3456, 3889, 4305, 4688, 5022, 5297, 5500, 5624, \
            5664, 5618, 5489, 5282, 5004, 4665, 4280, 3862, \
            3456, 3023, 2607, 2224, 1890, 1615, 1412, 1288, \
            1248, 1294, 1423, 1630, 1908, 2247, 2632, 3050, \
            3483, 3916, 4332, 4713, 5046, 5319, 5520, 5640, \
            5678, 5630, 5498, 5350, 5255, 5179, 5122, 5087, \
            5076, 5089, 5125, 5183, 5260, 5359, 5509, 5636, \
            5678, 5636, 5509, 5304, 5027, 4690, 4307, 3890, \
            3456, 3023, 2607, 2224, 1890, 1615, 1412, 1288, \
            1248, 1294, 1423, 1630, 1908, 2247, 2632, 3050, \
            3456, 3889, 4305, 4688, 5022, 5297, 5500, 5624, \
            5664, 5618, 5489, 5282, 5004, 4665, 4280, 3862, \
            3429, 2996, 2580, 2199, 1866, 1593, 1392, 1272, \
            1234, 1282, 1414, 1562, 1657, 1733, 1790, 1825, \
            1836, 1823, 1787, 1729, 1652, 1553, 1403, 1276, \
            1234, 1276, 1403, 1608, 1885, 2222, 2605, 3022, \
            3456, 3889, 4305, 4688, 5022, 5297, 5500, 5624, \
            5664, 5618, 5489, 5282, 5004, 4665, 4280, 3862, \
            3456, 3023, 2607, 2224, 1890, 1615, 1412, 1288, \
            1248, 1294, 1423, 1630, 1908, 2247, 2632, 3050 )
	src = blocks.vector_source_b (src_data)
	pulse_shaper = pulse_shaper_bs (1234, 5678, 1, 32) # (v_min, v_max, sign[+/-1], interpolation)
	dst = blocks.vector_sink_s ()
	self.tb.connect (src, pulse_shaper)
	self.tb.connect (pulse_shaper, dst)

        self.tb.run ()
        # check data
	result_data = dst.data ()
	self.assertEqual (expected_result, result_data)


if __name__ == '__main__':
    gr_unittest.run(qa_pulse_shaper_bs, "qa_pulse_shaper_bs.xml")
