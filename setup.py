from setuptools import setup

setup(
        name='gene2pubmed-stats',
        version='1.0.0',
        packages=['gene2pubmed_stats'],
        install_requires=['pandas'],
        entry_points={'console_scripts': ['gene2pubmed-stats=gene2pubmed_stats.main:main']})
