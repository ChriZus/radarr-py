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

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel
from radarr.models.alternative_title import AlternativeTitle
from radarr.models.language import Language
from radarr.models.media_cover import MediaCover
from radarr.models.movie_status_type import MovieStatusType
from radarr.models.movie_translation import MovieTranslation
from radarr.models.ratings import Ratings

class MovieMetadata(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    tmdb_id: Optional[int]
    images: Optional[List]
    genres: Optional[List]
    in_cinemas: Optional[datetime]
    physical_release: Optional[datetime]
    digital_release: Optional[datetime]
    certification: Optional[str]
    year: Optional[int]
    ratings: Optional[Ratings]
    collection_tmdb_id: Optional[int]
    collection_title: Optional[str]
    last_info_sync: Optional[datetime]
    runtime: Optional[int]
    website: Optional[str]
    imdb_id: Optional[str]
    title: Optional[str]
    clean_title: Optional[str]
    sort_title: Optional[str]
    status: Optional[MovieStatusType]
    overview: Optional[str]
    alternative_titles: Optional[List]
    translations: Optional[List]
    secondary_year: Optional[int]
    you_tube_trailer_id: Optional[str]
    studio: Optional[str]
    original_title: Optional[str]
    clean_original_title: Optional[str]
    original_language: Optional[Language]
    recommendations: Optional[List]
    popularity: Optional[float]
    is_recent_movie: Optional[bool]
    __properties = ["id", "tmdbId", "images", "genres", "inCinemas", "physicalRelease", "digitalRelease", "certification", "year", "ratings", "collectionTmdbId", "collectionTitle", "lastInfoSync", "runtime", "website", "imdbId", "title", "cleanTitle", "sortTitle", "status", "overview", "alternativeTitles", "translations", "secondaryYear", "youTubeTrailerId", "studio", "originalTitle", "cleanOriginalTitle", "originalLanguage", "recommendations", "popularity", "isRecentMovie"]

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
    def from_json(cls, json_str: str) -> MovieMetadata:
        """Create an instance of MovieMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "is_recent_movie",
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
        # override the default output from pydantic by calling `to_dict()` of each item in alternative_titles (list)
        _items = []
        if self.alternative_titles:
            for _item in self.alternative_titles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alternativeTitles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in translations (list)
        _items = []
        if self.translations:
            for _item in self.translations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['translations'] = _items
        # override the default output from pydantic by calling `to_dict()` of original_language
        if self.original_language:
            _dict['originalLanguage'] = self.original_language.to_dict()
        # set to None if images (nullable) is None
        if self.images is None:
            _dict['images'] = None

        # set to None if genres (nullable) is None
        if self.genres is None:
            _dict['genres'] = None

        # set to None if in_cinemas (nullable) is None
        if self.in_cinemas is None:
            _dict['inCinemas'] = None

        # set to None if physical_release (nullable) is None
        if self.physical_release is None:
            _dict['physicalRelease'] = None

        # set to None if digital_release (nullable) is None
        if self.digital_release is None:
            _dict['digitalRelease'] = None

        # set to None if certification (nullable) is None
        if self.certification is None:
            _dict['certification'] = None

        # set to None if collection_title (nullable) is None
        if self.collection_title is None:
            _dict['collectionTitle'] = None

        # set to None if last_info_sync (nullable) is None
        if self.last_info_sync is None:
            _dict['lastInfoSync'] = None

        # set to None if website (nullable) is None
        if self.website is None:
            _dict['website'] = None

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

        # set to None if alternative_titles (nullable) is None
        if self.alternative_titles is None:
            _dict['alternativeTitles'] = None

        # set to None if translations (nullable) is None
        if self.translations is None:
            _dict['translations'] = None

        # set to None if secondary_year (nullable) is None
        if self.secondary_year is None:
            _dict['secondaryYear'] = None

        # set to None if you_tube_trailer_id (nullable) is None
        if self.you_tube_trailer_id is None:
            _dict['youTubeTrailerId'] = None

        # set to None if studio (nullable) is None
        if self.studio is None:
            _dict['studio'] = None

        # set to None if original_title (nullable) is None
        if self.original_title is None:
            _dict['originalTitle'] = None

        # set to None if clean_original_title (nullable) is None
        if self.clean_original_title is None:
            _dict['cleanOriginalTitle'] = None

        # set to None if recommendations (nullable) is None
        if self.recommendations is None:
            _dict['recommendations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MovieMetadata:
        """Create an instance of MovieMetadata from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MovieMetadata.parse_obj(obj)

        _obj = MovieMetadata.parse_obj({
            "id": obj.get("id"),
            "tmdb_id": obj.get("tmdbId"),
            "images": [MediaCover.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "genres": obj.get("genres"),
            "in_cinemas": obj.get("inCinemas"),
            "physical_release": obj.get("physicalRelease"),
            "digital_release": obj.get("digitalRelease"),
            "certification": obj.get("certification"),
            "year": obj.get("year"),
            "ratings": Ratings.from_dict(obj.get("ratings")) if obj.get("ratings") is not None else None,
            "collection_tmdb_id": obj.get("collectionTmdbId"),
            "collection_title": obj.get("collectionTitle"),
            "last_info_sync": obj.get("lastInfoSync"),
            "runtime": obj.get("runtime"),
            "website": obj.get("website"),
            "imdb_id": obj.get("imdbId"),
            "title": obj.get("title"),
            "clean_title": obj.get("cleanTitle"),
            "sort_title": obj.get("sortTitle"),
            "status": obj.get("status"),
            "overview": obj.get("overview"),
            "alternative_titles": [AlternativeTitle.from_dict(_item) for _item in obj.get("alternativeTitles")] if obj.get("alternativeTitles") is not None else None,
            "translations": [MovieTranslation.from_dict(_item) for _item in obj.get("translations")] if obj.get("translations") is not None else None,
            "secondary_year": obj.get("secondaryYear"),
            "you_tube_trailer_id": obj.get("youTubeTrailerId"),
            "studio": obj.get("studio"),
            "original_title": obj.get("originalTitle"),
            "clean_original_title": obj.get("cleanOriginalTitle"),
            "original_language": Language.from_dict(obj.get("originalLanguage")) if obj.get("originalLanguage") is not None else None,
            "recommendations": obj.get("recommendations"),
            "popularity": obj.get("popularity"),
            "is_recent_movie": obj.get("isRecentMovie")
        })
        return _obj

