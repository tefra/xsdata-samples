from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.versioned_reference import VersionedReference

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class SituationRecordVersionedReference(VersionedReference):
    class Meta:
        name = "_SituationRecordVersionedReference"

    target_class: str = field(
        init=False,
        default="SituationRecord",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        },
    )
