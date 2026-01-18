from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .quay_version_structure import QuayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TaxiStandVersionStructure(QuayVersionStructure):
    class Meta:
        name = "TaxiStand_VersionStructure"

    maximum_standing_duration: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "MaximumStandingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
