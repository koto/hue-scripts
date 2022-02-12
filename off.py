#!/usr/bin/env python3
from phue import Bridge
BRIDGE = Bridge()
BRIDGE.connect()
GROUP_ID = 1

# Turn group off
BRIDGE.set_group(GROUP_ID, 'on', False)