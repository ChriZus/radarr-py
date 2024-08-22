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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from radarr.models.language import Language
from radarr.models.quality_model import QualityModel
from typing import Optional, Set
from typing_extensions import Self

class MovieFileListResource(BaseModel):
    """
    MovieFileListResource
    """ # noqa: E501
    movie_file_ids: Optional[List[StrictInt]] = Field(default=None, alias="movieFileIds")
    languages: Optional[List[Language]] = None
    quality: Optional[QualityModel] = None
    edition: Optional[StrictStr] = None
    release_group: Optional[StrictStr] = Field(default=None, alias="releaseGroup")
    scene_name: Optional[StrictStr] = Field(default=None, alias="sceneName")
    indexer_flags: Optional[StrictInt] = Field(default=None, alias="indexerFlags")
    __properties: ClassVar[List[str]] = ["movieFileIds", "languages", "quality", "edition", "releaseGroup", "sceneName", "indexerFlags"]

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
        """Create an instance of MovieFileListResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item_languages in self.languages:
                if _item_languages:
                    _items.append(_item_languages.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # set to None if movie_file_ids (nullable) is None
        # and model_fields_set contains the field
        if self.movie_file_ids is None and "movie_file_ids" in self.model_fields_set:
            _dict['movieFileIds'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if edition (nullable) is None
        # and model_fields_set contains the field
        if self.edition is None and "edition" in self.model_fields_set:
            _dict['edition'] = None

        # set to None if release_group (nullable) is None
        # and model_fields_set contains the field
        if self.release_group is None and "release_group" in self.model_fields_set:
            _dict['releaseGroup'] = None

        # set to None if scene_name (nullable) is None
        # and model_fields_set contains the field
        if self.scene_name is None and "scene_name" in self.model_fields_set:
            _dict['sceneName'] = None

        # set to None if indexer_flags (nullable) is None
        # and model_fields_set contains the field
        if self.indexer_flags is None and "indexer_flags" in self.model_fields_set:
            _dict['indexerFlags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MovieFileListResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "movieFileIds": obj.get("movieFileIds"),
            "languages": [Language.from_dict(_item) for _item in obj["languages"]] if obj.get("languages") is not None else None,
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None,
            "edition": obj.get("edition"),
            "releaseGroup": obj.get("releaseGroup"),
            "sceneName": obj.get("sceneName"),
            "indexerFlags": obj.get("indexerFlags")
        })
        return _obj


