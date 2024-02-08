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



from pydantic import BaseModel
from radarr.models.custom_format_resource import CustomFormatResource
from radarr.models.language import Language
from radarr.models.media_info_resource import MediaInfoResource
from radarr.models.quality_model import QualityModel

class MovieFileResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    movie_id: Optional[int]
    relative_path: Optional[str]
    path: Optional[str]
    size: Optional[int]
    date_added: Optional[datetime]
    scene_name: Optional[str]
    indexer_flags: Optional[int]
    quality: Optional[QualityModel]
    custom_formats: Optional[List]
    custom_format_score: Optional[int]
    media_info: Optional[MediaInfoResource]
    original_file_path: Optional[str]
    quality_cutoff_not_met: Optional[bool]
    languages: Optional[List]
    release_group: Optional[str]
    edition: Optional[str]
    __properties = ["id", "movieId", "relativePath", "path", "size", "dateAdded", "sceneName", "indexerFlags", "quality", "customFormats", "customFormatScore", "mediaInfo", "originalFilePath", "qualityCutoffNotMet", "languages", "releaseGroup", "edition"]

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
    def from_json(cls, json_str: str) -> MovieFileResource:
        """Create an instance of MovieFileResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in languages (list)
        _items = []
        if self.languages:
            for _item in self.languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['languages'] = _items
        # set to None if relative_path (nullable) is None
        if self.relative_path is None:
            _dict['relativePath'] = None

        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if scene_name (nullable) is None
        if self.scene_name is None:
            _dict['sceneName'] = None

        # set to None if custom_formats (nullable) is None
        if self.custom_formats is None:
            _dict['customFormats'] = None

        # set to None if original_file_path (nullable) is None
        if self.original_file_path is None:
            _dict['originalFilePath'] = None

        # set to None if languages (nullable) is None
        if self.languages is None:
            _dict['languages'] = None

        # set to None if release_group (nullable) is None
        if self.release_group is None:
            _dict['releaseGroup'] = None

        # set to None if edition (nullable) is None
        if self.edition is None:
            _dict['edition'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MovieFileResource:
        """Create an instance of MovieFileResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MovieFileResource.parse_obj(obj)

        _obj = MovieFileResource.parse_obj({
            "id": obj.get("id"),
            "movie_id": obj.get("movieId"),
            "relative_path": obj.get("relativePath"),
            "path": obj.get("path"),
            "size": obj.get("size"),
            "date_added": obj.get("dateAdded"),
            "scene_name": obj.get("sceneName"),
            "indexer_flags": obj.get("indexerFlags"),
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "custom_formats": [CustomFormatResource.from_dict(_item) for _item in obj.get("customFormats")] if obj.get("customFormats") is not None else None,
            "custom_format_score": obj.get("customFormatScore"),
            "media_info": MediaInfoResource.from_dict(obj.get("mediaInfo")) if obj.get("mediaInfo") is not None else None,
            "original_file_path": obj.get("originalFilePath"),
            "quality_cutoff_not_met": obj.get("qualityCutoffNotMet"),
            "languages": [Language.from_dict(_item) for _item in obj.get("languages")] if obj.get("languages") is not None else None,
            "release_group": obj.get("releaseGroup"),
            "edition": obj.get("edition")
        })
        return _obj

