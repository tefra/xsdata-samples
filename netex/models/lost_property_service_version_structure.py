from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .customer_service_version_structure import CustomerServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LostPropertyServiceVersionStructure(CustomerServiceVersionStructure):
    class Meta:
        name = "LostPropertyService_VersionStructure"

    property_kept_for_duration: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "PropertyKeptForDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
