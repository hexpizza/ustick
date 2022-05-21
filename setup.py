from setuptools import setup

with open("README.md") as file:
    read_me_description = file.read()

setup(
    name='ustick',
    version='0.1',
    packages=['ustick'],
    url='https://github.com/hexpizza/ustick',
    license='',
    author='hexpizza',
    author_email='skoryagin96@gmail.com',
    description='Tool for creating notes and stickers',
    long_description = read_me_description,
    long_description_content_type = "text/markdown",
    install_requires=['colorama', 'docopt', 'PyYAML', 'termcolor', 'textwrap3'],
    entry_points={
        'console_scripts':
            ['ustick = ustick.ustick']
    }
)
