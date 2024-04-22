#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup

version = "0.5.4"

setup(
    name="OPi.GPIO",
    version=version,
    author="Le Duc Lischetzke",
    description=("A drop-in replacement for RPi.GPIO for the Orange Pi Zero"),
    license="MIT",
    keywords="orange pi opi gpio",
    url="https://github.com/lischetzke/OPi.GPIO",
    download_url="https://github.com/lischetzke/OPi.GPIO/tarball/" + version,
    packages=["OPi", "orangepi"],
    zip_safe=False
)
