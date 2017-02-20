#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/build/swig:$PYTHONPATH
/usr/bin/python2 /home/jonathan/Masteroppgave/GNURadioprojects/gr-dsrcmod/python/qa_pulse_shaper_bs.py 
