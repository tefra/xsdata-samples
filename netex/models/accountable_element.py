from dataclasses import dataclass, field
from typing import Any

from .accountable_element_structure import AccountableElementStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccountableElement(AccountableElementStructure):
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
