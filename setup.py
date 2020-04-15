
from setuptools import setup, find_packages
from IotaCli.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='IotaCli',
    version=VERSION,
    description='CLI messaging application on the IOTA tangle',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Alan Vega',
    author_email='alanvega002@gmail.com',
    url='https://github.com/AlanVegaDecentralize/IotaCli.git',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'IotaCli': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        IotaCli = IotaCli.main:main
    """,
)
