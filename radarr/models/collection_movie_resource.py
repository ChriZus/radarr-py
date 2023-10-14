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
from radarr.models.media_cover import MediaCover
from radarr.models.movie_status_type import MovieStatusType
from radarr.models.ratings import Ratings

class CollectionMovieResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    tmdb_id: Optional[int]
    imdb_id: Optional[str]
    title: Optional[str]
    clean_title: Optional[str]
    sort_title: Optional[str]
    status: Optional[MovieStatusType]
    overview: Optional[str]
    runtime: Optional[int]
    images: Optional[List]
    year: Optional[int]
    ratings: Optional[Ratings]
    genres: Optional[List]
    folder: Optional[str]
    __properties = ["tmdbId", "imdbId", "title", "cleanTitle", "sortTitle", "status", "overview", "runtime", "images", "year", "ratings", "genres", "folder"]

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
    def from_json(cls, json_str: str) -> CollectionMovieResource:
        """Create an instance of CollectionMovieResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # set to None if imdb_id (nullable) is None
        if self.imdb_id is None:
            _dict['imdbId'] = None

        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if clean_title (nullable) is None
        if self.clean_title is None:
            _dict['cleanTitle'] = None

        # set to None if sort_title (nullable) is None
        if self.sort_title is None:
            _dict['sortTitle'] = None

        # set to None if overview (nullable) is None
        if self.overview is None:
            _dict['overview'] = None

        # set to None if images (nullable) is None
        if self.images is None:
            _dict['images'] = None

        # set to None if genres (nullable) is None
        if self.genres is None:
            _dict['genres'] = None

        # set to None if folder (nullable) is None
        if self.folder is None:
            _dict['folder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CollectionMovieResource:
        """Create an instance of CollectionMovieResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CollectionMovieResource.parse_obj(obj)

        _obj = CollectionMovieResource.parse_obj({
            "tmdb_id": obj.get("tmdbId"),
            "imdb_id": obj.get("imdbId"),
            "title": obj.get("title"),
            "clean_title": obj.get("cleanTitle"),
            "sort_title": obj.get("sortTitle"),
            "status": obj.get("status"),
            "overview": obj.get("overview"),
            "runtime": obj.get("runtime"),
            "images": [MediaCover.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "year": obj.get("year"),
            "ratings": Ratings.from_dict(obj.get("ratings")) if obj.get("ratings") is not None else None,
            "genres": obj.get("genres"),
            "folder": obj.get("folder")
        })
        return _obj

