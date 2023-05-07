from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.name import Name
from crossref.models.gov.nih.nlm.ncbi.jats1.string_name import StringName

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class NameAlternatives:
    """
    <div> <h3>Name Alternatives</h3> </div>
    """
    class Meta:
        name = "name-alternatives"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    string_name: List[StringName] = field(
        default_factory=list,
        metadata={
            "name": "string-name",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
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
