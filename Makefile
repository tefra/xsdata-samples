dataclass:
	xsdata xsd/travelport/air_v48_0/AirReqRsp.xsd --package samples.travelport.output.air_v48_0
	xsdata xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd --package samples.amadeus.output
	xsdata xsd/amadeus/Fare_MasterPricerTravelBoardSearchReply_15_3_1A.xsd --package samples.amadeus.output
	xsdata xsd/sabre/BargainFinderMaxRQ_v1-9-7.xsd --package samples.sabre.output
	xsdata xsd/sabre/BargainFinderMaxRS_v1-9-7.xsd --package samples.sabre.output

plantuml:
	xsdata xsd/travelport/air_v48_0/AirReqRsp.xsd --package samples.travelport.diagram.air_v48_0 --renderer plantuml
	xsdata xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd --package samples.amadeus.diagram --renderer plantuml
	xsdata xsd/amadeus/Fare_MasterPricerTravelBoardSearchReply_15_3_1A.xsd --package samples.amadeus.diagram --renderer plantuml
	xsdata xsd/sabre/BargainFinderMaxRQ_v1-9-7.xsd --package samples.sabre.diagram --renderer plantuml
	xsdata xsd/sabre/BargainFinderMaxRS_v1-9-7.xsd --package samples.sabre.diagram --renderer plantuml
