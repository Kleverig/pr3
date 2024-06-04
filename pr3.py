class Houses:
    pass

class WithLand(Houses):
    def get_house_type(self):
        return "House with land"

class WithoutLand(Houses):
    def get_house_type(self):
        return "House without land"

class ForOneFamily(WithLand):
    def get_house_type(self):
        return "House for one family"

class ForManyFamilies(WithLand):
    def get_house_type(self):
        return "House for many families"

class Villa(ForOneFamily):
    pass

class Townhouse(ForManyFamilies):
    pass

class Apartments(WithoutLand):
    pass

class Villets(Villa):
    pass

villets_instance = Villets()
apartments_instance = Apartments()

villets_message = villets_instance.get_house_type()
apartments_message = apartments_instance.get_house_type()

print(f"Villets: {villets_message}")
print(f"Apartments: {apartments_message}")