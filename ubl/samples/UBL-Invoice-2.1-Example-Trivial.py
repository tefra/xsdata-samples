from decimal import Decimal
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingCustomerParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import AccountingSupplierParty
from ubl.models.common.ubl_common_aggregate_components_2_1 import InvoiceLine
from ubl.models.common.ubl_common_aggregate_components_2_1 import InvoicePeriod
from ubl.models.common.ubl_common_aggregate_components_2_1 import Item
from ubl.models.common.ubl_common_aggregate_components_2_1 import LegalMonetaryTotal
from ubl.models.common.ubl_common_aggregate_components_2_1 import Party
from ubl.models.common.ubl_common_aggregate_components_2_1 import PartyName
from ubl.models.common.ubl_common_basic_components_2_1 import Description
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import LineExtensionAmount
from ubl.models.common.ubl_common_basic_components_2_1 import Name
from ubl.models.common.ubl_common_basic_components_2_1 import PayableAmount
from ubl.models.maindoc.ubl_invoice_2_1 import Invoice
from xsdata.models.datatype import XmlDate


obj = Invoice(
    id=Id(
        value="123"
    ),
    issue_date=XmlDate(2011, 9, 22),
    invoice_period=[
        InvoicePeriod(
            start_date=XmlDate(2011, 8, 1),
            end_date=XmlDate(2011, 8, 31)
        ),
    ],
    accounting_supplier_party=AccountingSupplierParty(
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value="Custom Cotter Pins"
                    )
                ),
            ]
        )
    ),
    accounting_customer_party=AccountingCustomerParty(
        party=Party(
            party_name=[
                PartyName(
                    name=Name(
                        value="North American Veeblefetzer"
                    )
                ),
            ]
        )
    ),
    legal_monetary_total=LegalMonetaryTotal(
        payable_amount=PayableAmount(
            value=Decimal("100.00"),
            currency_id="CAD"
        )
    ),
    invoice_line=[
        InvoiceLine(
            id=Id(
                value="1"
            ),
            line_extension_amount=LineExtensionAmount(
                value=Decimal("100.00"),
                currency_id="CAD"
            ),
            item=Item(
                description=[
                    Description(
                        value="Cotter pin, MIL-SPEC"
                    ),
                ]
            )
        ),
    ]
)
