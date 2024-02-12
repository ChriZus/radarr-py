# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class RemotePathMappingResource(BaseModel):
    """
    RemotePathMappingResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    host: Optional[StrictStr] = None
    remote_path: Optional[StrictStr] = Field(default=None, alias="remotePath")
    local_path: Optional[StrictStr] = Field(default=None, alias="localPath")
    __properties: ClassVar[List[str]] = ["id", "host", "remotePath", "localPath"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RemotePathMappingResource from a JSON string"""
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
        # set to None if host (nullable) is None
        # and model_fields_set contains the field
        if self.host is None and "host" in self.model_fields_set:
            _dict['host'] = None

        # set to None if remote_path (nullable) is None
        # and model_fields_set contains the field
        if self.remote_path is None and "remote_path" in self.model_fields_set:
            _dict['remotePath'] = None

        # set to None if local_path (nullable) is None
        # and model_fields_set contains the field
        if self.local_path is None and "local_path" in self.model_fields_set:
            _dict['localPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RemotePathMappingResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "host": obj.get("host"),
            "remotePath": obj.get("remotePath"),
            "localPath": obj.get("localPath")
        })
        return _obj


