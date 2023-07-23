from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.leg_price import LegPrice

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ExpertSolution:
    """
    Information about Expert Solution Route component retrieved from Knowledge
    Base.

    Parameters
    ----------
    leg_price
    key
    total_price
        The Total Price for the Solution.
    approximate_total_price
        The Converted Total Price in Agency's Default Currency Value
    created_date
        The Date on which this solution was created
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    leg_price: list[LegPrice] = field(
        default_factory=list,
        metadata={
            "name": "LegPrice",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    created_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "CreatedDate",
            "type": "Attribute",
            "required": True,
        }
    )
