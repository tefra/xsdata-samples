from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PaymentByMobileStructure:
    phone_number_to_pay: None | str = field(
        default=None,
        metadata={
            "name": "PhoneNumberToPay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    support_phone_number: None | str = field(
        default=None,
        metadata={
            "name": "SupportPhoneNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_url: None | str = field(
        default=None,
        metadata={
            "name": "PaymentUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_app_download_url: None | str = field(
        default=None,
        metadata={
            "name": "PaymentAppDownloadUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
