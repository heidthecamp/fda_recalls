# {
#             "country": "United States",
#             "city": "New York",
#             "address_1": "950 3rd Avenue, 21st Floor",
#             "reason_for_recall": "Recalled whey powder was used in further production of numerous food products.",
#             "address_2": "",
#             "product_quantity": "216 Cases (10 x 1.lb. pouches per case)",
#             "code_info": "2280703   Best By 4/3/2019",
#             "center_classification_date": "20180813",
#             "distribution_pattern": "CA, CO, UT, WA, GA, TX",
#             "state": "NY",
#             "product_description": "Homestyle Italian Seasoned Croutons:  1 lb. foil pouch  Item # 74384              Sugar Foods Corporation  6190 E. Slauson Ave.  Los Angeles, CA 90047",
#             "report_date": "20180808",
#             "classification": "Class II",
#             "openfda": {},
#             "recalling_firm": "Sugar Foods Corporation Inc",
#             "recall_number": "F-1804-2018",
#             "initial_firm_notification": "Telephone",
#             "product_type": "Food",
#             "event_id": "80580",
#             "termination_date": "20180918",
#             "recall_initiation_date": "20180720",
#             "postal_code": "10022",
#             "voluntary_mandated": "Voluntary: Firm initiated",
#             "status": "Terminated"
#         }

class FDA_Recall:
    def __init__(self, country, city, address_1, reason_for_recall, address_2, product_quantity, code_info, center_classification_date, distribution_pattern, state, product_description, report_date, classification, openfda, recalling_firm, recall_number, initial_firm_notification, product_type, event_id, termination_date, recall_initiation_date, postal_code, voluntary_mandated, status):
        self.country = country
        self.city = city
        self.address_1 = address_1
        self.reason_for_recall = reason_for_recall
        self.address_2 = address_2
        self.product_quantity = product_quantity
        self.code_info = code_info
        self.center_classification_date = center_classification_date
        self.distribution_pattern = distribution_pattern
        self.state = state
        self.product_description = product_description
        self.report_date = report_date
        self.classification = classification
        self.openfda = openfda
        self.recalling_firm = recalling_firm
        self.recall_number = recall_number
        self.initial_firm_notification = initial_firm_notification
        self.product_type = product_type
        self.event_id = event_id
        self.termination_date = termination_date
        self.recall_initiation_date = recall_initiation_date
        self.postal_code = postal_code
        self.voluntary_mandated = voluntary_mandated
        self.status = status

    def __init__(self, data):
        self.country = data['country']
        self.city = data['city']
        self.address_1 = data['address_1']
        self.reason_for_recall = data['reason_for_recall']
        self.address_2 = data['address_2']
        self.product_quantity = data['product_quantity']
        self.code_info = data['code_info']
        self.center_classification_date = data['center_classification_date']
        self.distribution_pattern = data['distribution_pattern']
        self.state = data['state']
        self.product_description = data['product_description']
        self.report_date = data['report_date']
        self.classification = data['classification']
        self.openfda = data['openfda']
        self.recalling_firm = data['recalling_firm']
        self.recall_number = data['recall_number']
        self.initial_firm_notification = data['initial_firm_notification']
        self.product_type = data['product_type']
        self.event_id = data['event_id']
        self.termination_date = data['termination_date']
        self.recall_initiation_date = data['recall_initiation_date']
        self.postal_code = data['postal_code']
        self.voluntary_mandated = data['voluntary_mandated']
        self.status = data['status']

    def get_country(self):
        return self.country
    
    def get_city(self):
        return self.city
    
    def get_reason_for_recall(self):
        return self.reason_for_recall
    
    def get_state(self):
        return self.state
    
    def get_product_description(self):
        return self.product_description
    
    def get_classification(self):
        return self.classification
    
    def get_product_type(self):
        return self.product_type
    
    def get_voluntary_mandated(self):
        return self.voluntary_mandated
    
    def get_termination_date(self):
        return self.termination_date
    
    def get_recall_initiation_date(self):
        return self.recall_initiation_date
    

