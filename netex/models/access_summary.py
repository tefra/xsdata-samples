from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .access_summary_versioned_child_structure import (
    AccessSummaryVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessSummary(AccessSummaryVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
