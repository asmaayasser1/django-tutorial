"""
Assignment: Module 4 Tutorial - Django Introduction
Student Name: Asmaa Ali
Course: SDVE220 - Full Stack Python Development
Date: April 14, 2025

Description:
This project follows the official Django tutorial to demonstrate 
basic setup and functionality of a Django web application, 
including models, views, templates, and admin configuration.

Repository: https://github.com/asmaayasser1/django-tutorial
"""


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
