"""Tests for `mu_diff` package."""

import pytest
from pkg_resources import parse_version

import mu_diff


def test_valid_version():
    """Check that the package defines a valid ``__version__``."""
    v_curr = parse_version(mu_diff.__version__)
    v_orig = parse_version("0.1.0-dev")
    assert v_curr >= v_orig
