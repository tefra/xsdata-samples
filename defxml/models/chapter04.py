from dataclasses import dataclass, field
from typing import Optional
from defxml.models.chapter04cust import CustomerType
from defxml.models.chapter04prod import ItemsType

__NAMESPACE__ = "http://example.org/ord"


@dataclass
class OrderType:
    number: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    customer: Optional[CustomerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    items: Optional[ItemsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Order(OrderType):
    class Meta:
        name = "order"
        namespace = "http://example.org/ord"
