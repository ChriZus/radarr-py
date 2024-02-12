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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from radarr.models.language import Language
from radarr.models.profile_format_item_resource import ProfileFormatItemResource
from radarr.models.quality_profile_quality_item_resource import QualityProfileQualityItemResource
from typing import Optional, Set
from typing_extensions import Self

class QualityProfileResource(BaseModel):
    """
    QualityProfileResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    upgrade_allowed: Optional[StrictBool] = Field(default=None, alias="upgradeAllowed")
    cutoff: Optional[StrictInt] = None
    items: Optional[List[QualityProfileQualityItemResource]] = None
    min_format_score: Optional[StrictInt] = Field(default=None, alias="minFormatScore")
    cutoff_format_score: Optional[StrictInt] = Field(default=None, alias="cutoffFormatScore")
    format_items: Optional[List[ProfileFormatItemResource]] = Field(default=None, alias="formatItems")
    language: Optional[Language] = None
    __properties: ClassVar[List[str]] = ["id", "name", "upgradeAllowed", "cutoff", "items", "minFormatScore", "cutoffFormatScore", "formatItems", "language"]

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
        """Create an instance of QualityProfileResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in format_items (list)
        _items = []
        if self.format_items:
            for _item in self.format_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['formatItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of language
        if self.language:
            _dict['language'] = self.language.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        # set to None if format_items (nullable) is None
        # and model_fields_set contains the field
        if self.format_items is None and "format_items" in self.model_fields_set:
            _dict['formatItems'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QualityProfileResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "upgradeAllowed": obj.get("upgradeAllowed"),
            "cutoff": obj.get("cutoff"),
            "items": [QualityProfileQualityItemResource.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "minFormatScore": obj.get("minFormatScore"),
            "cutoffFormatScore": obj.get("cutoffFormatScore"),
            "formatItems": [ProfileFormatItemResource.from_dict(_item) for _item in obj["formatItems"]] if obj.get("formatItems") is not None else None,
            "language": Language.from_dict(obj["language"]) if obj.get("language") is not None else None
        })
        return _obj


