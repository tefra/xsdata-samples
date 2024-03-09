from dataclasses import dataclass, field
from typing import Any

from .passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassingTimeView(PassingTimeViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
