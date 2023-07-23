from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_segment_ref import AirSegmentRef

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SelectionModifiers:
    """Modifiers supported for selection of services during EMD Issuance.

    Supported providers are 1V/1G/1P

    Parameters
    ----------
    air_segment_ref
        References to airsegments for which EMDs will be generated on all
        the associated services.
    svc_segment_ref
        SVC segment reference to which the EMD is being issued
    supplier_code
        Supplier/Vendor code for which EMDs will be generated on all the
        associated services. Required if PNR contains more than one
        supplier.
    rfic
        Reason for issuance code for which EMDs will be generated on all the
        associated services.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_ref: list[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    svc_segment_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SvcSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "length": 2,
        }
    )
    rfic: None | str = field(
        default=None,
        metadata={
            "name": "RFIC",
            "type": "Attribute",
            "length": 1,
        }
    )
