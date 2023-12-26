from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ConferenceAcronym:
    """The popularly known as or jargon name (e.g. SIGGRAPH for "Special Interest
    Group on Computer Graphics").

    Authors commonly cite the conference acronym rather than the full
    conference or proceedings name, so it is best to include this
    element when it is available.
    """

    class Meta:
        name = "conference_acronym"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 127,
        },
    )
