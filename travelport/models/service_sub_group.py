from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ServiceSubGroup:
    """The Service Sub Group of the Ancillary Service.

    Providers: 1G, 1V, 1P, ACH

    Parameters
    ----------
    code
        The Service Sub Group Code of the Ancillary Service.  Providers: 1G,
        1V, 1P, ACH
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        },
    )
