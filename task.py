from db import *

class Task:
    
    def __init__(userid, title, description, deadline, priority, effort):
        timestamp = None # this is autogenerated
        ordinality = None 
        pass
        
    def save_to_db():
        """Save this task to the tasks table"""
        pass
        
    def render():
        """Return the HTML rendering of a task with a template"""
        pass
    
    def get_values():
        """Return all the values for insertion into databases
        (taskid, userid, title, description, timestamp, deadline, priority, effort, ordinality, complete)
        """
        pass
