"""\
Grip
----

Render local readme files before sending off to GitHub.


Grip is easy to set up
``````````````````````

::

    $ pip install grip
    $ cd myproject
    $ grip


Links
`````

* `Website <http://github.com/joeyespo/grip>`_

"""

import os
from setuptools import setup, find_packages


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name='grip',
    version='3.3.0',
    description='Render local readme files before sending off to GitHub.',
    long_description=__doc__,
    author='Joe Esposito',
    author_email='joe@joeyespo.com',
    url='http://github.com/joeyespo/grip',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    package_data={'grip': ['static/*', 'templates/*']},
    install_requires=read('requirements.txt').splitlines(),
    zip_safe=False,
    entry_points={'console_scripts': ['grip = grip.command:main']},
)
