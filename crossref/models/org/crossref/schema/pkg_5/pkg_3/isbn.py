from dataclasses import dataclass, field
from crossref.models.org.crossref.schema.pkg_5.pkg_3.media_type_atts_media_type import MediaTypeAttsMediaType

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Isbn:
    """
    The ISBN assigned to an entity.
    """
    class Meta:
        name = "isbn"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 10,
            "max_length": 17,
            "pattern": r"(97(8|9)-)?\d[\d \-]+[\dX]",
        }
    )
    media_type: MediaTypeAttsMediaType = field(
        default=MediaTypeAttsMediaType.PRINT,
        metadata={
            "type": "Attribute",
        }
    )
