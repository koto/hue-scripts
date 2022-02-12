#!/usr/bin/env python3
from phue import Bridge
import os
import sys

BRIDGE = Bridge()
BRIDGE.connect()

GROUP_ID = 1

# The script name is the name of the scene.
scene = os.path.splitext(os.path.basename(__file__))[0]
if scene == 'set_scene':
    scene = sys.argv[1] if len(sys.argv) > 1 else ""

scenes = [x for x in BRIDGE.scenes if x.name == scene]
if len(scenes) == 1:
    BRIDGE.activate_scene(GROUP_ID, scenes[0].scene_id)
else:
    print("Could not find scene:", repr(scene))
