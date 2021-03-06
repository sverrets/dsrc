#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: DSRC Transceiver
# Generated: Mon Feb 20 12:59:28 2017
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
from gnuradio import eng_notation
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
from gnuradio import qtgui


class dsrc_transceiver(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "DSRC Transceiver")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("DSRC Transceiver")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "dsrc_transceiver")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.symbol_per_second = symbol_per_second = 250e3
        self.samp_per_symb = samp_per_symb = 20
        self.pulse_shaper_interpolation = pulse_shaper_interpolation = 32
        self.input_rate = input_rate = int(samp_per_symb * symbol_per_second)
        self.bit_per_second = bit_per_second = 500e3
        self.v_min = v_min = 1000
        self.v_max = v_max = 25000
        self.usrp_samples_per_second_0 = usrp_samples_per_second_0 = 100e6
        self.usrp_samples_per_second = usrp_samples_per_second = 400e6
        self.subcarrier_freq = subcarrier_freq = 1.5e6
        self.sample_rate_0 = sample_rate_0 = 16e6
        self.sample_rate = sample_rate = pulse_shaper_interpolation * bit_per_second
        self.phase = phase = 1

        self.lowpass_coeff = lowpass_coeff = firdes.low_pass(1.0, input_rate, 100e3, 100e3, firdes.WIN_HAMMING, 6.76)

        self.input_file = input_file = 'bst1.dat'
        self.gain = gain = 20.0
        self.frequency = frequency = 5.8025e9

        ##################################################
        # Blocks
        ##################################################
        self.usrp_source = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.usrp_source.set_samp_rate(input_rate)
        self.usrp_source.set_center_freq(5.8025e9, 0)
        self.usrp_source.set_gain(gain, 0)
        self.usrp_source.set_antenna('RX2', 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(sample_rate_0)
        self.uhd_usrp_sink_0.set_center_freq(frequency, 0)
        self.uhd_usrp_sink_0.set_gain(gain, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self._subcarrier_freq_tool_bar = Qt.QToolBar(self)
        self._subcarrier_freq_tool_bar.addWidget(Qt.QLabel('Subcarrier frequency'+": "))
        self._subcarrier_freq_line_edit = Qt.QLineEdit(str(self.subcarrier_freq))
        self._subcarrier_freq_tool_bar.addWidget(self._subcarrier_freq_line_edit)
        self._subcarrier_freq_line_edit.returnPressed.connect(
        	lambda: self.set_subcarrier_freq(eng_notation.str_to_num(str(self._subcarrier_freq_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._subcarrier_freq_tool_bar)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_c(
        	512, #size
        	sample_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(0, 26000)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

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

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
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

        for i in xrange(2):
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
        self._input_file_tool_bar = Qt.QToolBar(self)
        self._input_file_tool_bar.addWidget(Qt.QLabel('Input file'+": "))
        self._input_file_line_edit = Qt.QLineEdit(str(self.input_file))
        self._input_file_tool_bar.addWidget(self._input_file_line_edit)
        self._input_file_line_edit.returnPressed.connect(
        	lambda: self.set_input_file(str(str(self._input_file_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._input_file_tool_bar)
        self.dsrcmod_pulse_shaper_bs_0 = dsrcmod.pulse_shaper_bs(v_min, v_max, phase, pulse_shaper_interpolation)
        self.blocks_vector_source_b_0 = blocks.vector_source_b((1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0), True, 1, [])
        self.blocks_interleaved_short_to_complex_0 = blocks.interleaved_short_to_complex(False, False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_interleaved_short_to_complex_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_vector_source_b_0, 0), (self.dsrcmod_pulse_shaper_bs_0, 0))
        self.connect((self.dsrcmod_pulse_shaper_bs_0, 0), (self.blocks_interleaved_short_to_complex_0, 0))
        self.connect((self.usrp_source, 0), (self.qtgui_time_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dsrc_transceiver")
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

    def get_pulse_shaper_interpolation(self):
        return self.pulse_shaper_interpolation

    def set_pulse_shaper_interpolation(self, pulse_shaper_interpolation):
        self.pulse_shaper_interpolation = pulse_shaper_interpolation
        self.set_sample_rate(self.pulse_shaper_interpolation * self.bit_per_second)

    def get_input_rate(self):
        return self.input_rate

    def set_input_rate(self, input_rate):
        self.input_rate = input_rate
        self.usrp_source.set_samp_rate(self.input_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.input_rate)

    def get_bit_per_second(self):
        return self.bit_per_second

    def set_bit_per_second(self, bit_per_second):
        self.bit_per_second = bit_per_second
        self.set_sample_rate(self.pulse_shaper_interpolation * self.bit_per_second)

    def get_v_min(self):
        return self.v_min

    def set_v_min(self, v_min):
        self.v_min = v_min

    def get_v_max(self):
        return self.v_max

    def set_v_max(self, v_max):
        self.v_max = v_max

    def get_usrp_samples_per_second_0(self):
        return self.usrp_samples_per_second_0

    def set_usrp_samples_per_second_0(self, usrp_samples_per_second_0):
        self.usrp_samples_per_second_0 = usrp_samples_per_second_0

    def get_usrp_samples_per_second(self):
        return self.usrp_samples_per_second

    def set_usrp_samples_per_second(self, usrp_samples_per_second):
        self.usrp_samples_per_second = usrp_samples_per_second

    def get_subcarrier_freq(self):
        return self.subcarrier_freq

    def set_subcarrier_freq(self, subcarrier_freq):
        self.subcarrier_freq = subcarrier_freq
        Qt.QMetaObject.invokeMethod(self._subcarrier_freq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.subcarrier_freq)))

    def get_sample_rate_0(self):
        return self.sample_rate_0

    def set_sample_rate_0(self, sample_rate_0):
        self.sample_rate_0 = sample_rate_0
        self.uhd_usrp_sink_0.set_samp_rate(self.sample_rate_0)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.sample_rate)

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase

    def get_lowpass_coeff(self):
        return self.lowpass_coeff

    def set_lowpass_coeff(self, lowpass_coeff):
        self.lowpass_coeff = lowpass_coeff

    def get_input_file(self):
        return self.input_file

    def set_input_file(self, input_file):
        self.input_file = input_file
        Qt.QMetaObject.invokeMethod(self._input_file_line_edit, "setText", Qt.Q_ARG("QString", str(self.input_file)))

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.usrp_source.set_gain(self.gain, 0)

        self.uhd_usrp_sink_0.set_gain(self.gain, 0)


    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.uhd_usrp_sink_0.set_center_freq(self.frequency, 0)


def main(top_block_cls=dsrc_transceiver, options=None):

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
