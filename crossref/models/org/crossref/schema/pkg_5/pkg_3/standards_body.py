from dataclasses import dataclass, field
from typing import Optional

from crossref.models.org.crossref.schema.pkg_5.pkg_3.standards_body_acronym import (
    StandardsBodyAcronym,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.standards_body_name import (
    StandardsBodyName,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class StandardsBody:
    """
    A wrapper for standards body information.
    """

    class Meta:
        name = "standards_body"
        namespace = "http://www.crossref.org/schema/5.3.1"

    standards_body_name: StandardsBodyName | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    standards_body_acronym: StandardsBodyAcronym | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
