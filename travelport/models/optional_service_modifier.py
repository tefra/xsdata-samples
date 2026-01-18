from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class OptionalServiceModifier:
    """
    Optional service modifiers.

    Parameters
    ----------
    type_value
        Optional service type
    secondary_type
        Secondary optional service type
    supplier_code
        Optional service supplier code
    service_sub_code
        As published by ATPCO
    travel_date
        The departure date of the air segment the optional service is valid
        for.
    description
        This allows MDS to return specific image and text corresponding to
        the ancillary name (S5 ancillary name).
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    secondary_type: None | str = field(
        default=None,
        metadata={
            "name": "SecondaryType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    supplier_code: str = field(
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        }
    )
    service_sub_code: str = field(
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "required": True,
        }
    )
    travel_date: XmlDate = field(
        metadata={
            "name": "TravelDate",
            "type": "Attribute",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "name": "Description",
            "type": "Attribute",
            "required": True,
        }
    )
