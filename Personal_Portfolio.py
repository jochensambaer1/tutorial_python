# Personal_Portfolio.py

class Project:
    def __init__(self, title, description, technologies):
        self.title = title
        self.description = description
        self.technologies = technologies

class PersonalPortfolio:
    def __init__(self, name, projects):
        self.name = name
        self.projects = projects

    def add_project(self, project):
        self.projects.append(project)

    def display_projects(self):
        print(f"Projects in {self.name}'s portfolio:")
        for project in self.projects:
            print(f"Title: {project.title}")
            print(f"Description: {project.description}")
            print(f"Technologies: {', '.join(project.technologies)}")
            print()

# Create some projects
project1 = Project("Project 1", "Description of Project 1", ["Python", "HTML", "CSS"])
project2 = Project("Project 2", "Description of Project 2", ["JavaScript", "React"])

# Create a personal portfolio
portfolio = PersonalPortfolio("John Doe", [project1, project2])

# Add a new project
project3 = Project("Project 3", "Description of Project 3", ["Java", "Spring"])
portfolio.add_project(project3)

# Display the projects in the portfolio
portfolio.display_projects()
