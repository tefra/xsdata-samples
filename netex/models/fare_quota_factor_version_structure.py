from dataclasses import dataclass, field
from typing import Optional
from netex.models.quality_structure_factor_version_structure import QualityStructureFactorVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareQuotaFactorVersionStructure(QualityStructureFactorVersionStructure):
    class Meta:
        name = "FareQuotaFactor_VersionStructure"

    number_of_units: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
