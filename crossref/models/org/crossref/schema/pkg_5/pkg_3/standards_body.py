from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.org.crossref.schema.pkg_5.pkg_3.standards_body_acronym import (
    StandardsBodyAcronym,
)
from crossref.models.org.crossref.schema.pkg_5.pkg_3.standards_body_name import (
    StandardsBodyName,
)

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class StandardsBody:
    """
    A wrapper for standards body information.
    """

    class Meta:
        name = "standards_body"
        namespace = "http://www.crossref.org/schema/5.3.1"

    standards_body_name: StandardsBodyName = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    standards_body_acronym: StandardsBodyAcronym = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
