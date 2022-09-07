from dataclasses import dataclass, field
from crossref.models.org.crossref.schema.pkg_5.pkg_3.media_type_atts_media_type import MediaTypeAttsMediaType

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Issn:
    """
    The ISSN assigned to the title being registered.
    """
    class Meta:
        name = "issn"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 8,
            "max_length": 9,
            "pattern": r"\d{4}-?\d{3}[\dX]",
        }
    )
    media_type: MediaTypeAttsMediaType = field(
        default=MediaTypeAttsMediaType.PRINT,
        metadata={
            "type": "Attribute",
        }
    )
