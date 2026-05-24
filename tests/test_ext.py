# SPDX-FileCopyrightText: 2014, 2015 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""Flask-IIIF extension test."""

from __future__ import absolute_import

from unittest import TestCase

from flask import Flask

from flask_iiif import IIIF
from flask_iiif import config as default_config


class TestIIIF(TestCase):
    """Test extension creation."""

    def setUp(self):
        """Setup up."""
        app = Flask(__name__)
        app.config["DEBUG"] = True
        app.config["TESTING"] = True
        app.logger.disabled = True
        self.app = app

    def test_version(self):
        """Assert that version number can be parsed."""
        from distutils.version import LooseVersion

        from flask_iiif import __version__

        LooseVersion(__version__)

    def test_creation(self):
        """Test extension creation."""
        assert "iiif" not in self.app.extensions
        IIIF(app=self.app)
        assert isinstance(self.app.extensions["iiif"], IIIF)

    def test_creation_old_flask(self):
        """Simulate old Flask (pre 0.9)."""
        del self.app.extensions
        IIIF(app=self.app)
        assert isinstance(self.app.extensions["iiif"], IIIF)

    def test_creation_init(self):
        """Test extension creation init."""
        assert "iiif" not in self.app.extensions
        r = IIIF()
        r.init_app(app=self.app)
        assert isinstance(self.app.extensions["iiif"], IIIF)

    def test_double_creation(self):
        """Test extension double creation."""
        IIIF(app=self.app)
        self.assertRaises(RuntimeError, IIIF, app=self.app)

    def test_default_config(self):
        """Test extension default configuration."""
        IIIF(app=self.app)
        for k in dir(default_config):
            if k.startswith("IIIF_"):
                assert self.app.config.get(k) == getattr(default_config, k)
