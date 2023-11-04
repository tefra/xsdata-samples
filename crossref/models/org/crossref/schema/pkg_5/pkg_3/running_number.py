from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class RunningNumber:
    """
    Running numbers to specify the various reports (ex: RC1 to RC4)
    """
    class Meta:
        name = "running_number"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
