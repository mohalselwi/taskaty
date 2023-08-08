from setuptools import setup

setup(
    name='taskaty',
    version='0.1.0',
    description='A simple command-line Task-app written in Python',
    author='Mohammed alsewi',
    install_requires=['tabulate'],
    entry_points={
        'console_script':[
            'taskaty=taskaty:main',
        ],
    },
)