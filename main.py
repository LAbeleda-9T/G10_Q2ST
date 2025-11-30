from pyscript import document, display

def Badminton(event):
    badminton = {
        'Name': 'Badminton Club',
        'Description': 'A club for students who enjoy badminton and want to improve their skills.',
        'Meeting Time': 'Every Wednesday at 1:30 PM',
        'Location': 'Sports Hall',
        'Club Moderator': 'Mr. Velasquez',
        'Number of Members': 13
    }

    document.getElementById("output").innerHTML = ""
    display(
        f"{badminton['Name']}\n"
        f"{badminton['Description']}\n"
        f"Meeting Time: {badminton['Meeting Time']}\n"
        f"Location: {badminton['Location']}\n"
        f"Club Moderator: {badminton['Club Moderator']}\n"
        f"Number of Members: {badminton['Number of Members']}",
        target="output"
    )

def Volleyball(event):
    volleyball = {
        'Name': 'Volleyball Club',
        'Description': 'A club for players who want to train, compete, and improve volleyball skills.',
        'Meeting Time': 'Every Tuesday  at 3:0 PM',
        'Location': 'Main Gym/Court',
        'Club Moderator': 'Coach Reyes',
        'Number of Members': 24
    }

    document.getElementById("output").innerHTML = ""
    display(
        f"{volleyball['Name']}\n"
        f"{volleyball['Description']}\n"
        f"Meeting Time: {volleyball['Meeting Time']}\n"
        f"Location: {volleyball['Location']}\n"
        f"Club Moderator: {volleyball['Club Moderator']}\n"
        f"Number of Members: {volleyball['Number of Members']}",
        target="output"
    )

def Basketball(event):
    basketball = {
        'Name': 'Basketball Club',
        'Description': 'A club for students who enjoy basketball and want to improve strategy and teamwork.',
        'Meeting Time': 'Every Monday & Friday at 4:00 PM',
        'Location': 'Covered Court',
        'Club Moderator': 'Coach Ramirez',
        'Number of Members': 28
    }

    document.getElementById("output").innerHTML = ""
    display(
        f"{basketball['Name']}\n"
        f"{basketball['Description']}\n"
        f"Meeting Time: {basketball['Meeting Time']}\n"
        f"Location: {basketball['Location']}\n"
        f"Club Moderator: {basketball['Club Moderator']}\n"
        f"Number of Members: {basketball['Number of Members']}",
        target="output"
    )
