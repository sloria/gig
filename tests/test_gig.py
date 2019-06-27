import pytest
from scripttest import TestFileEnvironment as FileEnvironment


@pytest.fixture
def env():
    return FileEnvironment()


def test_no_arguments(env):
    res = env.run("gig", expect_error=True)
    assert res.returncode == 1
    assert "Usage:" in res.stderr


def test_single_language(env):
    res = env.run("gig", "Python")
    assert res.returncode == 0
    assert "### Python ###" in res.stdout


def test_multiple_languages(env):
    res = env.run("gig", "Python", "Ruby")
    assert "*.py[cod]" in res.stdout
    assert "*.gem" in res.stdout
    assert "### Python ###" in res.stdout
    assert "### Ruby ###" in res.stdout


def test_generate_global_gitignore(env):
    res = env.run("gig", "Windows", "macOS", "--global")
    assert "Thumbs.db" in res.stdout
    assert ".DS_Store" in res.stdout
    assert "### Windows ###" in res.stdout
    assert "### macOS ###" in res.stdout


def test_error(env):
    res = env.run("gig", "notfound", expect_error=True)
    assert res.returncode == 1
