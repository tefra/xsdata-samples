from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class GroupTitle:
    """Posted content may be organzed into groupings within a given publisher.

    This element provides for naming the group. It is expected that
    publishers will have a small number of groups each of which reflect
    a topic or subject area.
    """

    class Meta:
        name = "group_title"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 1024,
        },
    )
