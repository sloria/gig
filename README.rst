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

Install/Upgrade
---------------
::

    $ pip install -U gig

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

You can also generate global ``.gitignore_global`` files. For more info, see `here <http://augustl.com/blog/2009/global_gitignores/>`_.

::

    $ gig OSX SublimeText Linux --global


To get a list of available templates. . .

::

    $ gig list
    $ gig list --global

For more help, run ``gig --help``.


Requirements
------------

- Python >= 2.7 or >= 3.3
- Internet connection

License
-------

`MIT Licensed <http://sloria.mit-license.org/>`_.

Changelog
---------

0.2.0 (09/09/2013)
++++++++++++++++++
- Add support for global gitignore files.

0.1.0 (09/07/2013)
++++++++++++++++++
- First release