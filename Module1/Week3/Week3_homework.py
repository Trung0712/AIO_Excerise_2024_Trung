# Exercise 1:
import torch
import torch.nn as nn

class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x)
        return exp_x/ sum_exp_x
    
class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        max_x = torch.max(x)
        exp_x = torch.exp(x - max_x)  
        sum_exp_x = torch.sum(exp_x)
        return exp_x / sum_exp_x


# Exercise 2:
class Person:
    def __init__(self, name, yob) -> None:
        self.name = name
        self.yob = yob
    

class Student(Person):
    def __init__(self, name, yob, grade) -> None:
        super().__init__(name, yob)
        self.grade = grade
    
    def describe(self):
        return f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, yob, subject) -> None:
        super().__init__(name, yob)
        self.subject = subject
    
    def describe(self):
        return f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}"

class Doctor(Person):
    def __init__(self, name, yob, specialist) -> None:
        super().__init__(name, yob)
        self.specialist = specialist
    
    def describe(self):
        return f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}"
    
class Ward:
    def __init__(self, name) -> None:
        self.name = name
        self.people = []
    
    def add_person(self, person):
        self.people.append(person)
    
    def describe(self):
        msg = f"Ward: {self.name}\n"
        for person in self.people:
            msg += f"{person.describe()}\n"
        return msg.strip()
    
    def count_doctor(self):
        return sum(1 for person in self.people if isinstance(person, Doctor))
    
    def sort_age(self):
        self.people.sort(key= lambda person: person.yob)
    
    def compute_average(self):
        teachers = []
        for person in self.people:
            if isinstance(person, Teacher):
                teachers.append(person)
        
        return sum(teacher.yob for teacher in teachers)/ len(teachers) if len(teachers) > 0 else None
student1 = Student ( name =" studentZ2023 ", yob =2011 , grade ="6")
assert student1._yob == 2011
student1.describe ()

# Exercise 3:
class Stack:
    def __init__(self, capacity= None):
        self.stack = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        if not self.stack.is_full():
            self.stack.append(item)
        else:
            raise IndexError
    
    def pop(self):
        if not self.stack.is_empty():
            return self.stack.pop()
        else:
            raise IndexError
    
    def top(self):
        if not self.stack.is_empty():
            return self.stack[-1]
        else:
            raise IndexError
    
    def is_full(self):
        if self.capacity is None: # There's no limit
            return False
        return len(self.stack) >= self.capacity # If equal then stack is full
    
# Exercise 4
class Queue:
    def __init__(self, capacity=None):
        self.items = []
        self.capacity = capacity

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.capacity is None:
            return False  # No fixed capacity, queue can never be full in this sense
        else:
            return len(self.items) >= self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.items.insert(0, item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop()

    def size(self):
        return len(self.items)

