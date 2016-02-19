from setuptools import setup, find_packages

VERSION = '0.0.1'


setup(
    name="mkdocs-boost",
    version=VERSION,
    url='https://github.com/pfultz2/mkdocs-boost',
    license='boost',
    description='Boost theme for mkdocs',
    author='Paul Fultz II',
    author_email='pfultz2@yahoo.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'boost = mkdocs_boost',
        ]
    },
    zip_safe=False
)
