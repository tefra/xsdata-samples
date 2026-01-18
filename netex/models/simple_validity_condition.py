from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .entity_in_version_structure import ValidBetweenVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleValidityCondition(ValidBetweenVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    description: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    conditioned_object_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    with_condition_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    key_list: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    extensions: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    branding_ref: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
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
