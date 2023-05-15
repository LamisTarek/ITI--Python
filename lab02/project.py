import datetime
import json
import uuid

def project_title():
    str=input("Title: ")
    if str !="" and str.isalpha():
        return str
    else:
        print("title is required")
        return project_title()
    
def project_details():
    str=input("Details: ")
    if str !="" :
        return str
    else:
        print("Details is required")
        return project_details()

def project_total_target():
    value=input("Target: ")
    if value !="" and value.isdigit() and value!=0 :
        return value
    else:
        print("Total target is required")
        return project_total_target()
    
def project_date():
    value=input("Date in '%Y-%m-%d': ")
    date_format = '%Y-%m-%d'
    try:
        dateObject = datetime.datetime.strptime(value, date_format)
        return value
    except ValueError:
        return project_date()

def save_data(project):
    with open('project.json', 'r') as file:
        projects = json.load(file)
    projects.append(project)
    with open('project.json', 'w') as file:
        json.dump(projects,file)
    
def create_project(id, project_id):
    title = project_title()
    details = project_details()
    total_target = project_total_target()
    start_date= project_date()
    end_date= project_date()
    user_id=id    
    project={
        'tilte': title,
        'details': details,
        'total_target': total_target,
        'start_date': start_date,
        'end_date': end_date,
        'project_id': str(project_id),
        'user_id':str(id)
    }
    print("Successfully insterted")
    save_data(project)

def view_project():
    with open("project.json", "r") as f:
            data = json.load(f)
    for key in data:
            for value in key:
                print(value,":", key[value])
                print("-------------------")

def edit_project(user, project_id):
    title = project_title()
    details = project_details()
    total_target = project_total_target()
    start_date= project_date()
    end_date= project_date()
    with open("project.json", "r") as f:
            data = json.load(f)
    for project in data:
        print(project)
        if project["user_id"] != str(user) and project["project_id"] != str(project_id):
            print("Error: You cannot edit projects created by other users.")
            return
        if title:
            project["title"] = title
        if details:
            project["details"] = details
        if total_target:
            project["total_target"] = total_target
        if start_date:
            project["start_date"] = start_date.isoformat()
        if end_date:
            project["end_date"] = end_date.isoformat()

    with open("projects.json", "w") as f:
        json.dump(data, f)
    print("Project edited successfully.")
    
# def delete_project():
    


def project_menue(id):
    while True:
        print("\n1- Create Project\n2- View Project\n3- Edit Project\n4- Delete Project")
        choice = int(input("Enter your choice: "))
        project_id=uuid.uuid4()
        if choice == 1:
            create_project(id, project_id)
        elif choice == 2:
            view_project()
        elif choice == 3:
          
           edit_project(id, project_id)
        elif choice == 4:
            delete_project()
        else:
            print("Invalid choice, Please try again")