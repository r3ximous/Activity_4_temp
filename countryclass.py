class Country:
    '''
    this is a class that represents a country
    '''
    def __init__(self, country_name, enviroment, economy, culture, healthcare, education):
        self.__country_name = country_name
        self.__enviroment = enviroment
        self.__economy = economy
        self.__culture = culture
        self.__healthcare = healthcare
        self.__education = education
    
    def getCountryName(self):
        '''
        returns the name of the country
        '''
        return self.__country_name
    
    def setCountryName(self, country_name):
        '''
        sets up the variable of the country name
        '''
        self.__country_name = country_name

    def getEnvironment(self):
        '''
        returns the environment rating of the country
        '''
        return self.__enviroment
    
    def setEnvironment(self, enviroment):
        '''
        sets up the variable of the environment rating
        '''
        self.__country_name = enviroment

    def getEconomy(self):
        '''
        returns the economy rating of the country
        '''
        return self.__economy
    
    def setEconomy(self, economy):
        '''
        sets up the variable of the economy rating
        '''
        self.__country_name = economy

    def getCulture(self):
        '''
        returns the culture rating of the country
        '''
        return self.__culture
    
    def setCulture(self, culture):
        '''
        sets up the variable of the culture rating
        '''
        self.__country_name = culture

    def getHealthcare(self):
        '''
        returns the healthcare rating of the country
        '''
        return self.__healthcare
    
    def setHealthcare(self, healthcare):
        '''
        sets up the variable of the healthcare rating
        '''
        self.__country_name = healthcare

    def getEducation(self):
        '''
        returns the education rating of the country
        '''
        return self.__education
    
    def setEducation(self, education):
        '''
        sets up the variable of the education rating
        '''
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
        Measuring the happiness of each country based on the average factors in the Country class.

        returns a list of tuples with the country name and happiness score.
        """
        happiness_scores = []
        for country in self.countries:
            happiness_score = (country.getCountryName(), (country.getEnvironment() + country.getEconomy() + country.getCulture() + country.getHealthcare() + country.getEducation()) / 5)
            happiness_scores.append(happiness_score)
        return happiness_scores


def main():
    # Create an instance of the HappinessMeter class
    happiness_meter = HappinessMeter()

    # Prompt the user to enter the number of countries they want to assess
    num_countries = int(input("Enter the number of countries you want to assess: "))

    # Collect data for each country and add them to the HappinessMeter
    for _ in range(num_countries):
        country_name = input("\nEnter the name of the country: ")
        environment = int(input("Enter the environmental factor (1-100): "))
        economy = int(input("Enter the economic factor (1-100): "))
        culture = int(input("Enter the cultural factor (1-100): "))
        healthcare = int(input("Enter the healthcare factor (1-100): "))
        education = int(input("Enter the educational factor (1-100): "))

        # Create an instance of the Country class with user provided data for parameters
        country = Country(country_name, environment, economy, culture, healthcare, education)

        # Add country to the HappinessMeter
        happiness_meter.addCountry(country)

    # Measure the happiness by averaging the factors for each country
    happiness_scores = happiness_meter.measure_happiness()

    # Print the happiness scores for each country
    print("\nHappiness scores:")
    for country, score in happiness_scores:
        print(f"{country}: {score}")


# Call the main function
if __name__ == "__main__":
    main()
