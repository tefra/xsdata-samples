from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRestrictionSaleDate:
    """
    Restrict when this fare can be sold.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        }
    )
    end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        }
    )
