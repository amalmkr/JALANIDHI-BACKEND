def bill_calculator(water_used):
    if water_used <=10:
        amount=100

    elif water_used<=20:
        amount=100+(water_used-10)*20

    elif water_used<=30:
        amount=310+(water_used-20)*50

    else:
        amount=800+(water_used-30)*100

    return amount
    