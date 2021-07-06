# setup.py
from setuptools import setup

setup(entry_points={"saleor.plugins": ["subbly = subbly.plugin:SubblyPlugin"]})
