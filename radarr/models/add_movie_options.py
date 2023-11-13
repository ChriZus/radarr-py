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


from typing import Any, ClassVar, Dict, Optional
from pydantic import BaseModel
from radarr.models.add_movie_method import AddMovieMethod
from radarr.models.monitor_types import MonitorTypes

class AddMovieOptions(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    ignore_episodes_with_files: Optional[bool]
    ignore_episodes_without_files: Optional[bool]
    monitor: Optional[MonitorTypes]
    search_for_movie: Optional[bool]
    add_method: Optional[AddMovieMethod]
    __properties = ["ignoreEpisodesWithFiles", "ignoreEpisodesWithoutFiles", "monitor", "searchForMovie", "addMethod"]

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
    def from_json(cls, json_str: str) -> AddMovieOptions:
        """Create an instance of AddMovieOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddMovieOptions:
        """Create an instance of AddMovieOptions from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AddMovieOptions.parse_obj(obj)

        _obj = AddMovieOptions.parse_obj({
            "ignore_episodes_with_files": obj.get("ignoreEpisodesWithFiles"),
            "ignore_episodes_without_files": obj.get("ignoreEpisodesWithoutFiles"),
            "monitor": obj.get("monitor"),
            "search_for_movie": obj.get("searchForMovie"),
            "add_method": obj.get("addMethod")
        })
        return _obj

