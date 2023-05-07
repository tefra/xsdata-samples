from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.annotation import TransTitle
from crossref.models.gov.nih.nlm.ncbi.jats1.trans_subtitle import TransSubtitle
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class TransTitleGroup:
    """
    <div> <h3>Translated Title Group</h3> </div>
    """
    class Meta:
        name = "trans-title-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    trans_title: Optional[TransTitle] = field(
        default=None,
        metadata={
            "name": "trans-title",
            "type": "Element",
            "required": True,
        }
    )
    trans_subtitle: List[TransSubtitle] = field(
        default_factory=list,
        metadata={
            "name": "trans-subtitle",
            "type": "Element",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
