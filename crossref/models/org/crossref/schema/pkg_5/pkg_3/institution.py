from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution_acronym import (
    InstitutionAcronym,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution_department import (
    InstitutionDepartment,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution_id import (
    InstitutionId,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution_name import (
    InstitutionName,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution_place import (
    InstitutionPlace,
)

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

    institution_name: Optional[InstitutionName] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    institution_id: List[InstitutionId] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "sequence": 1,
        },
    )
    institution_acronym: List[InstitutionAcronym] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        },
    )
    institution_place: List[InstitutionPlace] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        },
    )
    institution_department: List[InstitutionDepartment] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 6,
        },
    )
