from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.models.multilingual_string import MultilingualString
from netex.models.site_component_version_structure import SiteComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingComponentVersionStructure(SiteComponentVersionStructure):
    class Meta:
        name = "ParkingComponent_VersionStructure"

    parking_payment_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParkingPaymentCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_weight: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
