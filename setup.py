from setuptools import setup, find_packages

setup(
    name='stython',
    version='1.3',
    license='MIT',
    author='Arun Kapila',
    author_email='starshootercity@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'stython'},
    url='https://github.com/cometcake575/stython',
    install_requires=[],

    py_modules=['stython'],
)
