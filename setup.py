from setuptools import setup, find_packages

setup(
    name='CGSearchRace',
    version='0.2.0',
    license='LICENSE',
    packages=find_packages(include=['CGSearchRace']),
    description='Port Coding Games CGSearchRace to Python',
    long_description=open('Readme.md').read(),
)
