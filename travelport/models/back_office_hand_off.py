from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_back_office import TypeBackOffice

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class BackOfficeHandOff:
    """
    Allows an agency to select the back office documents and also route to
    different host to produce for the itinerary.

    Parameters
    ----------
    type_value
        The type of back office document,valid options are
        Accounting,Global,NonAccounting,NonAccountingRemote,Dual.
    location
        This is required for NonAccountingRemote,Dual and Global type back
        office.
    pseudo_city_code
        The PCC of the host system where it would be routed.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    type_value: None | TypeBackOffice = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
