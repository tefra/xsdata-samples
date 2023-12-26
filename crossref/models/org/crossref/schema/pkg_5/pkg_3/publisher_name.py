from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class PublisherName:
    """The name of the publisher of a book or conference proceedings.

    This name may differ from that of the organization registering or
    maintaining the metadata record.
    """

    class Meta:
        name = "publisher_name"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
        },
    )
