from dataclasses import dataclass, field
from typing import Optional
from crossref.models.org.crossref.schema.pkg_5.pkg_3.mime_type_atts_mime_type import MimeTypeAttsMimeType
from crossref.models.org.crossref.schema.pkg_5.pkg_3.resource_content_version import ResourceContentVersion

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Resource:
    """
    The URI associated with a DOI.
    """
    class Meta:
        name = "resource"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 2048,
            "pattern": r"([hH][tT][tT][pP]|[hH][tT][tT][pP][sS]|[fF][tT][pP])://.*",
        }
    )
    mime_type: Optional[MimeTypeAttsMimeType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content_version: Optional[ResourceContentVersion] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
