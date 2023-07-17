from setuptools import setup

setup(
    name='OsuFileParser',
    version='1.0.1',
    description='Package for wrapping ".osu" file data into a python class.',
    author='ZyMa-1',
    url='https://github.com/ZyMa-1/OsuFileParser',
    license='MIT',
    python_requires=">=3.10",
    package_dir={'OsuFileParser': 'src'},
    packages=['OsuFileParser', 'src/my_dataclasses'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        # Specify any required dependencies here
    ],
)
