from setuptools import setup, find_packages

version = open('pyswagger/__init__.py', 'r').readline().split()[2].strip("'")

setup(
    name = 'pyswagger',
    packages = find_packages(exclude=['*.tests.*']),
    version = version,
    description = 'A type-safe, dynamic, spec-compliant swagger client & converter for python',
    author = 'Mission Liao',
    author_email = 'missionaryliao@gmail.com',
    url = 'https://github.com/mission-liao/pyswagger', # use the URL to the github repo
    download_url = 'https://github.com/mission-liao/pyswagger/tarball/{0}'.format(version),
    keywords = ['swagger', 'REST'], # arbitrary keywords
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.1',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = ['six >= 1.7.2', 'pyaml>=15.03.1', 'validate_email']
)

