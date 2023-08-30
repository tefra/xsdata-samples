from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.xref_faces import (
    B,
    Em,
    Font,
    I,
    Ovl,
    Scp,
    Strong,
    Sub,
    Sup,
    Tt,
    U,
)
from crossref.models.org.w3.pkg_1998.math.math_ml.math import Math

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Assertion:
    """
    An assertion is a piece of custom, non-bibliographic metadata that the
    publisher is asserting about the content to which the Crossmark refers.

    :ivar explanation: If the publisher wants to provide a further
        explanation of what the particular "assertion" means, they can
        link to such an explanation by providing an appropriate url on
        the "explanation" attribute.
    :ivar group_label: This is the human-readable form of the
        "group_name" attribute. This is what will be displayed in the
        group headings on the Crossmark metadata record dialog.
    :ivar group_name: Some assertions could be logically "grouped"
        together in the CrossMark dialog. For instance, if the publisher
        is recording several pieces of metadata related to funding
        sources (source name, percentage, grant number), they may want
        to make sure that these three assertions are grouped next to
        each-other in the CrossMark dialog. The group_name attribute is
        the machine-readable value that will be used for grouping such
        assertions.
    :ivar label: This is the human-readable version of the name
        attribute which will be displayed in the CrossMark dialog. If
        this attribute is missing, then the value of the assertion will
        *not* be displayed in the dialog. Publishers may want to "hide"
        assertions this way in cases where the assertion value is too
        large or too complex to display in the dialog, but where the
        assertion is nonetheless valuable enough to include in API
        queries and metadata dumps (e.g. detailed licensing terms)
    :ivar name: This is the machine-readable name of the assertion. Use
        the "label" attribute to provide a human-readable version of the
        name.
    :ivar order: The publisher may want to control the order in which
        assertions are displayed to the user in the CrossMark dialog.
        All assertions will be sorted by this element if it is present.
    :ivar href:
    :ivar content:
    """
    class Meta:
        name = "assertion"
        namespace = "http://www.crossref.org/schema/5.3.1"

    explanation: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    group_label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 2,
            "max_length": 150,
        }
    )
    group_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 2,
            "max_length": 150,
        }
    )
    label: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 2,
            "max_length": 150,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 150,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "i",
                    "type": I,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "strong",
                    "type": Strong,
                },
                {
                    "name": "u",
                    "type": U,
                },
                {
                    "name": "ovl",
                    "type": Ovl,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "scp",
                    "type": Scp,
                },
                {
                    "name": "tt",
                    "type": Tt,
                },
                {
                    "name": "font",
                    "type": Font,
                },
                {
                    "name": "math",
                    "type": Math,
                    "namespace": "http://www.w3.org/1998/Math/MathML",
                },
            ),
        }
    )
