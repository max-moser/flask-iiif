# SPDX-FileCopyrightText: 2015, 2016, 2017 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""Signals triggered on Flask-IIIF API request.

.. note::

    The signals are triggered before process, after the validation and after
    the process of the request.

.. code-block:: python

    from flask import current_app

    from flask_iiif.signals import (
        iiif_after_process_request, iiif_before_process_request
    )

    def on_before_process_request(
            current_object_state, version='', uuid='', region='', size='',
            rotate='', quality='', image_format=''):
        # Do something before process the request

    iiif_before_process_request.connect_via(on_before_process_request)

    def on_after_process_request(
            current_object_state, mimetype='', image=''):
        # Do something after proccess the request

    iiif_after_process_request.connect(on_after_process_request)

"""

from blinker import Namespace

_signals = Namespace()

# Before request
iiif_before_process_request = _signals.signal("iiif-before-process-request")
# After request
iiif_after_process_request = _signals.signal("iiif-after-process-request")
# Before info.json request
iiif_before_info_request = _signals.signal("iiif-before-info-request")
# After info.json request
iiif_after_info_request = _signals.signal("iiif-after-info-request")
