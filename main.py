from js import document

# Dictionary of clubs
clubs = {
    "Badminton Club": {
        "Description": "Play and practice badminton, join tournaments.",
        "Meeting Time": "Mondays, 3:00 PM",
        "Location": "Gym 1",
        "Club Moderator": "Mr. Tan",
        "Number of Members": 20
    },
    "Basketball Club": {
        "Description": "Improve basketball skills and teamwork.",
        "Meeting Time": "Wednesdays, 4:00 PM",
        "Location": "Basketball Court",
        "Club Moderator": "Ms. Cruz",
        "Number of Members": 25
    },
    "Volleyball Club": {
        "Description": "Practice volleyball and join school competitions.",
        "Meeting Time": "Fridays, 3:30 PM",
        "Location": "Gym 2",
        "Club Moderator": "Mrs. Reyes",
        "Number of Members": 18
    }
}

# Function to display club info
def showClubInfo(*args):
    selected = document.getElementById("clubDropdown").value
    info_card = document.getElementById("clubInfo")
    
    if selected in clubs:
        club = clubs[selected]
        document.getElementById("clubName").innerText = selected
        document.getElementById("clubDesc").innerText = club["Description"]
        document.getElementById("clubTime").innerText = club["Meeting Time"]
        document.getElementById("clubLocation").innerText = club["Location"]
        document.getElementById("clubModerator").innerText = club["Club Moderator"]
        document.getElementById("clubMembers").innerText = club["Number of Members"]
        info_card.style.display = "block"
    else:
        info_card.style.display = "none"

# Bind the button click to the function
document.getElementById("showInfoBtn").addEventListener("click", showClubInfo)
