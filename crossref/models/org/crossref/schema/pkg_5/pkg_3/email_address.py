from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass
class EmailAddress:
    """
    e-mail address to which batch success and/or error messages are sent.
    """
    class Meta:
        name = "email_address"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 6,
            "max_length": 200,
        }
    )
