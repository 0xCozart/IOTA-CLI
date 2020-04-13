
from setuptools import setup, find_packages
from iota-cli.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='iota-cli',
    version=VERSION,
    description='CLI application to hold and transfer IOTA tokens.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Alan Vega',
    author_email='alanvega002@gmail.com',
    url='https://github.com/AlanVegaDecentralize/IOTA-CLI.git',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'iota-cli': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        iota-cli = iota-cli.main:main
    """,
)
