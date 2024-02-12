# coding: utf-8

"""
    Radarr

    Radarr API docs

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from radarr.models.command import Command
from radarr.models.command_priority import CommandPriority
from radarr.models.command_result import CommandResult
from radarr.models.command_status import CommandStatus
from radarr.models.command_trigger import CommandTrigger
from typing import Optional, Set
from typing_extensions import Self

class CommandResource(BaseModel):
    """
    CommandResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    command_name: Optional[StrictStr] = Field(default=None, alias="commandName")
    message: Optional[StrictStr] = None
    body: Optional[Command] = None
    priority: Optional[CommandPriority] = None
    status: Optional[CommandStatus] = None
    result: Optional[CommandResult] = None
    queued: Optional[datetime] = None
    started: Optional[datetime] = None
    ended: Optional[datetime] = None
    duration: Optional[StrictStr] = None
    exception: Optional[StrictStr] = None
    trigger: Optional[CommandTrigger] = None
    client_user_agent: Optional[StrictStr] = Field(default=None, alias="clientUserAgent")
    state_change_time: Optional[datetime] = Field(default=None, alias="stateChangeTime")
    send_updates_to_client: Optional[StrictBool] = Field(default=None, alias="sendUpdatesToClient")
    update_scheduled_task: Optional[StrictBool] = Field(default=None, alias="updateScheduledTask")
    last_execution_time: Optional[datetime] = Field(default=None, alias="lastExecutionTime")
    __properties: ClassVar[List[str]] = ["id", "name", "commandName", "message", "body", "priority", "status", "result", "queued", "started", "ended", "duration", "exception", "trigger", "clientUserAgent", "stateChangeTime", "sendUpdatesToClient", "updateScheduledTask", "lastExecutionTime"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CommandResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of body
        if self.body:
            _dict['body'] = self.body.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if command_name (nullable) is None
        # and model_fields_set contains the field
        if self.command_name is None and "command_name" in self.model_fields_set:
            _dict['commandName'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if started (nullable) is None
        # and model_fields_set contains the field
        if self.started is None and "started" in self.model_fields_set:
            _dict['started'] = None

        # set to None if ended (nullable) is None
        # and model_fields_set contains the field
        if self.ended is None and "ended" in self.model_fields_set:
            _dict['ended'] = None

        # set to None if exception (nullable) is None
        # and model_fields_set contains the field
        if self.exception is None and "exception" in self.model_fields_set:
            _dict['exception'] = None

        # set to None if client_user_agent (nullable) is None
        # and model_fields_set contains the field
        if self.client_user_agent is None and "client_user_agent" in self.model_fields_set:
            _dict['clientUserAgent'] = None

        # set to None if state_change_time (nullable) is None
        # and model_fields_set contains the field
        if self.state_change_time is None and "state_change_time" in self.model_fields_set:
            _dict['stateChangeTime'] = None

        # set to None if last_execution_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_execution_time is None and "last_execution_time" in self.model_fields_set:
            _dict['lastExecutionTime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommandResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "commandName": obj.get("commandName"),
            "message": obj.get("message"),
            "body": Command.from_dict(obj["body"]) if obj.get("body") is not None else None,
            "priority": obj.get("priority"),
            "status": obj.get("status"),
            "result": obj.get("result"),
            "queued": obj.get("queued"),
            "started": obj.get("started"),
            "ended": obj.get("ended"),
            "duration": obj.get("duration"),
            "exception": obj.get("exception"),
            "trigger": obj.get("trigger"),
            "clientUserAgent": obj.get("clientUserAgent"),
            "stateChangeTime": obj.get("stateChangeTime"),
            "sendUpdatesToClient": obj.get("sendUpdatesToClient"),
            "updateScheduledTask": obj.get("updateScheduledTask"),
            "lastExecutionTime": obj.get("lastExecutionTime")
        })
        return _obj


