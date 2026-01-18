from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.footer_type import FooterType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message/footer"
)


@dataclass(frozen=True)
class Footer(FooterType):
    """
    Footer is used to communicate information such as error and warnings
    after the payload of a message.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message/footer"
        )
