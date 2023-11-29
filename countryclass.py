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

