#!/usr/bin/env python

from setuptools import setup, find_packages

epdict=dict();
epdict['nova.hooks']=dict();
epdict['nova.hooks']['run_instance=pinhead.hooks:PinHeadRunHook']=None
epdict['nova.hooks']['terminate_instance=pinhead.hooks:PinHeadRunHook']=None

setup(name='pinhead',
	version='0.1.2',
	description='A tool for auto-pinning kvm vcpus to physical threads on the local machine (+ Nova hooks)',
	author='Giorgio Franceschi',
	author_email='g.franceschi@tmg.nl',
	packages=find_packages(),
	entry_points=epdict
)
