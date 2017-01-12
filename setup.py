from distutils.core import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


PACKAGE = "redistools"
NAME = "redistools"
DESCRIPTION = "A Redis tools provide python's Lock RLock Semaphore BoundedSemaphore Condition Event Barrier and Queue cross process."
AUTHOR = "wwqgtxx"
AUTHOR_EMAIL = "wwqgtxx@gmail.com"
URL = "https://github.com/wwqgtxx/RedisTools"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="GNU General Public License v3 (GPLv3)",
    url=URL,
    packages=["redistools"],
    platforms='any',
    install_requires=[
        'future>=0.16.0',
        'redis>=2.10.5',
        'six>=1.10.0',
        'monotonic>=1.2',
        'redis-collections>=0.4.2'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
    ],
    zip_safe=False,
)
