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
# DSRC-module made by: Einar Thorsrud, Jonathan Hansen
#

# 

import numpy
from gnuradio import gr

class nrz_to_nrzi_bb(gr.sync_block):
    """
    docstring for block nrz_to_nrzi_bb
    """
    def __init__(self, preload):
	self.preload = preload
        gr.sync_block.__init__(self,
            name="nrz_to_nrzi_bb",
            in_sig=[numpy.int8],
            out_sig=[numpy.int8])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
	nrzi_bit = 0
	nrz_bit = 0
	prev_nrzi_bit = self.preload

	for i in range(len(out)):
		nrz_bit = in0[i]

		#Convert NRZ to NRZI
		if(nrz_bit == 0):
			nrzi_bit = prev_nrzi_bit ^ 1
		else:
			nrzi_bit = prev_nrzi_bit
		out[i] = nrzi_bit
		prev_nrzi_bit = nrzi_bit

        return len(output_items[0])

