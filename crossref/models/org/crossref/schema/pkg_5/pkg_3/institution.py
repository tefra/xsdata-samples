from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution_id import InstitutionId

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Institution:
    """
    Container element for information about an institution or organization
    associated with an item.
    """
    class Meta:
        name = "institution"
        namespace = "http://www.crossref.org/schema/5.3.1"

    institution_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 1024,
        }
    )
    institution_id: List[InstitutionId] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        }
    )
    institution_acronym: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
            "min_length": 1,
            "max_length": 255,
        }
    )
    institution_place: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
            "min_length": 2,
            "max_length": 255,
        }
    )
    institution_department: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
            "min_length": 2,
            "max_length": 255,
        }
    )
