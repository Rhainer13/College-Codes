# Rhainer Matheuz P. Mata
# BSIT II-1
# Date: 1-12-2024
# Finals

class Node:
    def __init__(self, job_title, company_name, job_description, required_qualifications):
        self.job_title = job_title
        self.company_name = company_name
        self.job_description = job_description
        self.required_qualifications = required_qualifications
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, job_title=None, company_name=None, job_description=None, required_qualifications=None):
        if job_title is not None and company_name is None and job_description is None and required_qualifications is None:
            if job_applications.top is None:
                node = Node(job_title.job_title, job_title.company_name, job_title.job_description, job_title.required_qualifications)
                job_applications.top = node
            else:
                node = Node(job_title.job_title, job_title.company_name, job_title.job_description, job_title.required_qualifications)
                node.next = job_applications.top
                job_applications.top = node
        elif self.top is None:
            node = Node(job_title, company_name, job_description, required_qualifications)
            self.top = node
        else:
            node = Node(job_title, company_name, job_description, required_qualifications)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return
        
        data_to_return = self.top
        self.top = self.top.next

        return data_to_return

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print(f"Job Title:{self.top.job_title} || Company Name:{self.top.company_name} || Job Description:{self.top.job_description} || Required Qualification:{self.top.required_qualifications}")

    def display(self):
        if self.top is None:
            print("Job application is empty")
        else:
            current = self.top

            while current:
                print(f"Job Title:{current.job_title} || Company Name:{current.company_name} || Job Description:{current.job_description} || Required Qualification:{current.required_qualifications}")
                current = current.next
            print()
    
    # employers can post job openings by providing details such as job title, company name, job description, and required qualifications
    # each job posting should be pushed onto the stack
    def post_job(self, job_title, company_name, job_description, required_qualifications):
        job_posting.push(job_title, company_name, job_description, required_qualifications)

    # job seekers can apply for jobs by submitting their application details
    # applications should be pushed onto a separate stack
    def apply_for_job(self):
        job_applications.push(job_posting.pop())

    # employers can review and process job applications
    # implement a function to pop the top application from the stack of applications
    def process_job_application(self):
        job_applications.pop()

    # job seekers can view the latest job postings without removing any job details
    # display the details of the top job posting on the stack
    def view_latest_job_posting(self):
        job_posting.peek()

    # employers can view the latest job applications without removing any application details
    # display the details of the top application on the stack of applications
    def view_latest_job_application(self):
        job_applications.peek()

    # employers can close a job opening, removing it from the top of the job postings stack
    def close_job_opening(self):
        job_posting.pop()

    # job seekers should be able to check the status of their job applications
    def check_job_application_status(self):
        if job_applications.top is None:
            print("Job application is empty")
        else:
            current = job_applications.top

            while current:
                print(f"Job Title:{current.job_title} || Company Name:{current.company_name} || Job Description:{current.job_description} || Required Qualification:{current.required_qualifications}")
                current = current.next
            print()

job_posting = Stack()
job_applications = Stack()


print("\n--- Post Job ---")
print(">> Start (Job Posting Stack) <<")
job_posting.post_job("Janitor", "AAA", "Mop the floor", "high school graduate")
job_posting.post_job("Mechanic", "BBB", "repair vehicles", "high school graduate")
job_posting.post_job("Cook", "CCC", "cook food", "high school graduate")
job_posting.display()

print(">> Start (Job Application Stack) <<")
job_applications.display()

print("\n--- Apply for Job (Transfer from Job Opening stack to Job application stack)---")
job_posting.apply_for_job()
job_posting.apply_for_job()
job_applications.view_latest_job_application()

print("\n--- View latest job posting (the top of the Job Opening Stack)---")
job_posting.view_latest_job_posting()

print("\n--- View latest job application (the top of the Job Application Stack)---")
job_applications.view_latest_job_application()

print("\n--- Close Job Opening (remove the top of the job opening stack)---")
job_posting.close_job_opening()
job_posting.view_latest_job_posting()

print("\n--- Process Job Application (removes the top of the job application stack)---")
job_applications.process_job_application()

print("\n--- Check Job application status ---")
job_applications.check_job_application_status()

print(">> End (Job Posting Stack) <<")
job_posting.display()

print("\n>> End (Job Application Stack) <<")
job_applications.display()