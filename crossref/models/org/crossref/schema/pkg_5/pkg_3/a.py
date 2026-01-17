from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class A:
    """
    content is "Inline" except that anchors shouldn't be nested.
    """

    class Meta:
        name = "a"
        namespace = "http://www.crossref.org/schema/5.3.1"

    href: Optional[str] = field(
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
