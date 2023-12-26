from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_advisory_type_2 import TypeAdvisoryType2
from travelport.models.type_geo_political_area_type_2 import (
    TypeGeoPoliticalAreaType2,
)
from travelport.models.type_key_element_2 import TypeKeyElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class Advisory2(TypeKeyElement2):
    """A categorization of travel documents and other identification, or other
    warnings that an agency may need to share with agents.

    Examples include visas requirements, travel permit requirements,
    passport requirements, etc. May also include government travel or
    health advisories.

    Parameters
    ----------
    type_value
        A categorization of travel documents and other identification, or
        other warnings that an agency may need to share with agents.
        Examples include visas requirements, travel permit requirements,
        passport requirements, etc. May also include government travel or
        health advisories.
    start_date
        The start date of the advisory
    end_date
        The end date of the advisory
    summary
        A summary of this Advisory
    description
    priority_order
        Priority order associated with this Advisory.
    geo_political_area_type
        The type of the geographical location.
    geo_political_area_code
        The location code of the geographical location.
    """

    class Meta:
        name = "Advisory"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    type_value: None | TypeAdvisoryType2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
            "required": True,
        },
    )
    end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        },
    )
    summary: None | str = field(
        default=None,
        metadata={
            "name": "Summary",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 1000,
        },
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    geo_political_area_type: None | TypeGeoPoliticalAreaType2 = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaType",
            "type": "Attribute",
            "required": True,
        },
    )
    geo_political_area_code: None | str = field(
        default=None,
        metadata={
            "name": "GeoPoliticalAreaCode",
            "type": "Attribute",
            "required": True,
            "max_length": 6,
        },
    )
