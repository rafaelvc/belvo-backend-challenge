# from django.test import TestCase
import json
from rest_framework.test import APITestCase
# from django.urls import reverse 
from rest_framework import status

class TestCases(APITestCase):

    user1 = { "name": "Rafael", "email": "verganic@gmail.com", "age": 39 }
    user1_out = {'id': 1, 'name': 'Rafael', 'email': 'verganic@gmail.com', 'age': 39}

    goal1_input = [
        {"reference": "000051", "account": "C00099", "date": "2020-01-03", "amount": -51.13, "type": "outflow", "category": "groceries", "user_id": 1},
        {"reference": "000052", "account": "C00099", "date": "2020-01-10", "amount": 2500.72, "type": "inflow", "category": "salary", "user_id": 1},
        {"reference": "000053", "account": "C00099", "date": "2020-01-10", "amount": -150.72, "type": "outflow", "category": "transfer", "user_id": 1},
        {"reference": "000054", "account": "C00099", "date": "2020-01-13", "amount": -560.00, "type": "outflow", "category": "rent", "user_id": 1},
        {"reference": "000689", "account": "S00012", "date": "2020-01-10", "amount": 150.72, "type": "inflow", "category": "savings" ,"user_id":1}]

    goal1_output = [
            {'account': 'C00099', 'balance': 1738.87, 'total_inflow': 2500.72, 'total_outflow': -761.85},
            { 'account': 'S00012', 'balance': 150.72, 'total_inflow': 150.72, 'total_outflow': 0} ]

    goal2_output = {"inflow": {"salary": 2500.72, "savings": 150.72}, "outflow": {"groceries": -51.13, "rent": -560.00, "transfer": -150.72}}

    def add_user1(self):
        response = self.client.post('/users/', data=json.dumps(TestCases.user1), content_type='application/json')
        self.assertEquals(response.data, TestCases.user1_out)

    def add_user1_trans(self):
        response = self.client.post('/usertransadd/', data=json.dumps(TestCases.goal1_input), content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
 
    def test_goal1(self):
        self.add_user1()
        self.add_user1_trans()
        response = self.client.get('/userbalance/?user_id=1')
        self.assertEquals(response.data, TestCases.goal1_output)

    def test_goal1_for_date_ranges(self):
        pass

    def test_goal2(self):
        self.add_user1()
        self.add_user1_trans()
        response = self.client.get('/userbalancebycategory/?user_id=1')
        self.assertEquals(response.data, TestCases.goal2_output)

    def test_inflow_negative(self):
        inflow_negative = [{"reference": "000088", "account": "C00099", "date": "2020-01-03", "amount": "-51.13", "type": "inflow", "category": "groceries", "user_id": 1}]
        expected = "[{\'non_field_errors\': [ErrorDetail(string=\'Inflow transaction 000088 must be positive.\', code=\'invalid\')]}]"
        self.add_user1()
        response = self.client.post('/usertransadd/', data=json.dumps(inflow_negative), content_type='application/json')
        self.assertEquals(str(response.data), expected)
 
    def test_outflow_positive(self):
        outflow_positive = [{"reference": "000088", "account": "C00099", "date": "2020-01-03", "amount": "51.13", "type": "outflow", "category": "groceries", "user_id": 1}]
        expected = "[{\'non_field_errors\': [ErrorDetail(string=\'Outflow transaction 000088 must be negative.\', code=\'invalid\')]}]"
        self.add_user1()
        response = self.client.post('/usertransadd/', data=json.dumps(outflow_positive), content_type='application/json')
        self.assertEquals(str(response.data), expected)

    def test_wrong_transtype(self):
        wrong_type = [{"reference": "000088", "account": "C00099", "date": "2020-01-03", "amount": "51.13", "type": "noflow", "category": "groceries", "user_id": 1}]
        expected = "[{\'non_field_errors\': [ErrorDetail(string=\'Invalid type of transaction for (000088). Type was (noflow) and it must be inflow or outflow.\', code=\'invalid\')]}]"
        self.add_user1()
        response = self.client.post('/usertransadd/', data=json.dumps(wrong_type), content_type='application/json')
        self.assertEquals(str(response.data), expected)


    def test_duplicated_trans(self):
        # trans1 = [{"reference": "000088", "account": "C00099", "date": "2020-01-03", "amount": "51.13", "type": "intflow", "category": "groceries", "user_id": 1}]
        # self.add_user1()
        # response = self.client.post('/usertransadd/', data=json.dumps(trans1), content_type='application/json')
        # self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        pass
