# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: v5.10.4.9218
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from radarr.models.blocklist_resource import BlocklistResource
from radarr.models.sort_direction import SortDirection
from typing import Optional, Set
from typing_extensions import Self

class BlocklistResourcePagingResource(BaseModel):
    """
    BlocklistResourcePagingResource
    """ # noqa: E501
    page: Optional[StrictInt] = None
    page_size: Optional[StrictInt] = Field(default=None, alias="pageSize")
    sort_key: Optional[StrictStr] = Field(default=None, alias="sortKey")
    sort_direction: Optional[SortDirection] = Field(default=None, alias="sortDirection")
    total_records: Optional[StrictInt] = Field(default=None, alias="totalRecords")
    records: Optional[List[BlocklistResource]] = None
    __properties: ClassVar[List[str]] = ["page", "pageSize", "sortKey", "sortDirection", "totalRecords", "records"]

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
        """Create an instance of BlocklistResourcePagingResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in records (list)
        _items = []
        if self.records:
            for _item_records in self.records:
                if _item_records:
                    _items.append(_item_records.to_dict())
            _dict['records'] = _items
        # set to None if sort_key (nullable) is None
        # and model_fields_set contains the field
        if self.sort_key is None and "sort_key" in self.model_fields_set:
            _dict['sortKey'] = None

        # set to None if records (nullable) is None
        # and model_fields_set contains the field
        if self.records is None and "records" in self.model_fields_set:
            _dict['records'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BlocklistResourcePagingResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "page": obj.get("page"),
            "pageSize": obj.get("pageSize"),
            "sortKey": obj.get("sortKey"),
            "sortDirection": obj.get("sortDirection"),
            "totalRecords": obj.get("totalRecords"),
            "records": [BlocklistResource.from_dict(_item) for _item in obj["records"]] if obj.get("records") is not None else None
        })
        return _obj


