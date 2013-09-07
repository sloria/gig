import sys
import subprocess

from setuptools import setup

PUBLISH_CMD = "python setup.py register sdist upload"
TEST_PUBLISH_CMD = 'python setup.py register -r test sdist upload -r test'

if 'publish' in sys.argv:
    status = subprocess.call(PUBLISH_CMD, shell=True)
    sys.exit(status)

if 'publish_test' in sys.argv:
    status = subprocess.call(TEST_PUBLISH_CMD, shell=True)
    sys.exit()

def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='gig',
    version="0.1.0",
    description='Generate .gitignore templates from the command line',
    long_description=read("README.rst"),
    author='Steven Loria',
    author_email='sloria1@gmail.com',
    url='https://github.com/sloria/gig',
    install_requires=['requests'],
    license=read("LICENSE"),
    py_modules=["gig", 'docopt'],
    entry_points={
        'console_scripts': [
            "gig = gig:main"
        ]
    },
    tests_require=['nose'],
    test_suite='tests',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    keywords=['git', 'gitignore', 'command-line']
)