# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TrackedDownloadState(str, Enum):
    """
    TrackedDownloadState
    """

    """
    allowed enum values
    """
    DOWNLOADING = 'downloading'
    IMPORTPENDING = 'importPending'
    IMPORTING = 'importing'
    IMPORTED = 'imported'
    FAILEDPENDING = 'failedPending'
    FAILED = 'failed'
    IGNORED = 'ignored'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TrackedDownloadState from a JSON string"""
        return cls(json.loads(json_str))


