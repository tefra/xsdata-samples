from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ConferenceTheme:
    """The theme is the slogan or special emphasis of a conference in a
    particular year.

    It differs from the subject of a conference in that the subject is
    stable over the years while the theme may vary from year to year.
    For example, the American Society for Information Science and
    Technology conference theme was "Knowledge: Creation, Organization
    and Use" in 1999 and "Defining Information Architecture" in 2000.
    """
    class Meta:
        name = "conference_theme"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        }
    )
