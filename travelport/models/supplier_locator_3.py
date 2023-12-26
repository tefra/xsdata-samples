from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate, XmlDateTime
from travelport.models.type_general_reference_3 import TypeGeneralReference3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class SupplierLocator3:
    """
    Locator code on the host carrier system.

    Parameters
    ----------
    segment_ref
        Air/Passive Segment Reference
    supplier_code
        Carrier Code
    supplier_locator_code
        Carrier reservation locator code
    provider_reservation_info_ref
        Provider Reservation  reference
    create_date_time
        The Date and Time which the reservation is received from the Vendor
        as a SupplierLocator creation Date.
    """

    class Meta:
        name = "SupplierLocator"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    segment_ref: list[TypeGeneralReference3] = field(
        default_factory=list,
        metadata={
            "name": "SegmentRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
    supplier_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierLocatorCode",
            "type": "Attribute",
            "required": True,
        },
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        },
    )
    create_date_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "CreateDateTime",
            "type": "Attribute",
        },
    )
