from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_stay_unit import TypeStayUnit

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeRestrictionLengthOfStay:
    """
    Length Of Stay Restriction ( e.g. 2 day minimum..)

    Parameters
    ----------
    length
    stay_unit
    stay_date
    more_rules_present
        If true, specifies that advance purchase information will be present
        in fare rules.
    """
    class Meta:
        name = "typeRestrictionLengthOfStay"

    length: None | int = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Attribute",
        }
    )
    stay_unit: None | TypeStayUnit = field(
        default=None,
        metadata={
            "name": "StayUnit",
            "type": "Attribute",
        }
    )
    stay_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StayDate",
            "type": "Attribute",
        }
    )
    more_rules_present: None | bool = field(
        default=None,
        metadata={
            "name": "MoreRulesPresent",
            "type": "Attribute",
        }
    )
