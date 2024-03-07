def calculate_daily_pay(successful_delivery_rate):
    base_pay = 5000
    if successful_delivery_rate < 0:
        raise ValueError('Incorrect Input')
    if successful_delivery_rate < 50:
        return successful_delivery_rate * 160 + 5000
    elif successful_delivery_rate < 60:
        return successful_delivery_rate * 200 + 5000
    elif successful_delivery_rate < 70:
        return successful_delivery_rate * 250 + 5000
    elif successful_delivery_rate >= 70:
        return successful_delivery_rate * 500 + 5000

