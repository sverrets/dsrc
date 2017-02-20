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
from nrz_to_nrzi_bb import nrz_to_nrzi_bb

class qa_nrz_to_nrzi_bb (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        # set up fg
	src_data = (1,1,0,0,1,0)
	expected_result = (1,1,0,1,1,0)
	src = blocks.vector_source_b (src_data)
	nrz_to_nrzi = nrz_to_nrzi_bb (1) # Test with initial state 1
	sink = blocks.vector_sink_b ()
	self.tb.connect (src, nrz_to_nrzi)
	self.tb.connect (nrz_to_nrzi, sink)
        self.tb.run ()
        # check data
	result_data = sink.data ()
	self.assertEqual(expected_result, result_data)

    def test_002_t (self):
        # set up fg
	src_data = (0,1,0,0,1,0)
	expected_result = (1,1,0,1,1,0)
	src = blocks.vector_source_b (src_data)
	nrz_to_nrzi = nrz_to_nrzi_bb (0) # Test with initial state 0
	sink = blocks.vector_sink_b ()
	self.tb.connect (src, nrz_to_nrzi)
	self.tb.connect (nrz_to_nrzi, sink)
        self.tb.run ()
        # check data
	result_data = sink.data ()
	self.assertEqual(expected_result, result_data)


if __name__ == '__main__':
    gr_unittest.run(qa_nrz_to_nrzi_bb, "qa_nrz_to_nrzi_bb.xml")
