from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_mct_connection import TypeMctConnection

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class MctStandard:
    """
    The standard MCT time for the given search criteria.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    type_value: TypeMctConnection = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    time: int = field(
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        }
    )
