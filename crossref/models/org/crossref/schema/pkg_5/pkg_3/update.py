from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from crossref.models.org.crossref.schema.pkg_5.pkg_3.cm_update_type import (
    CmUpdateType,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Update:
    """The DOI of the content being updated (e.g. corrected, retracted, etc.) In
    the CrossMark Terms and Conditions "updates" are defined as changes that are
    likely to "change the reader’s interpretation or crediting of the work." That
    is, *editorially significant* changes.

    "Updates" should not include minor changes to spelling, punctuation,
    formatting, etc.

    :ivar type_value: This attribute should be used to list the update
        type. Allowed update types are: <ul xmlns=""> <li>addendum</li>
        <li>clarification</li> <li>correction</li> <li>corrigendum</li>
        <li>erratum</li> <li>expression_of_concern</li>
        <li>new_edition</li> <li>new_version</li>
        <li>partial_retraction</li> <li>removal</li> <li>retraction</li>
        <li>withdrawal</li> </ul>
    :ivar date: The date of the update will be displayed in the
        CrossMark dialog and can help the researcher easily tell whether
        they are likley to have seen the update.
    :ivar content:
    """

    class Meta:
        name = "update"
        namespace = "http://www.crossref.org/schema/5.3.1"

    type_value: Optional[CmUpdateType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "type": str,
                    "default": "",
                    "min_length": 6,
                    "max_length": 2048,
                    "pattern": r"10\.[0-9]{4,9}/.{1,200}",
                },
            ),
        },
    )
