from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.service_sub_group import ServiceSubGroup

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class ServiceGroup:
    """
    The Service Group of the Ancillary Service.

    Providers: 1G, 1V, 1P, ACH.

    Parameters
    ----------
    service_sub_group
    code
        The Service Group Code of the Ancillary Service.  Providers: 1G, 1V,
        1P, ACH
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    service_sub_group: list[ServiceSubGroup] = field(
        default_factory=list,
        metadata={
            "name": "ServiceSubGroup",
            "type": "Element",
            "max_occurs": 15,
        },
    )
    code: str = field(
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        }
    )
