from setuptools import setup
from setuptools import find_packages

setup(
    name='ustick',
    version='0.0.1',
    url='https://github.com/hexpizza/ustick',
    author='Sergey Koryagin',
    author_email='skoryagin96@gmail.com',
    description='Tool for creating console stickers',
    install_requires=['colorama', 'docopt', 'PyYAML', 'termcolor', 'textwrap3'],
    packages=find_packages(),
    entry_points={
        'console_scripts':
            [
                'ustick = ustick.ustick:main'
            ]
    }
)
