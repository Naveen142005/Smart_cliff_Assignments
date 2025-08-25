def calculate_emi(account, amount, rate, duration):
    rate = (rate / 100) / 12
    duration = duration * 12

    emi = amount * rate * ((1 + rate) ** duration) / ((1 + rate) ** duration - 1)
    return round(emi, 2)