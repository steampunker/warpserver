import re
import os
from setuptools import find_packages, setup


PKG = 'warpserver'
VERSIONFILE = os.path.join(PKG, "version.py")
long_description = """Warpserver is a replacement for the Creatures Docking Station warp server.
"""
install_requires = ['pymongo', 'scoundrels', 'beautifulsoup4']

verstr = "unknown"
try:
	verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
	pass # Okay, there is no version file.
else:
	VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
	mo = re.search(VSRE, verstrline, re.M)
	if mo:
		__version__ = mo.group(1)
	else:
		msg = "if %s.py exists, it is required to be well-formed" % VERSIONFILE
		raise RuntimeError(msg)

setup(
	name=PKG,
	version=__version__,
	install_requires=install_requires,
	entry_points={
		'console_scripts': [],
	},
	packages=find_packages(),
	package_dir={'warpserver':'warpserver'},
	package_data={},
	author='Sina Mashek',
	author_email='mashek@thescoundrels.net',
	maintainer='Sina Mashek',
	maintainer_email='mashek@thescoundrels.net',
	long_description=long_description,
	description='Warpserver is a Creatures Docking Station server.',
	license='LICENSE',
	url='http://scoundrels.github.io/scrib',
	platforms=['any'],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Environment :: Web Environment',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
	],
)
