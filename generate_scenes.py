#!/usr/bin/env python3
from phue import Bridge
import os
import argparse

def main():
    """
    Generates scripts activating every scene file on the Bridge in scenes/ subdirectory.
    """
    BRIDGE = Bridge()
    BRIDGE.connect()
    TARGET_DIR = "scenes"
    # Generate files for all scenes.
    print("Scenes:")
    scene_names = [s.name for s in BRIDGE.scenes if not s.recycle]
    print(scene_names)
    target_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), TARGET_DIR)
    for scene in scene_names:
        link_name = target_dir + '/' + scene + '.py'
        print("Writing to ", link_name)
        # check for path traversal in a scene name.
        if os.path.commonprefix((os.path.realpath(link_name),target_dir)) == target_dir: 
            os.symlink('../set_scene.py', link_name)

if __name__ == '__main__':
    main()