# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('pdf_compressor')

from pdf_compressor_lib import Window
from pdf_compressor.AboutPdfCompressorDialog import AboutPdfCompressorDialog
from pdf_compressor.PreferencesPdfCompressorDialog import PreferencesPdfCompressorDialog

# See pdf_compressor_lib.Window.py for more details about how this class works
class PdfCompressorWindow(Window):
    __gtype_name__ = "PdfCompressorWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(PdfCompressorWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutPdfCompressorDialog
        self.PreferencesDialog = PreferencesPdfCompressorDialog

        # Code for other initialization actions should be added here.

        self.compressioncommand = "gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile="

        self.button1 = self.builder.get_object("button1")
        self.filechooserbutton1 = self.builder.get_object("filechooserbutton1")

    def on_button1_clicked(self, widget):
        bashcommand = (self.compressioncommand + 
                           self.filechooserbutton1.get_filename()[:-4] + 
                           "_compressed.pdf " + self.filechooserbutton1.get_filename())
        print bashcommand
        import os
        os.system(bashcommand)


