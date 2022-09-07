from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class PublisherPlace:
    """publisher_place gives the primary city location of the publisher.

    If the city is not a major city, the appropriate country, state, or
    province should be added.
    """
    class Meta:
        name = "publisher_place"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 2,
            "max_length": 255,
        }
    )
