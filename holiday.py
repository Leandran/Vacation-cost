def HotelCost(nights):
    RoomCost = 2500 * int(nights)
    return RoomCost

print(HotelCost(3))


HotelCost(10)


def PlaneCost(city):

    if city == 'Capetown':
        Ticketprice = 1000
        return Ticketprice

    elif city == 'Durban':
        Ticketprice = 700
        return Ticketprice

    elif city == 'Jhb':
        Ticketprice = 500
        return Ticketprice
            



print(PlaneCost('Capetown'))




def CarRental(days):
    Carcost = 400 * int(days)
    return Carcost


print(CarRental(2))



#solution was to replace the all the print functions with the return function, therefor being able to calculate the total cost


def HolidayCost(nights,city,days):
    total = HotelCost(nights) + PlaneCost(city) + CarRental(days)
    print(total)

HolidayCost(5,'Jhb',5)

    
    
  








