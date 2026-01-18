from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class A:
    """
    content is "Inline" except that anchors shouldn't be nested.
    """

    class Meta:
        name = "a"
        namespace = "http://www.crossref.org/schema/5.3.1"

    href: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
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
                    "type": str,
                },
            ),
        },
    )
