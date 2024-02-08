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
from radarr.models.provider_message_type import ProviderMessageType

class ProviderMessage(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    message: Optional[str]
    type: Optional[ProviderMessageType]
    __properties = ["message", "type"]

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
    def from_json(cls, json_str: str) -> ProviderMessage:
        """Create an instance of ProviderMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if message (nullable) is None
        if self.message is None:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProviderMessage:
        """Create an instance of ProviderMessage from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProviderMessage.parse_obj(obj)

        _obj = ProviderMessage.parse_obj({
            "message": obj.get("message"),
            "type": obj.get("type")
        })
        return _obj

