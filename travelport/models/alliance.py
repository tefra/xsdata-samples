from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Alliance:
    """
    Alliance Code.

    Parameters
    ----------
    code
        The possible values are *A for Star Alliance,*O for One world,*S for
        Sky team etc.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
