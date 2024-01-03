from dataclasses import dataclass, field
from typing import Any
from .alternative_texts_rel_structure import ValidBetweenVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimpleValidityCondition(ValidBetweenVersionStructure):
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
    key_list: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    extensions: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    branding_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    description: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    conditioned_object_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    with_condition_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
