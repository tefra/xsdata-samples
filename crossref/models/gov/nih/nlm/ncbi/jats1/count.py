from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class Count:
    """
    <div> <h3>Count</h3> </div>.
    """

    class Meta:
        name = "count"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    count: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    count_type: str | None = field(
        default=None,
        metadata={
            "name": "count-type",
            "type": "Attribute",
            "required": True,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
