from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_fare_guarantee import TypeFareGuarantee

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareGuaranteeInfo:
    """
    The information related to fare guarantee details.

    Parameters
    ----------
    guarantee_date
        The date till which the fare is guaranteed.
    guarantee_type
        Determines the status of a fare for a passenger.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    guarantee_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "GuaranteeDate",
            "type": "Attribute",
        },
    )
    guarantee_type: None | TypeFareGuarantee = field(
        default=None,
        metadata={
            "name": "GuaranteeType",
            "type": "Attribute",
            "required": True,
        },
    )
