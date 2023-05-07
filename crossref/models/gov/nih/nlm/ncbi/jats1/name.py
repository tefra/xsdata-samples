from dataclasses import dataclass, field
from typing import List, Optional, Union
from crossref.models.gov.nih.nlm.ncbi.jats1.given_names import GivenNames
from crossref.models.gov.nih.nlm.ncbi.jats1.name_name_style import NameNameStyle
from crossref.models.gov.nih.nlm.ncbi.jats1.prefix import Prefix
from crossref.models.gov.nih.nlm.ncbi.jats1.suffix import Suffix
from crossref.models.gov.nih.nlm.ncbi.jats1.surname import Surname
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Name:
    """
    <div> <h3>Name of Person (Structured)</h3> </div>
    """
    class Meta:
        name = "name"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    surname: Optional[Surname] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    given_names: List[GivenNames] = field(
        default_factory=list,
        metadata={
            "name": "given-names",
            "type": "Element",
            "max_occurs": 2,
            "sequence": 2550,
        }
    )
    prefix: Optional[Prefix] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    suffix: Optional[Suffix] = field(
        default=None,
        metadata={
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
    name_style: NameNameStyle = field(
        default=NameNameStyle.WESTERN,
        metadata={
            "name": "name-style",
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
