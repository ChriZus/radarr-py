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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from radarr.models.add_movie_options import AddMovieOptions
from radarr.models.alternative_title_resource import AlternativeTitleResource
from radarr.models.language import Language
from radarr.models.media_cover import MediaCover
from radarr.models.movie_collection_resource import MovieCollectionResource
from radarr.models.movie_file_resource import MovieFileResource
from radarr.models.movie_statistics_resource import MovieStatisticsResource
from radarr.models.movie_status_type import MovieStatusType
from radarr.models.ratings import Ratings
from typing import Optional, Set
from typing_extensions import Self

class MovieResource(BaseModel):
    """
    MovieResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    original_title: Optional[StrictStr] = Field(default=None, alias="originalTitle")
    original_language: Optional[Language] = Field(default=None, alias="originalLanguage")
    alternate_titles: Optional[List[AlternativeTitleResource]] = Field(default=None, alias="alternateTitles")
    secondary_year: Optional[StrictInt] = Field(default=None, alias="secondaryYear")
    secondary_year_source_id: Optional[StrictInt] = Field(default=None, alias="secondaryYearSourceId")
    sort_title: Optional[StrictStr] = Field(default=None, alias="sortTitle")
    size_on_disk: Optional[StrictInt] = Field(default=None, alias="sizeOnDisk")
    status: Optional[MovieStatusType] = None
    overview: Optional[StrictStr] = None
    in_cinemas: Optional[datetime] = Field(default=None, alias="inCinemas")
    physical_release: Optional[datetime] = Field(default=None, alias="physicalRelease")
    digital_release: Optional[datetime] = Field(default=None, alias="digitalRelease")
    physical_release_note: Optional[StrictStr] = Field(default=None, alias="physicalReleaseNote")
    images: Optional[List[MediaCover]] = None
    website: Optional[StrictStr] = None
    remote_poster: Optional[StrictStr] = Field(default=None, alias="remotePoster")
    year: Optional[StrictInt] = None
    you_tube_trailer_id: Optional[StrictStr] = Field(default=None, alias="youTubeTrailerId")
    studio: Optional[StrictStr] = None
    path: Optional[StrictStr] = None
    quality_profile_id: Optional[StrictInt] = Field(default=None, alias="qualityProfileId")
    has_file: Optional[StrictBool] = Field(default=None, alias="hasFile")
    monitored: Optional[StrictBool] = None
    minimum_availability: Optional[MovieStatusType] = Field(default=None, alias="minimumAvailability")
    is_available: Optional[StrictBool] = Field(default=None, alias="isAvailable")
    folder_name: Optional[StrictStr] = Field(default=None, alias="folderName")
    runtime: Optional[StrictInt] = None
    clean_title: Optional[StrictStr] = Field(default=None, alias="cleanTitle")
    imdb_id: Optional[StrictStr] = Field(default=None, alias="imdbId")
    tmdb_id: Optional[StrictInt] = Field(default=None, alias="tmdbId")
    title_slug: Optional[StrictStr] = Field(default=None, alias="titleSlug")
    root_folder_path: Optional[StrictStr] = Field(default=None, alias="rootFolderPath")
    folder: Optional[StrictStr] = None
    certification: Optional[StrictStr] = None
    genres: Optional[List[StrictStr]] = None
    tags: Optional[List[StrictInt]] = None
    added: Optional[datetime] = None
    add_options: Optional[AddMovieOptions] = Field(default=None, alias="addOptions")
    ratings: Optional[Ratings] = None
    movie_file: Optional[MovieFileResource] = Field(default=None, alias="movieFile")
    collection: Optional[MovieCollectionResource] = None
    popularity: Optional[Union[StrictFloat, StrictInt]] = None
    statistics: Optional[MovieStatisticsResource] = None
    __properties: ClassVar[List[str]] = ["id", "title", "originalTitle", "originalLanguage", "alternateTitles", "secondaryYear", "secondaryYearSourceId", "sortTitle", "sizeOnDisk", "status", "overview", "inCinemas", "physicalRelease", "digitalRelease", "physicalReleaseNote", "images", "website", "remotePoster", "year", "youTubeTrailerId", "studio", "path", "qualityProfileId", "hasFile", "monitored", "minimumAvailability", "isAvailable", "folderName", "runtime", "cleanTitle", "imdbId", "tmdbId", "titleSlug", "rootFolderPath", "folder", "certification", "genres", "tags", "added", "addOptions", "ratings", "movieFile", "collection", "popularity", "statistics"]

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
        """Create an instance of MovieResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of original_language
        if self.original_language:
            _dict['originalLanguage'] = self.original_language.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in alternate_titles (list)
        _items = []
        if self.alternate_titles:
            for _item in self.alternate_titles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alternateTitles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of add_options
        if self.add_options:
            _dict['addOptions'] = self.add_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of movie_file
        if self.movie_file:
            _dict['movieFile'] = self.movie_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of collection
        if self.collection:
            _dict['collection'] = self.collection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if original_title (nullable) is None
        # and model_fields_set contains the field
        if self.original_title is None and "original_title" in self.model_fields_set:
            _dict['originalTitle'] = None

        # set to None if alternate_titles (nullable) is None
        # and model_fields_set contains the field
        if self.alternate_titles is None and "alternate_titles" in self.model_fields_set:
            _dict['alternateTitles'] = None

        # set to None if secondary_year (nullable) is None
        # and model_fields_set contains the field
        if self.secondary_year is None and "secondary_year" in self.model_fields_set:
            _dict['secondaryYear'] = None

        # set to None if sort_title (nullable) is None
        # and model_fields_set contains the field
        if self.sort_title is None and "sort_title" in self.model_fields_set:
            _dict['sortTitle'] = None

        # set to None if size_on_disk (nullable) is None
        # and model_fields_set contains the field
        if self.size_on_disk is None and "size_on_disk" in self.model_fields_set:
            _dict['sizeOnDisk'] = None

        # set to None if overview (nullable) is None
        # and model_fields_set contains the field
        if self.overview is None and "overview" in self.model_fields_set:
            _dict['overview'] = None

        # set to None if in_cinemas (nullable) is None
        # and model_fields_set contains the field
        if self.in_cinemas is None and "in_cinemas" in self.model_fields_set:
            _dict['inCinemas'] = None

        # set to None if physical_release (nullable) is None
        # and model_fields_set contains the field
        if self.physical_release is None and "physical_release" in self.model_fields_set:
            _dict['physicalRelease'] = None

        # set to None if digital_release (nullable) is None
        # and model_fields_set contains the field
        if self.digital_release is None and "digital_release" in self.model_fields_set:
            _dict['digitalRelease'] = None

        # set to None if physical_release_note (nullable) is None
        # and model_fields_set contains the field
        if self.physical_release_note is None and "physical_release_note" in self.model_fields_set:
            _dict['physicalReleaseNote'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if website (nullable) is None
        # and model_fields_set contains the field
        if self.website is None and "website" in self.model_fields_set:
            _dict['website'] = None

        # set to None if remote_poster (nullable) is None
        # and model_fields_set contains the field
        if self.remote_poster is None and "remote_poster" in self.model_fields_set:
            _dict['remotePoster'] = None

        # set to None if you_tube_trailer_id (nullable) is None
        # and model_fields_set contains the field
        if self.you_tube_trailer_id is None and "you_tube_trailer_id" in self.model_fields_set:
            _dict['youTubeTrailerId'] = None

        # set to None if studio (nullable) is None
        # and model_fields_set contains the field
        if self.studio is None and "studio" in self.model_fields_set:
            _dict['studio'] = None

        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if has_file (nullable) is None
        # and model_fields_set contains the field
        if self.has_file is None and "has_file" in self.model_fields_set:
            _dict['hasFile'] = None

        # set to None if folder_name (nullable) is None
        # and model_fields_set contains the field
        if self.folder_name is None and "folder_name" in self.model_fields_set:
            _dict['folderName'] = None

        # set to None if clean_title (nullable) is None
        # and model_fields_set contains the field
        if self.clean_title is None and "clean_title" in self.model_fields_set:
            _dict['cleanTitle'] = None

        # set to None if imdb_id (nullable) is None
        # and model_fields_set contains the field
        if self.imdb_id is None and "imdb_id" in self.model_fields_set:
            _dict['imdbId'] = None

        # set to None if title_slug (nullable) is None
        # and model_fields_set contains the field
        if self.title_slug is None and "title_slug" in self.model_fields_set:
            _dict['titleSlug'] = None

        # set to None if root_folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.root_folder_path is None and "root_folder_path" in self.model_fields_set:
            _dict['rootFolderPath'] = None

        # set to None if folder (nullable) is None
        # and model_fields_set contains the field
        if self.folder is None and "folder" in self.model_fields_set:
            _dict['folder'] = None

        # set to None if certification (nullable) is None
        # and model_fields_set contains the field
        if self.certification is None and "certification" in self.model_fields_set:
            _dict['certification'] = None

        # set to None if genres (nullable) is None
        # and model_fields_set contains the field
        if self.genres is None and "genres" in self.model_fields_set:
            _dict['genres'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MovieResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "originalTitle": obj.get("originalTitle"),
            "originalLanguage": Language.from_dict(obj["originalLanguage"]) if obj.get("originalLanguage") is not None else None,
            "alternateTitles": [AlternativeTitleResource.from_dict(_item) for _item in obj["alternateTitles"]] if obj.get("alternateTitles") is not None else None,
            "secondaryYear": obj.get("secondaryYear"),
            "secondaryYearSourceId": obj.get("secondaryYearSourceId"),
            "sortTitle": obj.get("sortTitle"),
            "sizeOnDisk": obj.get("sizeOnDisk"),
            "status": obj.get("status"),
            "overview": obj.get("overview"),
            "inCinemas": obj.get("inCinemas"),
            "physicalRelease": obj.get("physicalRelease"),
            "digitalRelease": obj.get("digitalRelease"),
            "physicalReleaseNote": obj.get("physicalReleaseNote"),
            "images": [MediaCover.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "website": obj.get("website"),
            "remotePoster": obj.get("remotePoster"),
            "year": obj.get("year"),
            "youTubeTrailerId": obj.get("youTubeTrailerId"),
            "studio": obj.get("studio"),
            "path": obj.get("path"),
            "qualityProfileId": obj.get("qualityProfileId"),
            "hasFile": obj.get("hasFile"),
            "monitored": obj.get("monitored"),
            "minimumAvailability": obj.get("minimumAvailability"),
            "isAvailable": obj.get("isAvailable"),
            "folderName": obj.get("folderName"),
            "runtime": obj.get("runtime"),
            "cleanTitle": obj.get("cleanTitle"),
            "imdbId": obj.get("imdbId"),
            "tmdbId": obj.get("tmdbId"),
            "titleSlug": obj.get("titleSlug"),
            "rootFolderPath": obj.get("rootFolderPath"),
            "folder": obj.get("folder"),
            "certification": obj.get("certification"),
            "genres": obj.get("genres"),
            "tags": obj.get("tags"),
            "added": obj.get("added"),
            "addOptions": AddMovieOptions.from_dict(obj["addOptions"]) if obj.get("addOptions") is not None else None,
            "ratings": Ratings.from_dict(obj["ratings"]) if obj.get("ratings") is not None else None,
            "movieFile": MovieFileResource.from_dict(obj["movieFile"]) if obj.get("movieFile") is not None else None,
            "collection": MovieCollectionResource.from_dict(obj["collection"]) if obj.get("collection") is not None else None,
            "popularity": obj.get("popularity"),
            "statistics": MovieStatisticsResource.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None
        })
        return _obj


