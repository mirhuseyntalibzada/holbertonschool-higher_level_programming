import os
import re


def generate_invitations(template_content, attendees):
    """
    Generate invitation files for each attendee based on a template.

    Args:
        template_content (str): Template string with placeholders.
        attendees (list): List of dictionaries containing attendee data.

    Behavior:
        - Validates input types.
        - Replaces missing placeholder values with "N/A".
        - Writes each invitation to a uniquely named file.
        - Checks if files already exist to avoid overwriting.
    """
    try:
        if not isinstance(template_content, str):
            print(
                f"Error: Template must be a string, got {type(template_content).__name__}"
            )
            return

        if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
            print(
                f"Error: Attendees must be a list of dictionaries, got {type(attendees).__name__}"
            )
            return

        if not template_content.strip():
            print("Template is empty, no output files generated.")
            return

        if not attendees:
            print("No data provided, no output files generated.")
            return

        placeholders = re.findall(r"{(.*?)}", template_content)

        for i, attendee in enumerate(attendees, start=1):
            try:
                invitation = template_content
                for key in placeholders:
                    value = str(attendee.get(key, "N/A"))
                    invitation = invitation.replace(f"{{{key}}}", value)

                base_filename = f"output_{i}.txt"
                filename = base_filename
                counter = 1
                while os.path.exists(filename):
                    filename = f"output_{i}_{counter}.txt"
                    counter += 1

                with open(filename, "w", encoding="utf-8") as file:
                    file.write(invitation)

                print(f"Created {filename}")

            except Exception as e:
                print(f"Error processing attendee {i}: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
