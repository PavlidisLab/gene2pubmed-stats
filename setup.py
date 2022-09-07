from setuptools import setup

setup(
        name='gene2pubmed-stats',
        version='1.0.0',
        install_requires=['pandas'],
        entry_points={'console_scripts': ['gene2pubmed-stats=main:main']})
