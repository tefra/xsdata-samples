from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ResourceId:
    """
    <div> <h3>Resource Identifier</h3> </div>
    """
    class Meta:
        name = "resource-id"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    assigning_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigning-authority",
            "type": "Attribute",
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
    resource_id_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "resource-id-type",
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
    vocab: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    vocab_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vocab-identifier",
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
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
