from setuptools import setup, find_packages

setup(
    name='OsuFileParser',
    version='1.0',
    description='Package for wrapping ".osu" file data into a python class.',
    author='ZyMa-1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
