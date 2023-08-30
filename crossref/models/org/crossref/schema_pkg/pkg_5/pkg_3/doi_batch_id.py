from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class DoiBatchId:
    """
    Publisher generated ID that uniquely identifies the DOI submission batch.
    """
    class Meta:
        name = "doi_batch_id"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 4,
            "max_length": 100,
        }
    )
