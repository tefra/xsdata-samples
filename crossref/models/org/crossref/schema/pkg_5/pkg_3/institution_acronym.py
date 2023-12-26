from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class InstitutionAcronym:
    """
    The acronym of the institution.
    """

    class Meta:
        name = "institution_acronym"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        },
    )
