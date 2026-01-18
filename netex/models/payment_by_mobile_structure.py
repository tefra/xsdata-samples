from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PaymentByMobileStructure:
    phone_number_to_pay: str | None = field(
        default=None,
        metadata={
            "name": "PhoneNumberToPay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    support_phone_number: str | None = field(
        default=None,
        metadata={
            "name": "SupportPhoneNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_url: str | None = field(
        default=None,
        metadata={
            "name": "PaymentUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_app_download_url: str | None = field(
        default=None,
        metadata={
            "name": "PaymentAppDownloadUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
