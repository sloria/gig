# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import unittest
import logging
from nose.tools import *  # PEP8 asserts
from subprocess import check_output, CalledProcessError

import gig

HERE = os.path.abspath(os.path.dirname(__file__))

class TestGig(unittest.TestCase):

    '''Unit tests for gig.'''

    def setUp(self):
        os.chdir(HERE)

    def tearDown(self):
        os.chdir(HERE)
        if os.path.isfile('.gitignore'):
            os.remove('.gitignore')

    def test_single_language(self):
        run_cmd("gig Python")
        assert_true(os.path.isfile('.gitignore'))
        with open('.gitignore', 'r') as fp:
            contents = fp.read()
            assert_in('*.py[cod]', contents)
            assert_in('### Python ###', contents)

    def test_multiple_languages(self):
        run_cmd('gig Python Ruby')
        assert_true(os.path.isfile('.gitignore'))
        with open('.gitignore', 'r') as fp:
            gitignore = fp.read()
            assert_in("*.py[cod]", gitignore)
            assert_in("*.gem", gitignore)
            assert_in("### Python ###", gitignore)
            assert_in("### Ruby ###", gitignore)

    def test_cant_overwrite_by_default(self):
        run_cmd("gig Python")
        # Now a .gitignore exists, shouldn't be able to overwrite
        with assert_raises(CalledProcessError):
            run_cmd('gig Ruby')

    def test_force(self):
        run_cmd('gig Python')
        run_cmd('gig Ruby -f')
        with open('.gitignore', 'r') as fp:
            gitignore = fp.read()
            assert_in('### Ruby ###', gitignore)
            assert_in("*.gem", gitignore)
            assert_not_in("### Python ###", gitignore)

    def test_append(self):
        run_cmd('gig Python')
        run_cmd('gig Ruby -a')
        run_cmd('gig Clojure --append')
        with open('.gitignore', 'r') as fp:
            gitignore = fp.read()
            assert_in("### Ruby ###", gitignore)
            assert_in("*.py[cod]", gitignore)
            assert_in("### Python ###", gitignore)
            assert_in("*.gem", gitignore)
            assert_in("### Clojure ###", gitignore)
            assert_in("Leiningen.gitignore", gitignore)

    def test_generate_gitignore(self):
        gitignore = gig.generate_gitignore(['Python', 'Ruby'])
        assert_in("*.py[cod]", gitignore)
        assert_in("*.gem", gitignore)
        assert_in("### Python ###", gitignore)
        assert_in("### Ruby ###", gitignore)

    def test_generate_global_gitignore(self):
        gitignore = gig.generate_gitignore(["Windows", "OSX"], global_=True)
        assert_in("Thumbs.db", gitignore)
        assert_in(".DS_Store", gitignore)


def run_cmd(cmd):
    '''Run a shell command `cmd` and return its output.'''
    return check_output(cmd, shell=True).decode('utf-8')


if __name__ == '__main__':
    unittest.main()