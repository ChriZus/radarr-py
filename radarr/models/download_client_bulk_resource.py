# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.9.1.9070
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from radarr.models.apply_tags import ApplyTags
from typing import Optional, Set
from typing_extensions import Self

class DownloadClientBulkResource(BaseModel):
    """
    DownloadClientBulkResource
    """ # noqa: E501
    ids: Optional[List[StrictInt]] = None
    tags: Optional[List[StrictInt]] = None
    apply_tags: Optional[ApplyTags] = Field(default=None, alias="applyTags")
    enable: Optional[StrictBool] = None
    priority: Optional[StrictInt] = None
    remove_completed_downloads: Optional[StrictBool] = Field(default=None, alias="removeCompletedDownloads")
    remove_failed_downloads: Optional[StrictBool] = Field(default=None, alias="removeFailedDownloads")
    __properties: ClassVar[List[str]] = ["ids", "tags", "applyTags", "enable", "priority", "removeCompletedDownloads", "removeFailedDownloads"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DownloadClientBulkResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if ids (nullable) is None
        # and model_fields_set contains the field
        if self.ids is None and "ids" in self.model_fields_set:
            _dict['ids'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if enable (nullable) is None
        # and model_fields_set contains the field
        if self.enable is None and "enable" in self.model_fields_set:
            _dict['enable'] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict['priority'] = None

        # set to None if remove_completed_downloads (nullable) is None
        # and model_fields_set contains the field
        if self.remove_completed_downloads is None and "remove_completed_downloads" in self.model_fields_set:
            _dict['removeCompletedDownloads'] = None

        # set to None if remove_failed_downloads (nullable) is None
        # and model_fields_set contains the field
        if self.remove_failed_downloads is None and "remove_failed_downloads" in self.model_fields_set:
            _dict['removeFailedDownloads'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DownloadClientBulkResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ids": obj.get("ids"),
            "tags": obj.get("tags"),
            "applyTags": obj.get("applyTags"),
            "enable": obj.get("enable"),
            "priority": obj.get("priority"),
            "removeCompletedDownloads": obj.get("removeCompletedDownloads"),
            "removeFailedDownloads": obj.get("removeFailedDownloads")
        })
        return _obj


