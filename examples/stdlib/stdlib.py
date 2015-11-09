#!/usr/bin/env python

from kidraw import *

with library('stdlib') as l:
    l.std.resistor()
    l.std.capacitor()
    l.std.capacitor.polarized()
    l.std.inductor()
    l.std.diode()
    l.std.diode.zener()
    l.std.diode.schottky()
    l.std.led()
    l.std.power.vcc()
    l.std.power.vcc('+12V')
    l.std.power.gnd()
    l.std.power.gnd('AGND')
    l.std.power.flag()
    l.std.transistor.bipolar.npn(base_pin=2, collector_pin=1, emitter_pin=3)
    l.std.transistor.bipolar.pnp(base_pin=2, collector_pin=1, emitter_pin=3)
    l.std.transistor.jfet.n_channel(gate_pin=2, drain_pin=1, source_pin=3)
    l.std.transistor.jfet.p_channel(gate_pin=2, drain_pin=1, source_pin=3)
    l.std.transistor.mosfet.n_channel(gate_pin=2, drain_pin=1, source_pin=3)
    l.std.transistor.mosfet.p_channel(gate_pin=2, drain_pin=1, source_pin=3)
