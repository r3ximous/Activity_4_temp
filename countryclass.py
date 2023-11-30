class Country:
    def __init__(self, country_name, enviroment, economy, culture, healthcare, education):
        self.__country_name = country_name
        self.__enviroment = enviroment
        self.__economy = economy
        self.__culture = culture
        self.__healthcare = healthcare
        self.__education = education
    
    def getCountry_name(self):
        return self.__country_name
    
    def setCountry_name(self, country_name):
        self.__country_name = country_name

    def getenviroment(self):
        return self.__enviroment
    
    def setEnviroment(self, enviroment):
        self.__country_name = enviroment

    def getEconomy(self):
        return self.__economy
    
    def setEconomy(self, economy):
        self.__country_name = economy

    def getCulture(self):
        return self.__culture
    
    def setCulture(self, culture):
        self.__country_name = culture

    def getHealthcare(self):
        return self.__healthcare
    
    def setHealthcare(self, healthcare):
        self.__country_name = healthcare

    def getEducation(self):
        return self.__education
    
    def setEducation(self, education):
        self.__country_name = education

class HappinessMeter:
    def __init__(self):
        """
        Initialize HappinessMeter object with an empty list of countries.
        """
        self.countries = []

    def addCountry(self, country):
        """
        Add a country to the HappinessMeter.

        """
        self.countries.append(country)

    def measure_happiness(self):
        """
        Measuring the happiness of each country based on factors in the Country class.

        Returns:
        Tuples containing country name and each of ther happiness scores
        """
        happiness_scores = []

        for country in self.countries:
            happiness_score = (
                country.getEnvironment()
                + country.getEconomy()
                + country.getCulture()
                + country.getHealthcare()
                + country.getEducation()
            )

            happiness_scores.append((country.getCountryName(), happiness_score))

        return happiness_scores


def main():
    # Create an instance of the HappinessMeter class
    happiness_meter = HappinessMeter()

    # Prompt the user to enter the number of countries they want to assess
    num_countries = int(input("Enter the number of countries you want to assess: "))

    # Collect data for each country and add them to the HappinessMeter
    for _ in range(num_countries):
        country_name = input("Enter the name of the country: ")
        environment = int(input("Enter the environmental factor (1-10): "))
        economy = int(input("Enter the economic factor (1-10): "))
        culture = int(input("Enter the cultural factor (1-10): "))
        healthcare = int(input("Enter the healthcare factor (1-10): "))
        education = int(input("Enter the educational factor (1-10): "))

        # Create an instance of the Country class with user provided data for parameters
        country = Country(country_name, environment, economy, culture, healthcare, education)

        # Add country to the HappinessMeter
        happiness_meter.addCountry(country)

    # Measure the happiness and print the results
    happiness_scores = happiness_meter.measure_happiness()
    for country, score in happiness_scores:
        print(f"{country}: {score}")


# Call the main function
if __name__ == "__main__":
    main()

