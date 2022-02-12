#!/usr/bin/env python3
from phue import Bridge
BRIDGE = Bridge()
BRIDGE.connect()
GROUP_ID = 1

BRIDGE.set_group(GROUP_ID, 'bri_inc', 40)