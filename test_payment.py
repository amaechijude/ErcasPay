import unittest
import unittest.mock
from ercaspay import Ercaspay

class TestErcaspayInitiateTransaction(unittest.TestCase):
    def setUp(self):
        self.ercaspay = Ercaspay("test_secret_key")

    def test_usd_initiate_transaction_successful(self):
        mock_response = {
            "requestSuccessful": True,
            "responseCode": "00",
            "responseBody": {
                "paymentReference": "TEST_REF_123",
                "transactionReference": "ERCS_TX_123",
                "checkoutUrl": "https://checkout.ercaspay.com/123"
            }
        }
        
        with unittest.mock.patch('requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = mock_response
            
            result = self.ercaspay.usd_initiate_transaction(
                amount=100.00,
                payment_reference="TEST_REF_123",
                customer_name="John Doe",
                customer_email="john@example.com"
            )
            
            self.assertTrue(result["tx_status"])
            self.assertEqual(result["tx_code"], "00")
            self.assertEqual(result["tx_body"]["payment_reference"], "TEST_REF_123")
            self.assertEqual(result["tx_body"]["tx_reference"], "ERCS_TX_123")
            self.assertEqual(result["tx_body"]["checkoutUrl"], "https://checkout.ercaspay.com/123")
            
            mock_post.assert_called_once()
            _, kwargs = mock_post.call_args
            self.assertEqual(kwargs["json"]["currency"], "USD")

            def test_usd_initiate_transaction_invalid_amount(self):
                with self.assertRaises(ValueError) as context:
                    self.ercaspay.usd_initiate_transaction(
                        amount=-10.00,
                        payment_reference="TEST_REF_123",
                        customer_name="John Doe",
                        customer_email="john@example.com"
                    )
                
                self.assertEqual(str(context.exception), "Amount must be a positive float")
            
                with self.assertRaises(ValueError) as context:
                    self.ercaspay.usd_initiate_transaction(
                        amount="invalid",
                        payment_reference="TEST_REF_123",
                        customer_name="John Doe",
                        customer_email="john@example.com"
                    )
                
                self.assertEqual(str(context.exception), "Amount must be a positive float")

class TestErcaspayVerification(unittest.TestCase):
    def setUp(self):
        self.ercaspay = Ercaspay("test_secret_key")
    def test_verify_transaction_successful(self):
        mock_response = {
            "requestSuccessful": True,
            "responseCode": "00",
            "responseMessage": "Transaction verified successfully",
            "responseBody": {
                "transactionReference": "ERCS_TX_123",
                "paymentReference": "TEST_REF_123",
                "amount": 100.00,
                "currency": "NGN",
                "status": "successful"
            }
        }
        
        with unittest.mock.patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response
            
            result = self.ercaspay.verify_transaction("ERCS_TX_123")
            
            self.assertTrue(result["tx_status"])
            self.assertEqual(result["tx_code"], "00")
            self.assertEqual(result["tx_message"], "Transaction verified successfully")
            self.assertEqual(result["tx_body"]["transactionReference"], "ERCS_TX_123")
            self.assertEqual(result["tx_body"]["paymentReference"], "TEST_REF_123")
            self.assertEqual(result["tx_body"]["amount"], 100.00)
            self.assertEqual(result["tx_body"]["currency"], "NGN")
            self.assertEqual(result["tx_body"]["status"], "successful")
            
            mock_get.assert_called_once_with(
                f"{self.ercaspay.base_url}/payment/transaction/verify/ERCS_TX_123",
                headers={
                    "Authorization": f"Bearer {self.ercaspay.sk}",
                    "Content-Type": "application/json"
                }
            )



if __name__ == '__main__':
    unittest.main()