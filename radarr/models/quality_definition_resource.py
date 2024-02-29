# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.3.6.8612
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional, Union
from radarr.models.quality import Quality
from typing import Optional, Set
from typing_extensions import Self

class QualityDefinitionResource(BaseModel):
    """
    QualityDefinitionResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    quality: Optional[Quality] = None
    title: Optional[StrictStr] = None
    weight: Optional[StrictInt] = None
    min_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="minSize")
    max_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxSize")
    preferred_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="preferredSize")
    __properties: ClassVar[List[str]] = ["id", "quality", "title", "weight", "minSize", "maxSize", "preferredSize"]

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
        """Create an instance of QualityDefinitionResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if min_size (nullable) is None
        # and model_fields_set contains the field
        if self.min_size is None and "min_size" in self.model_fields_set:
            _dict['minSize'] = None

        # set to None if max_size (nullable) is None
        # and model_fields_set contains the field
        if self.max_size is None and "max_size" in self.model_fields_set:
            _dict['maxSize'] = None

        # set to None if preferred_size (nullable) is None
        # and model_fields_set contains the field
        if self.preferred_size is None and "preferred_size" in self.model_fields_set:
            _dict['preferredSize'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QualityDefinitionResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "quality": Quality.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "title": obj.get("title"),
            "weight": obj.get("weight"),
            "minSize": obj.get("minSize"),
            "maxSize": obj.get("maxSize"),
            "preferredSize": obj.get("preferredSize")
        })
        return _obj


