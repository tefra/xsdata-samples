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

    parking_payment_code: str | None = field(
        default=None,
        metadata={
            "name": "ParkingPaymentCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_length: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_width: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_height: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_weight: Decimal | None = field(
        default=None,
        metadata={
            "name": "MaximumWeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
