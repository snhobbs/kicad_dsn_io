#!/usr/bin/env python

"""Tests for `kicad_dsn_io` package."""


import unittest
from click.testing import CliRunner

from kicad_dsn_io import kicad_dsn_io
from kicad_dsn_io import cli


class TestKicad_dsn_io(unittest.TestCase):
    """Tests for `kicad_dsn_io` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'kicad_dsn_io.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
