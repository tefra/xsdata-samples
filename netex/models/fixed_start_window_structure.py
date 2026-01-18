from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FixedStartWindowStructure:
    maximum_services_before: int | None = field(
        default=None,
        metadata={
            "name": "MaximumServicesBefore",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_period_before: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "FlexiblePeriodBefore",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_services_after: int | None = field(
        default=None,
        metadata={
            "name": "MaximumServicesAfter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_period_after: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "FlexiblePeriodAfter",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
