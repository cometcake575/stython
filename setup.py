from setuptools import setup

from stython import __version__

setup(
    name='stython',
    version=__version__,

    url='https://github.com/cometcake575/stython',
    author='Arun Kapila',
    author_email='starshootercity@gmail.com',
    install_requires=[
        'os',
        'time',
        'sys',
        'random'
    ],

    py_modules=['stython'],
)
