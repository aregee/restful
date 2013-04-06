#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fiddle.settings")

    from django.core.management import execute_from_command_line
    print "REST APIs with django-restframework"
    execute_from_command_line(sys.argv)
