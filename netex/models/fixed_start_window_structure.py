from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FixedStartWindowStructure:
    maximum_services_before: None | int = field(
        default=None,
        metadata={
            "name": "MaximumServicesBefore",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_period_before: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "FlexiblePeriodBefore",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_services_after: None | int = field(
        default=None,
        metadata={
            "name": "MaximumServicesAfter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_period_after: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "FlexiblePeriodAfter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
