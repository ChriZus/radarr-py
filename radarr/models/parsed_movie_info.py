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


from typing import List, Optional
from pydantic import BaseModel
from radarr.models.language import Language
from radarr.models.quality_model import QualityModel

class ParsedMovieInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    movie_titles: Optional[List]
    original_title: Optional[str]
    release_title: Optional[str]
    simple_release_title: Optional[str]
    quality: Optional[QualityModel]
    languages: Optional[List]
    release_group: Optional[str]
    release_hash: Optional[str]
    edition: Optional[str]
    year: Optional[int]
    imdb_id: Optional[str]
    tmdb_id: Optional[int]
    hardcoded_subs: Optional[str]
    movie_title: Optional[str]
    primary_movie_title: Optional[str]
    __properties = ["movieTitles", "originalTitle", "releaseTitle", "simpleReleaseTitle", "quality", "languages", "releaseGroup", "releaseHash", "edition", "year", "imdbId", "tmdbId", "hardcodedSubs", "movieTitle", "primaryMovieTitle"]

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
    def from_json(cls, json_str: str) -> ParsedMovieInfo:
        """Create an instance of ParsedMovieInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "movie_title",
                            "primary_movie_title",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # set to None if movie_titles (nullable) is None
        if self.movie_titles is None:
            _dict['movieTitles'] = None

        # set to None if original_title (nullable) is None
        if self.original_title is None:
            _dict['originalTitle'] = None

        # set to None if release_title (nullable) is None
        if self.release_title is None:
            _dict['releaseTitle'] = None

        # set to None if simple_release_title (nullable) is None
        if self.simple_release_title is None:
            _dict['simpleReleaseTitle'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if release_hash (nullable) is None
        if self.release_hash is None:
            _dict['releaseHash'] = None

        # set to None if edition (nullable) is None
        if self.edition is None:
            _dict['edition'] = None

        # set to None if imdb_id (nullable) is None
        if self.imdb_id is None:
            _dict['imdbId'] = None

        # set to None if hardcoded_subs (nullable) is None
        if self.hardcoded_subs is None:
            _dict['hardcodedSubs'] = None

        # set to None if movie_title (nullable) is None
        if self.movie_title is None:
            _dict['movieTitle'] = None

        # set to None if primary_movie_title (nullable) is None
        if self.primary_movie_title is None:
            _dict['primaryMovieTitle'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ParsedMovieInfo:
        """Create an instance of ParsedMovieInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ParsedMovieInfo.parse_obj(obj)

        _obj = ParsedMovieInfo.parse_obj({
            "movie_titles": obj.get("movieTitles"),
            "original_title": obj.get("originalTitle"),
            "release_title": obj.get("releaseTitle"),
            "simple_release_title": obj.get("simpleReleaseTitle"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "languages": [Language.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None,
            "release_group": obj.get("releaseGroup"),
            "release_hash": obj.get("releaseHash"),
            "edition": obj.get("edition"),
            "year": obj.get("year"),
            "imdb_id": obj.get("imdbId"),
            "tmdb_id": obj.get("tmdbId"),
            "hardcoded_subs": obj.get("hardcodedSubs"),
            "movie_title": obj.get("movieTitle"),
            "primary_movie_title": obj.get("primaryMovieTitle")
        })
        return _obj

