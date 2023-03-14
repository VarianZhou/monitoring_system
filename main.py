from Monitor import Monitor
from Sensor import Sensor, Motor_Sensor
from Actuator import Actuator, Motor_Actuator
from Criteria import Motor_Criteria
from Task import Task


# In this class we provide an example of how to use this program

# The main function class
def main():
    # initialize the monitor system
    monitor = Monitor()
    # We initialize a list of sensors
    msg1 = '''1. Please remove the tap of the machine using a screw driver,
              2. Please remove the motor on the left hand side,
              3. Please replace it with a new motor,
              4. Put the tap back,
              5. Try to restart the machine.'''
    msg2 = '''1. Please remove the tap of the machine using a screw driver,
              2. Please remove the motor on the right hand side,
              3. Please replace it with a new motor,
              4. Put the tap back,
              5. Try to restart the machine.'''
    motor_sensor1 = Motor_Sensor('Motor Sensor 1', msg1, int)
    motor_sensor2 = Motor_Sensor('Motor Sensor 2', msg2, int)

    motor_actuator1 = Motor_Actuator('Motor Actuator 1')
    motor_actuator2 = Motor_Actuator('Motor Actuator 2')

    # We define the sensor and task lists
    sensors = [motor_sensor1, motor_sensor2]
    actuators = [motor_actuator1, motor_actuator2]
    parameters1 = [180,180]
    parameters2 = [150,100]

    # Now define the criterias
    criteria1 = Motor_Criteria((170,190))
    criteria2 = Motor_Criteria((170,190))
    criteria3 = Motor_Criteria((140,160))
    criteria4 = Motor_Criteria((90,110))
    c1 = [criteria1,criteria2]
    c2 = [criteria3,criteria4]

    # Now we define the tasks
    task1 = Task(sensors,actuators,parameters1,c1)
    task2 = Task(sensors,actuators,parameters2,c2)

    # We initialize a sequence of tasks
    monitor.add_task(task1)
    monitor.add_task(task2)

    # This task should be successful
    monitor.monitor_next_task()
    # This one should fail
    monitor.monitor_next_task()
main()