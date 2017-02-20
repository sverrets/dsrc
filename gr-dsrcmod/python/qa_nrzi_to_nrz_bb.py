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
from nrzi_to_nrz_bb import nrzi_to_nrz_bb

class qa_nrzi_to_nrz_bb (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
	src_data = (1,1,0,1,1,0)
	expected_result = (1,1,0,0,1,0)
	src = blocks.vector_source_b (src_data)
	nrzi_to_nrz = nrzi_to_nrz_bb (1) # Test with initial state 1
	sink = blocks.vector_sink_b ()
	self.tb.connect (src, nrzi_to_nrz)
	self.tb.connect (nrzi_to_nrz, sink)
        self.tb.run ()
        # check data
	result_data = sink.data ()
	self.assertEqual(expected_result, result_data)

    def test_002_t (self):
        # set up fg
	src_data = (1,1,0,1,1,0)
	expected_result = (0,1,0,0,1,0)
	src = blocks.vector_source_b (src_data)
	nrzi_to_nrz = nrzi_to_nrz_bb (0) # Test with initial state 0
	sink = blocks.vector_sink_b ()
	self.tb.connect (src, nrzi_to_nrz)
	self.tb.connect (nrzi_to_nrz, sink)
        self.tb.run ()
        # check data
	result_data = sink.data ()
	self.assertEqual(expected_result, result_data)

if __name__ == '__main__':
    gr_unittest.run(qa_nrzi_to_nrz_bb, "qa_nrzi_to_nrz_bb.xml")
