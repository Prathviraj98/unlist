from setuptools import setup, find_packages

setup(
    name='unlist_nested',
    version='0.1.0',
    description='A simple Python package to unlist (flatten) lists of any nesting level.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Darling',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
