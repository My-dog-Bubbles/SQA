"""
Brief Pytest Template
Example: Username Validator
Use this as a reference for writing your credit_card_validator tests.
"""

import pytest


class Test_Credit_Card_Number:
    """Test suite for credit_card_validator function"""

    # These test are asserted to work with a hypothetical credit_card_validator function.

    #visa card number valid scenarios
    def test_valid_visa_number(self):
        """Test if the vise card number is valid"""
        assert credit_card_validator(4234567891235002) == True

    #mastercard valid scenarios
    def test_valid_mastercard_start_with_51(self):
        """Test if the mastercard card number is valid"""
        assert credit_card_validator(5134567891235000) == True

    def test_valid_mastercard_start_with_53(self):
        """Test if the mastercard card number is valid"""
        assert username_validator(5534567891235006) == True

    def test_valid_mastercard_start_with_2221(self):
        """Test if the mastercard card number is valid"""
        assert username_validator(2221567891235001) == True

    def test_valid_mastercard_start_with_2720(self):
        """Test if the mastercard card number is valid"""
        assert username_validator(2720567891235007) == True

    #American Express valid scenarios
    def test_valid_American_Express_start_with_2720(self):
        """Test if the American Express card number is valid"""
        assert username_validator(342056789125001) == true

    def test_valid_American_Express_start_with_2720(self):
        """Test if the American Express card number is valid"""
        assert username_validator(372056789125004) == True

    # These test are asserted to not work with a hypothetical credit_card_validator function.

    #visa card number invalid scenarios
    def test_invalid_visa_length_long(self):
        """Test if the vise card number will be invalid if its to long"""
        assert credit_card_validator(42345678912350005) == False

    def test_visa_null_value(self):
        """Test if the vise card number will be invalid if its numbers is null"""
        assert credit_card_validator(null) == False

    def test_visa_not_start_with_4(self):
        """Test if the vise card number will be invalid if its numbers does not start with 4"""
        assert credit_card_validator(3213456789123008) == False

    def test_invalid_visa_length_short(self):
        """Test if the vise card number will be invalid if its to short"""
        assert credit_card_validator(423456789123000) == False

    def test_invalid_luhn_number_check(self):
        """Test if the vise card number will pass the luhn check"""
        assert credit_card_validator(4253456789123006) == False

    #mastercard invalid scenarios
    def test_invalid_mastercard_length_long(self):
        """Test if the mastercard card number will be invalid if its to long"""
        assert credit_card_validator(51213456789123007) == False

    def test_mastercard_null_value(self):
        """Test if the mastercard card number will be invalid if its numbers is null"""
        assert credit_card_validator(null) == False

    def test_mastercard_not_start_with_51_55_to_low(self):
        """Test if the mastercard card number will be invalid if its numbers does not start with 51 to 55 its to low"""
        assert credit_card_validator(5033456789123001) == False

    def test_mastercard_not_start_with_51_55_to_high(self):
        """Test if the mastercard card number will be invalid if its numbers does not start with 51 to 55 its to high"""
        assert credit_card_validator(5633456789123005) == False

    def test_mastercard_not_start_with_2221_2720_to_high(self):
        """Test if the mastercard card number will be invalid if its numbers does not start with 2221 to 2720 its to high"""
        assert credit_card_validator(2721456789123005) == False

    def test_mastercard_not_start_with_2221_2720_to_low(self):
        """Test if the mastercard card number will be invalid if its numbers does not start with 2221 to 2720 its to low"""
        assert credit_card_validator(2221456789123000) == False

    def test_invalid_mastercard_length_short(self):
        """Test if the mastercard card number will be invalid if its to short"""
        assert credit_card_validator(513456789123001) == False

    def test_invalid_luhn_number_check(self):
        """Test if the mastercard card number will pass the luhn check"""
        assert credit_card_validator(5133456789123400) == False

    #American Express invalid scenarios
    def test_invalid_American_Express_length_long(self):
        """Test if the American Express card number will be invalid if its to long"""
        assert credit_card_validator(3734567812679004) == False

    def test_American_Express_null_value(self):
        """Test if the American Express card number will be invalid if its numbers is null"""
        assert credit_card_validator(null) == False

    def test_American_Express_not_start_with_34_or_37(self):
        """Test if the American Express card number will be invalid if its numbers does not start with 34"""
        assert credit_card_validator(353456781267007) == False

    def test_invalid_American_Express_length_short(self):
        """Test if the American Express card number will be invalid if its to short"""
        assert credit_card_validator(34156789123007) == False

    def test_invalid_luhn_number_check(self):
        """Test if the American Express card number will pass the luhn check"""
        assert credit_card_validator(341456789123001) == False
