from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class SeriesNumber:
    """
    The series number within a specific published conference discipline.
    """
    class Meta:
        name = "series_number"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 15,
        }
    )
