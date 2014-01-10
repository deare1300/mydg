#!/usr/bin/env python
import os
import sys
##this is for session handler
BASE_DIR = os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, BASE_DIR)
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mydg.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
