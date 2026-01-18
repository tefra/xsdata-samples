from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class UniversalModifyCommandError:
    """
    Container to return modify command failures.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    universal_modify_cmd_key: str = field(
        metadata={
            "name": "UniversalModifyCmdKey",
            "type": "Attribute",
            "required": True,
        }
    )
