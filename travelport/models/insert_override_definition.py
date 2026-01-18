from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.override_definition import OverrideDefinition

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class InsertOverrideDefinition:
    """
    Insert new override Definition.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    override_definition: list[OverrideDefinition] = field(
        default_factory=list,
        metadata={
            "name": "OverrideDefinition",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
