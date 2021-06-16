from setuptools import setup
import sys

if __name__ == "__main__":
    if sys.platform == 'OpenVMS':
        setup(version = u'6.2.4')   # we have to set version manually on OpenVMS
    else:
        setup()
