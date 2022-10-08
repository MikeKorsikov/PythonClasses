# HW on abstract factory (Helpdesk)

from abc import ABC, abstractmethod
import sys

# *** CLASS SECTION ***
# 1
class Ticket(ABC):
    @abstractmethod
    def info(self): pass


# 2
class IncidentTicket(Ticket):  # [1] to be used by both Jira and ServiceNow factories
    def info(self):
        self.ID = id(self)
        message = "{name} number {ID} was created." \
                  "".format(name=self.__class__.__name__, ID=self.ID)
        return message


# 3a
class ProblemTicket(Ticket):  # [1] to be used by Jira factory
    def info(self):
        self.ID = id(self)
        message = "{name} number {ID} was created." \
                  "".format(name=self.__class__.__name__, ID=self.ID)
        return message


# 3b
class ChangeRequestTicket(Ticket):  # [1] to be used by ServiceNow factory
    def info(self):
        self.ID = id(self)
        message = "{name} number {ID} was created." \
                  "".format(name=self.__class__.__name__, ID=self.ID)
        return message


# 4 interface, abstract base class
class AbstractFactory(ABC):  # to be used by both Jira and ServiceNow factories
    @abstractmethod
    def create_ticket(self, issue_type):
        pass


# 5 concrete factory
class JiraFactory(AbstractFactory):  # [4]
    def create_ticket(self, issue_type):
        if issue_type == 'incident':
            return IncidentTicket()  # [2]
        if issue_type == 'problem':
            return ProblemTicket()  # [3a]


# 6 concrete factory
class SnowFactory(AbstractFactory):  # [4]
    def create_ticket(self, issue_type):
        if issue_type == 'incident':
            return IncidentTicket()  # [2]
        if issue_type == 'change':
            return ChangeRequestTicket()  # [3b]


# 7 support class to create individual factory based on type of system
class FactoryProducer:
    def get_factory(self, system_type):
        if system_type == 'jira':
            return JiraFactory()  # [5]
        if system_type == 'snow':
            return SnowFactory()  # [6]


# *** MENU SECTION ***
producer = FactoryProducer()


def menu():
    print('\nChatbot: In which system do you work?'
          '\n\t [1] ServiceNow'
          '\n\t [2] Jira')
    system_selected = int(input('\nUser: '))
    if system_selected == 1:
        servicenow()
    elif system_selected == 2:
        jira()
    else:
        print('Chatbot: Please only select only [1] or [2].')
        menu()


def servicenow():
    snow_factory = producer.get_factory('snow')
    print('\nChatbot: What type of ticket would you like to raise in ServiceNow?'
          '\n\t [1] Incident'
          '\n\t [2] Change request')
    ticket_selected = int(input('\nUser: '))

    if ticket_selected == 1:
        snow_incident = snow_factory.create_ticket('incident')
        print(snow_incident.info())
        goon()

    elif ticket_selected == 2:
        snow_change = snow_factory.create_ticket('change')
        print(snow_change.info())
        goon()

    else:
        print('Chatbot: Please only select either [1] or [2].')
        servicenow()


def jira():
    jira_factory = producer.get_factory('jira')
    print('\nChatbot: What type of ticket would you like to raise in Jira?'
          '\n\t [1] Incident'
          '\n\t [2] Problem')
    ticket_selected = int(input('\nUser: '))
    if ticket_selected == 1:
        jira_incident = jira_factory.create_ticket('incident')
        print(jira_incident.info())
        goon()

    elif ticket_selected == 2:
        jira_problem = jira_factory.create_ticket('problem')
        print(jira_problem.info())
        goon()

    else:
        print('Chatbot: Please only select either [1] or [2].')
        jira()

def goon():
    print("Chatbot: Do you want to continue? [Y/N]")
    option = str(input("\nUser: "))
    if option.lower() == 'y':
        menu()
    elif option.lower() == 'n':
        print('Thank you for using our service.')
        sys.exit()
    else:
        print('Please choose either [y] or [n].')
        goon()

# invoke menu
menu()
