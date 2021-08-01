from dataclasses import dataclass, field
from datexii.models.eu.datexii.v2.versioned_reference import VersionedReference

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MeasurementSiteRecordVersionedReference(VersionedReference):
    class Meta:
        name = "_MeasurementSiteRecordVersionedReference"

    target_class: str = field(
        init=False,
        default="MeasurementSiteRecord",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
        }
    )
