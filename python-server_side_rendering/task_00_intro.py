import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    if not attendess:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template.replace("{name}", attendee.get("name", "N/A"))
        invitation = invitation.replace("{event_title}", attendee.get("event_title", "N/A"))
        invitation = invitation.replace("{event_date}", attendee.get("event_date", "N/A") if attendee.get("event_date") is not None else "N/A")
        invitation = invitation.replace("{event_location}", attendee.get("event_location", "N/A"))

        output_filename = f"output_{index}.txt"

        with open(output_filename, "w") as output_file:
            output_file.write(invitation)

            print(f"Generated {output_filename}")
