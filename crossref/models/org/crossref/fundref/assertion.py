from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from crossref.models.org.crossref.fundref.assertion_name import AssertionName
from crossref.models.org.crossref.fundref.assertion_provider import (
    AssertionProvider,
)

__NAMESPACE__ = "http://www.crossref.org/fundref.xsd"


@dataclass
class Assertion:
    """
    FundRef attributes included in assertion are: fundgroup: used to group
    funding info for items with multiple funding sources.

    Required for items with multiple award_number assertions, optional for
    items with a single award_number funder_identifier: funding agency
    identifier, must be nested within the funder_name assertion
    funder_name: name of the funding agency (required) award_number: grant
    number or other fund identifier.
    """

    class Meta:
        name = "assertion"
        namespace = "http://www.crossref.org/fundref.xsd"

    provider: AssertionProvider = field(
        default=AssertionProvider.PUBLISHER,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | AssertionName = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "assertion",
                    "type": ForwardRef("Assertion"),
                },
            ),
        },
    )
