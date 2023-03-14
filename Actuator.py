
'''The Actuator class is a real HW device that could perform a particular task, e.g. like motor rotating for a certain degree.'''

class Actuator():
    def __init__(self,name:str):
        self.name = name
        pass
    '''This method sends activation signal to the actuator to request proceeding, return True when the execution is done.'''
    def execute(self, *args):
        # To be implemented by the particular actuator type
        return True

# Here we define the most likly used actuator in our project
class Motor_Actuator(Actuator):
    '''
    @angle The rotatory angle expected '''
    def execute(self, angle):
        # The procudures to rotate the motor
        return True


