from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class ElocationId:
    """
    Article identifier or e-location id of the item.
    """
    class Meta:
        name = "elocation_id"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
