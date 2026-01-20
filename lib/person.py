#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    # Sentinel for "not provided"
    _NOT_PROVIDED = object()
    
    def __init__(self, name=_NOT_PROVIDED, job=_NOT_PROVIDED):
        self._name = None
        self._job = None
        
        if name is not Person._NOT_PROVIDED:
            self.name = name
        
        if job is not Person._NOT_PROVIDED:
            self.job = job
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    
    name = property(get_name, set_name)
    
    def get_job(self):
        return self._job
    
    def set_job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
    
    job = property(get_job, set_job)