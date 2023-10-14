# coding: utf-8

"""
    Radarr

    Radarr API docs  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from radarr.models.language import Language
from radarr.models.quality_model import QualityModel

class MovieFileListResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    movie_file_ids: Optional[List]
    languages: Optional[List]
    quality: Optional[QualityModel]
    edition: Optional[str]
    release_group: Optional[str]
    scene_name: Optional[str]
    indexer_flags: Optional[int]
    __properties = ["movieFileIds", "languages", "quality", "edition", "releaseGroup", "sceneName", "indexerFlags"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MovieFileListResource:
        """Create an instance of MovieFileListResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # set to None if movie_file_ids (nullable) is None
        if self.movie_file_ids is None:
            _dict['movieFileIds'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        # set to None if edition (nullable) is None
        if self.edition is None:
            _dict['edition'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if scene_name (nullable) is None
        if self.scene_name is None:
            _dict['sceneName'] = None

        # set to None if indexer_flags (nullable) is None
        if self.indexer_flags is None:
            _dict['indexerFlags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MovieFileListResource:
        """Create an instance of MovieFileListResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MovieFileListResource.parse_obj(obj)

        _obj = MovieFileListResource.parse_obj({
            "movie_file_ids": obj.get("movieFileIds"),
            "languages": [Language.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None,
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "edition": obj.get("edition"),
            "release_group": obj.get("releaseGroup"),
            "scene_name": obj.get("sceneName"),
            "indexer_flags": obj.get("indexerFlags")
        })
        return _obj

