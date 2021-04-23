"""
In check-writing systems, it’s crucial to prevent alteration of check amounts.
One common security method requires that the amount be written in numbers AND
spelled out in words as well. 
Even if someone can alter the numerical amount of the check, it’s tough to change the amount in words. 
Create a dictionary that maps numbers to their corresponding word equivalents.
Write a script that inputs a numeric check amount that’s less than 1000 AND
uses the dictionary to write the word equivalent of the amount. 
For example, the amount 112.43 should be written as
ONE HUNDRED TWELVE AND 43/100
"""


digits_in_words = {
    "1": "ONE", "2": "TWO", "3": "THREE", "4": "FOUR",
    "5": "FIVE", "6": "SIX", "7": "SEVEN", "8": "EIGHT",
    "9": "NINE"
    }

ten_to_nineteen_in_words = {
    "10": "TEN", "11": "ELEVEN", "12": "TWELVE", "13": "THIRTEEN", "14": "FOURTEEN",
    "15": "FIFTEEN", "16": "SIXTEEN", "17": "SEVENTEEN", "18": "EIGHTEEN", "19": "NINETEEN"
    }

ten_to_ninety_in_words = {
    "10": "TEN", "20": "TWENTY", "30": "THIRTY", "40": "FORTY", "50": "FIFTY",
    "60": "SIXTY", "70": "SEVENTY", "80": "EIGHTY", "90": "NINETY"
    }


def write_out_hundreds(amount):
    """
    Input: Money amount less than 1000 as a string with optional fractional part 
    Returns: Empty string if less than 100, else like "ONE HUNDRED"
    """
    # Cast str type just in case
    amount = str(amount)

    if float(amount) < 100:
        return ""
    return f"{digits_in_words[amount[0]]} HUNDRED "


def write_out_tens(amount):
    """
    Input: Money amount less than 1000 as a string with optional fractional part 
    Returns:    1) Empty string if no tens
                2) Eleven to Nineteen as special cases 
                3) Else like "FIFTY"
    """
    # Cast str type just in case
    amount = str(amount)
    tens_place = int(float(amount)) % 100

    # If there are no tens in the amount
    if tens_place < 10:
        return ""
    elif tens_place == 10:
        return "TEN "
    elif tens_place <= 19:
        return f"{ten_to_nineteen_in_words[str(tens_place)]} "
    else:
        return f"{ten_to_ninety_in_words[str(tens_place // 10 * 10)]} "


def write_out_ones(amount):
    """
    Input: Money amount less than 1000 as a string  ith optional fractional part 
    Returns:    1) Empty string if no ones
                2) Empty string if eleven to nineteen special cases 
                3) Else like "FIVE"
    """
    # Cast str type just in case
    amount = str(amount)
    
    has_ten_through_nineteen = (10 <= int(float(amount)) % 100 <= 19)

    if has_ten_through_nineteen:
        return ""
    ones_place = str(int(float(amount)) % 10)
    return f"{digits_in_words[ones_place]} "
    

def write_out_fractions(amount):
    """
    Input: Money amount less than 1000 as a string with optional fractional part 
    Returns: Empty string if no fraction, else " AND {fraction}/100"
    """
    # Cast str type just in case
    amount = str(amount)

    # If there is no "." in amount

    if "." not in amount:
        return ""
    else:
        return f"AND {amount[amount.index('.') + 1:]}/100"


money_amount_numerical = input("Enter a money amount < 1'000: ")
if len(money_amount_numerical) == 0:
    money_amount_numerical = "312.43"
        
while money_amount_numerical != "stop":

    money_amount_in_words = ""

    hundreds_in_words = write_out_hundreds(money_amount_numerical)
    tens_in_words = write_out_tens(money_amount_numerical)
    ones_in_words = write_out_ones(money_amount_numerical)
    fraction_in_words = write_out_fractions(money_amount_numerical)

    money_amount_in_words += (hundreds_in_words + tens_in_words + ones_in_words + fraction_in_words)

    print(money_amount_in_words)
    
    money_amount_numerical = input("Enter a money amount < 1'000: ")
