
import json
from pathlib import Path


DIRECTIONS = ["north", "east", "south", "west", "up", "down"]


def ask_non_empty(prompt):
    """Ask for text until the user enters something non-empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def ask_integer(prompt, minimum=1):
    """Ask for a valid integer."""
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)
            if number >= minimum:
                return number
            print(f"Please enter a number of at least {minimum}.")
        except ValueError:
            print("Please enter a valid whole number.")


def ask_description(prompt):
    """Allow descriptions to be empty, e.g. alternativeDescription."""
    return input(prompt).strip()


def ask_dark_room():
    """Only allow true or false."""
    while True:
        value = input('Dark room? ("true" or "false"): ').strip().lower()

        if value in ("true", "false"):
            return value

        print('Please enter exactly "true" or "false".')


def ask_objects():
    """Collect objects until the user types done or none."""
    objects = []

    print('Enter objects one at a time.')
    print('Type "done" or "none" when finished.')

    while True:
        value = input("Object: ").strip()

        if value.lower() in ("done", "none"):
            if value.lower() == "none" and not objects:
                return []
            if value.lower() == "none":
                print("Keeping the objects already entered.")
            return objects

        if value:
            objects.append(value)
            print(f"Added: {value}")


def ask_connection(direction, valid_room_ids):
    """Ask for a room ID or none, converting none to 0."""
    while True:
        value = input(f"{direction.capitalize()}: ").strip().lower()

        if value == "none":
            return 0

        try:
            room_id = int(value)

            if room_id not in valid_room_ids:
                print("That room ID is not part of this map.")
                continue

            return room_id

        except ValueError:
            print('Enter a valid room ID or type "none".')


def main():
    print("=" * 40)
    print("     BACKROOMS MAP CREATOR")
    print("=" * 40)

    # File information
    filename = ask_non_empty(
        "Filename (example: level-23.json): "
    )

    if not filename.lower().endswith(".json"):
        filename += ".json"

    # Prevent accidentally treating a path as part of the filename.
    filename = Path(filename).name

    map_name = ask_non_empty(
        "Map name (example: Level 23): "
    )

    room_count = ask_integer("How many rooms do you need? ")

    starting_id = ask_integer("What room ID should it start from? ")

    # Generate room IDs before collecting connections.
    valid_room_ids = set(
        range(starting_id, starting_id + room_count)
    )

    rooms = []

    # Create each room.
    for room_id in sorted(valid_room_ids):
        print("\n" + "=" * 40)
        print(f"CONFIGURING ROOM {room_id}")
        print("=" * 40)

        room = {
            "id": room_id,
            "name": f"Room {room_id}",
            "description": ask_description("Description: "),
            "alreadyInRoomDescription": ask_description(
                "Already-in-room description: "
            ),
            "alternativeDescription": ask_description(
                "Alternative description: "
            ),
            "checkRoomMessage": ask_description(
                "Check-room message: "
            ),
            "darkRoom": ask_dark_room(),
            "objects": ask_objects(),
            "connections": {}
        }

        print("\nEnter connections for Room", room_id)
        print('Type "none" for a direction with no connection.')

        for direction in DIRECTIONS:
            room["connections"][direction] = ask_connection(
                direction, valid_room_ids
            )

        rooms.append(room)

    # Assemble the complete map.
    map_data = {
        "mapName": map_name,
        "rooms": rooms
    }

    output_path = Path(filename)

    # Do not overwrite an existing file without confirmation.
    if output_path.exists():
        while True:
            answer = input(
                f"\n{output_path} already exists. Overwrite? (yes/no): "
            ).strip().lower()

            if answer in ("yes", "y"):
                break
            elif answer in ("no", "n"):
                print("Cancelled. No file was overwritten.")
                return
            else:
                print('Please enter "yes" or "no".')

    # Save the JSON file.
    try:
        with output_path.open("w", encoding="utf-8") as file:
            json.dump(
                map_data,
                file,
                indent=2,
                ensure_ascii=False
            )
            file.write("\n")

        print("\n" + "=" * 40)
        print("MAP CREATED SUCCESSFULLY!")
        print(f"File: {output_path.resolve()}")
        print(f"Map name: {map_name}")
        print(f"Rooms created: {len(rooms)}")
        print("=" * 40)

    except OSError as error:
        print(f"Could not save the file: {error}")


if __name__ == "__main__":
    main()
