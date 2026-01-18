from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import TransTitle
from crossref.models.gov.nih.nlm.ncbi.jats1.trans_subtitle import TransSubtitle
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class TransTitleGroup:
    """
    <div> <h3>Translated Title Group</h3> </div>.
    """

    class Meta:
        name = "trans-title-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    trans_title: None | TransTitle = field(
        default=None,
        metadata={
            "name": "trans-title",
            "type": "Element",
            "required": True,
        },
    )
    trans_subtitle: list[TransSubtitle] = field(
        default_factory=list,
        metadata={
            "name": "trans-subtitle",
            "type": "Element",
        },
    )
    content_type: None | str = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: None | str = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: None | str | LangValue = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
