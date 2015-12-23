#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk

from objects.frame import geometry


class Gui:
    def __init__(self):
        interface = Gtk.Builder()
        interface.add_from_file('gui/interface.glade')
        interface.connect_signals(self)
        self.a_value = interface.get_object("a_value")
        self.b_value = interface.get_object("b_value")
        self.c_value = interface.get_object("c_value")
        self.section = interface.get_object("section_type")
        self.A_value = interface.get_object("A_value")
        self.status = interface.get_object("status")
        self.I_x_value = interface.get_object("I_x_value")
        
    def gtk_main_quit(self):
        Gtk.main_quit()
    
    def on_compute_clicked(self, widget):
        a = float(self.a_value.get_text())
        b = float(self.b_value.get_text())
        if self.c_value.get_text():
            c = float(self.c_value.get_text())
            
        section = self.section.get_active_text()
        values = geometry(section, a, b)
        
        self.A_value.set_text(str(format(values.A, '6.3E')))
        self.I_x_value.set_text(str(format(values.I_x, '6.3E')))
        
    def on_a_value_changed(self, widget):
        value = widget.get_text()
        self.status.set_text("")
        try:
            float(value)
        except:
            self.status.set_text("Incorrect value, please set a number in float or engineering format e.g. 1200 or 1.2E3")
        
        
if __name__ == "__main__":
    Gui()
    Gtk.main()
    
    
