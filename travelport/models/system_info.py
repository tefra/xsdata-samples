from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/system_v32_0"


@dataclass
class SystemInfo:
    """
    Identifies the type of system and version running.

    Parameters
    ----------
    system_type
        Identifies whether or not this is a Production or Test system.
    application_version
        The running version of the system.
    description
        The description of the system.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/system_v32_0"

    system_type: None | str = field(
        default=None,
        metadata={
            "name": "SystemType",
            "type": "Attribute",
            "required": True,
        }
    )
    application_version: None | str = field(
        default=None,
        metadata={
            "name": "ApplicationVersion",
            "type": "Attribute",
            "required": True,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
