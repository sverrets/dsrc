#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: DSRC RSU Receiver
# Generated: Tue Jan 17 09:48:02 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import digital;import cmath
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import dsrcmod
import sip
import sys
import time


class rsu_receiver(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "DSRC RSU Receiver")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("DSRC RSU Receiver")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "rsu_receiver")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.symbol_per_second = symbol_per_second = 250e3
        self.samp_per_symb = samp_per_symb = 20
        self.usrp_samples_per_second = usrp_samples_per_second = 100e6
        self.input_rate = input_rate = int(samp_per_symb * symbol_per_second)
        self.subcarrier_freq = subcarrier_freq = 1.5e6
        
        self.lowpass_coeff = lowpass_coeff = firdes.low_pass(1.0, input_rate, 100e3, 100e3, firdes.WIN_HAMMING, 6.76)
          
        self.gain = gain = 1.0
        self.decimation_rate = decimation_rate = int(usrp_samples_per_second / input_rate)

        ##################################################
        # Blocks
        ##################################################
        self._subcarrier_freq_tool_bar = Qt.QToolBar(self)
        self._subcarrier_freq_tool_bar.addWidget(Qt.QLabel('Subcarrier frequency'+": "))
        self._subcarrier_freq_line_edit = Qt.QLineEdit(str(self.subcarrier_freq))
        self._subcarrier_freq_tool_bar.addWidget(self._subcarrier_freq_line_edit)
        self._subcarrier_freq_line_edit.returnPressed.connect(
        	lambda: self.set_subcarrier_freq(eng_notation.str_to_num(str(self._subcarrier_freq_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._subcarrier_freq_tool_bar)
        self.usrp_source = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.usrp_source.set_samp_rate(input_rate)
        self.usrp_source.set_center_freq(5.8e9, 0)
        self.usrp_source.set_gain(gain, 0)
        self.usrp_source.set_antenna('RX2', 0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	256, #size
        	input_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.file_sink = blocks.file_sink(gr.sizeof_char*gr.sizeof_char, 'binary_nrz_data', False)
        self.file_sink.set_unbuffered(False)
        self.dsrcmod_nrzi_to_nrz_bb_0 = dsrcmod.nrzi_to_nrz_bb(1)
        self.digital_mpsk_receiver_cc_0 = digital.mpsk_receiver_cc(2, 0, cmath.pi/100.0, -0.00393, 0.00393, 0.5, 0.05, samp_per_symb, (samp_per_symb * samp_per_symb) / 4, 0.005)
        self.complex_to_real = blocks.complex_to_real(1)
        self.channel_filter = filter.freq_xlating_fir_filter_ccf(1, (lowpass_coeff), 5.8e9 + subcarrier_freq, input_rate)
        self.binary_slicer = digital.binary_slicer_fb()

        ##################################################
        # Connections
        ##################################################
        self.connect((self.binary_slicer, 0), (self.dsrcmod_nrzi_to_nrz_bb_0, 0))    
        self.connect((self.channel_filter, 0), (self.digital_mpsk_receiver_cc_0, 0))    
        self.connect((self.complex_to_real, 0), (self.binary_slicer, 0))    
        self.connect((self.digital_mpsk_receiver_cc_0, 0), (self.complex_to_real, 0))    
        self.connect((self.dsrcmod_nrzi_to_nrz_bb_0, 0), (self.file_sink, 0))    
        self.connect((self.usrp_source, 0), (self.channel_filter, 0))    
        self.connect((self.usrp_source, 0), (self.qtgui_time_sink_x_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rsu_receiver")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_symbol_per_second(self):
        return self.symbol_per_second

    def set_symbol_per_second(self, symbol_per_second):
        self.symbol_per_second = symbol_per_second
        self.set_input_rate(int(self.samp_per_symb * self.symbol_per_second))

    def get_samp_per_symb(self):
        return self.samp_per_symb

    def set_samp_per_symb(self, samp_per_symb):
        self.samp_per_symb = samp_per_symb
        self.set_input_rate(int(self.samp_per_symb * self.symbol_per_second))
        self.digital_mpsk_receiver_cc_0.set_omega(self.samp_per_symb)
        self.digital_mpsk_receiver_cc_0.set_gain_omega((self.samp_per_symb * self.samp_per_symb) / 4)

    def get_usrp_samples_per_second(self):
        return self.usrp_samples_per_second

    def set_usrp_samples_per_second(self, usrp_samples_per_second):
        self.usrp_samples_per_second = usrp_samples_per_second
        self.set_decimation_rate(int(self.usrp_samples_per_second / self.input_rate))

    def get_input_rate(self):
        return self.input_rate

    def set_input_rate(self, input_rate):
        self.input_rate = input_rate
        self.usrp_source.set_samp_rate(self.input_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.input_rate)
        self.set_decimation_rate(int(self.usrp_samples_per_second / self.input_rate))

    def get_subcarrier_freq(self):
        return self.subcarrier_freq

    def set_subcarrier_freq(self, subcarrier_freq):
        self.subcarrier_freq = subcarrier_freq
        Qt.QMetaObject.invokeMethod(self._subcarrier_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.subcarrier_freq)))
        self.channel_filter.set_center_freq(5.8e9 + self.subcarrier_freq)

    def get_lowpass_coeff(self):
        return self.lowpass_coeff

    def set_lowpass_coeff(self, lowpass_coeff):
        self.lowpass_coeff = lowpass_coeff
        self.channel_filter.set_taps((self.lowpass_coeff))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.usrp_source.set_gain(self.gain, 0)
        	

    def get_decimation_rate(self):
        return self.decimation_rate

    def set_decimation_rate(self, decimation_rate):
        self.decimation_rate = decimation_rate


def main(top_block_cls=rsu_receiver, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
