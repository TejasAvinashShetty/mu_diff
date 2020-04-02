"""Tests for `mu_diff` package."""

import pytest
from numpy.random import random_sample
# from numpy.testing import assert_allclose
from pkg_resources import parse_version

# from mu_diff import mu_diff_maker
import mu_diff


def test_valid_version():
    """Check that the package defines a valid ``__version__``."""
    v_curr = parse_version(mu_diff.__version__)
    v_orig = parse_version("0.1.0-dev")
    assert v_curr >= v_orig


def test_mu_diff():
    a = random_sample((10,))
    assert mu_diff.mu_diff.mu_diff_maker(a, a) == 0
