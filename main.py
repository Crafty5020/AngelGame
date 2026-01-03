import json
import os
from time import sleep

inventory = []
room = "outside"
floor = ""
death = False
aiInRoom = ""
aiIRoom = ""
money = 0
rooms = json.load(open("floors.json"))
items = json.load(open("items.json"))


def MainLoop():
	while not death:
		getFloor()
		print("===========================================")
		print(f"You are currently in the {room} on {floor}.") # type: ignore
		print("===========================================")
		listInventory()
		listRooms()
		print("___________________________________________")
		print("For camera type 'c', for discovered code type 'code', to hide type 'h', to go to another room type 'go [room name]'")
		print("-------------------------------------------")
		userInput = input("What would you like to do? ").lower().strip()
		if userInput == "c":
			cam()
		elif userInput.startswith("go "):
			nextRoom(userInput[3:])
		elif userInput == "code" or userInput == "codes":
			listCode()
		else:
			clearScreen()
			print("Invalid input, please try again.")

def getFloor():
	global floor
	for tempFloor, floorRooms in rooms.items():
		if room in floorRooms:
			floor = tempFloor
			return
	raise ValueError(f"Room '{room}' not found in any floor")

def clearScreen():
	command = 'cls' if os.name == 'nt' else 'clear'
	os.system(command)

def listRooms():
	print(f"Possible moves: {rooms[floor][room]["con"]}")

def listInventory():
	print(f"Inventory: {inventory}")

def nextRoom(nextRoom: str):
	clearScreen()
	if nextRoom not in rooms[floor]:
		print("That room does not exist or its written incorrectly, please try again.")
		return
	if "" != rooms[floor][nextRoom]["special"]:
		specialRoom(nextRoom)
	global room 
	room = nextRoom

def specialRoom(nextRoom: str):
	clearScreen()
	if rooms[floor][nextRoom]["special"] == "base":
		print("This area is closed off, it looks like a keycard, pin code are required to enter.")
		sleep(2)
	global room
	room = rooms[floor][nextRoom]["con"][1]
	return
def listCode():
	clearScreen()
	if "LockpadCode1" in inventory:
		print("Keep turning right to 10")
	elif "LockpadCode2" in inventory:
		print("Turn left to 16")
	elif "LockpadCode3" in inventory:
		print("Turn right to 21")
	else:
		print("You have not discovered any codes yet.")

def start():
	clearScreen()
	print("Welcome to the Adventure Game! Try to find the codes and dont get caught!")
	MainLoop()

def cam():
	clearScreen()
	pass

if __name__ == "__main__":
	start()