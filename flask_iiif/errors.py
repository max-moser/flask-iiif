# SPDX-FileCopyrightText: 2014, 2015 CERN.
# SPDX-License-Identifier: BSD-3-Clause

"""Multimedia error."""


class MultimediaError(Exception):
    """General multimedia exception."""

    def __init__(self, message=None, code=None):
        """Init the error handler."""
        super(MultimediaError, self).__init__()
        self.message = message or self.__class__.__name__
        self.code = code or 500

    def __str__(self):
        """Error message."""
        return repr(
            "Error message: {message}. Error code: {code}".format(
                message=self.message, code=self.code
            )
        )


class MultimediaImageNotFound(MultimediaError):
    """Image not found error."""

    def __init__(self, message=None):
        """Init with status code 404."""
        super(MultimediaImageNotFound, self).__init__(message, code=404)


class MultimediaImageCropError(MultimediaError):
    """Image on crop error."""


class MultimediaImageResizeError(MultimediaError):
    """Image resize error."""


class MultimediaImageRotateError(MultimediaError):
    """Image rotate error."""


class MultimediaImageQualityError(MultimediaError):
    """Image quality error."""


class MultimediaImageFormatError(MultimediaError):
    """Image format error."""


class IIIFValidatorError(MultimediaError):
    """IIIF API validator error."""
