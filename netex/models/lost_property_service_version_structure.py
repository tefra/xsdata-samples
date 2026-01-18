from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .customer_service_version_structure import CustomerServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LostPropertyServiceVersionStructure(CustomerServiceVersionStructure):
    class Meta:
        name = "LostPropertyService_VersionStructure"

    property_kept_for_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "PropertyKeptForDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
