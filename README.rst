===
gig
===

.. image:: https://badge.fury.io/py/gig.png
    :target: http://badge.fury.io/py/gig

.. image:: https://travis-ci.org/sloria/gig.png?branch=master
        :target: https://travis-ci.org/sloria/gig


A CLI utility to create .gitignore files, to keep your source control so fresh and so clean clean.

.. image:: https://dl.dropboxusercontent.com/u/1693233/github/andre3000_crop.jpg
    :alt: Andre

Install
-------
::

    $ pip install gig

Usage
-----

In the shell. . .

::

    $ gig Python Ruby


Or, programmatically, in Python. . .

.. code-block:: python

    >>> import gig
    >>> gig.generate_gitignore(["Clojure"])
    u'\n### Clojure ###\nLeiningen.gitignore'

For more help, run ``gig --help``.


Requirements
------------

- Python >= 2.7 or >= 3.3
- Internet connection

License
-------

`MIT Licensed <http://sloria.mit-license.org/>`_.