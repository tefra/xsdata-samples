from dataclasses import dataclass, field
from crossref.models.org.crossref.schema_pkg.pkg_5.pkg_3.isbn_media_type import IsbnMediaType

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
    media_type: IsbnMediaType = field(
        default=IsbnMediaType.PRINT,
        metadata={
            "type": "Attribute",
        }
    )
