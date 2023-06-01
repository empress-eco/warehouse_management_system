from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in wms_frappe/__init__.py
from wms_frappe import __version__ as version

setup(
	name="wms_frappe",
	version=version,
	description="Warehouse Management System",
	author="Agile Shift I/O",
	author_email="contacto@gruporeal.org",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
