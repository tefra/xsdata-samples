from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class Filter:
    """The filter element is used to disambiguate content in situations where
    multiple publishers share the same host (e.g. when on an aggregated
    platform).

    It should contain a substring of the path that can be used to
    uniquely identify a publisher's or publication's content. For
    instance, using the string "alpsp" here would help the CrossMark
    system distinguish between ALPSP publications on the ingentaconnect
    host and other publications on the same host.
    """
    class Meta:
        name = "filter"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
