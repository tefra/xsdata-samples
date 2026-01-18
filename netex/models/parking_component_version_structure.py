from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .multilingual_string import MultilingualString
from .site_component_version_structure import SiteComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingComponentVersionStructure(SiteComponentVersionStructure):
    class Meta:
        name = "ParkingComponent_VersionStructure"

    parking_payment_code: None | str = field(
        default=None,
        metadata={
            "name": "ParkingPaymentCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_length: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_width: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_weight: None | Decimal = field(
        default=None,
        metadata={
            "name": "MaximumWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
