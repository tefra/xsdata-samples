from ubl.models.common.ubl_common_aggregate_components_2_1 import Consignment
from ubl.models.common.ubl_common_aggregate_components_2_1 import TransportExecutionPlanDocumentReference
from ubl.models.common.ubl_common_basic_components_2_1 import Id
from ubl.models.common.ubl_common_basic_components_2_1 import TransportationStatusTypeCode
from ubl.models.common.ubl_common_basic_components_2_1 import UblversionId
from ubl.models.maindoc.ubl_transportation_status_request_2_1 import TransportationStatusRequest
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlTime


obj = TransportationStatusRequest(
    ublversion_id=UblversionId(
        value="2.1"
    ),
    id=Id(
        value="TSR_1"
    ),
    issue_date=XmlDate(2011, 10, 6),
    issue_time=XmlTime(9, 29, 10, 0, 60),
    transportation_status_type_code=TransportationStatusTypeCode(
        value="All deviations"
    ),
    transport_execution_plan_document_reference=TransportExecutionPlanDocumentReference(
        id=Id(
            value="TEP_1"
        )
    ),
    consignment=[
        Consignment(
            id=Id(
                value="CON_1"
            )
        ),
    ]
)
