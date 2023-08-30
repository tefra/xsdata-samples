from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class JournalTitle:
    """
    Journal title in a citation.
    """
    class Meta:
        name = "journal_title"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
