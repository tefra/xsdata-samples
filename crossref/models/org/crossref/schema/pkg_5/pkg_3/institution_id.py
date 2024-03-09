from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.institution_id_type import (
    InstitutionIdType,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class InstitutionId:
    """Identifier for an institution or organization (currently supported: ROR,
    ISNI, Wikidata).

    Identifiers must be included as a URI
    """

    class Meta:
        name = "institution_id"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[hH][tT][tT][pP][sS]://.{1,50}",
        },
    )
    type_value: Optional[InstitutionIdType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
