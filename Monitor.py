'''
The Monitor function is
'''
from Task import Task
from Sensor import Sensor
from Criteria import Criteria
from queue import *

class Monitor():

    '''
    We start with a monitor, with the sensors and their criterias defined.
    '''

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.tasks = SimpleQueue()
            cls.tolerance = 3
        return cls._instance

    # 我们可以把criteria本身作为sensor的一个attribute或者function
    '''Add a task to the queue'''
    def add_task(self, task):
        self._instance.tasks.put(task)

    '''Monitor the process of the task at the head of the queue'''
    def monitor_next_task(self):
        # get the first task in the queue
        task = self._instance.tasks.get()
        while True:
            # in case of failure
            if not self.execute_next_process(task):
                break
            # accrue the pointer of the task
            if task.accrue_pointer():
                break

    def execute_next_process(self,task):
        for i in range(self.tolerance):
            task.execute_next()
            criteria = task.send_criteria()
            state = task.report_state()
            # in case of success
            if self.check_criteria_meet(criteria, state):
                return True
        device = task.report_fault_device()
        device.print_instruction()
        # in case of fail for three times
        return False


    def num_of_left_tasks(self):
        return self._instance.tasks.qsize()

    # check if the criteria is met by the feedback from a sensor
    def check_criteria_meet(self,criteria : Criteria, data):
        return criteria.success(data)

# 问题1：如何解决同一个sensor在不同情况下需要使用不同的criteria的问题
# 可以把criteria跟task绑定在一起，criteria取决于task

# 问题2：假设现在机器给出了一项折叠任务，我们想要逐步监视整个折叠的流程，如何监视这一流程呢？
# 我的设计是把Task作为一个单独的class，每一项task都对应着一次折叠的任务。每个task都有自己的一套流程，我们要让task向monitor实时汇报每一步完成
# 的情况。这样设计我们就需要Monitor去干预整个task的流程和行动。所以不如直接把Monitor跟sensor系统整合到一起，