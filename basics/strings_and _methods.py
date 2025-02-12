# strings and their methods
name = "ibad uddin"

print(name.title()) #title() method
print(name.upper()) #upper() method
print(name.lower()) #lower() method

first_name = "ammad"
last_name = "uddin"
full_name = f"{first_name} {last_name}"
# The f before the string makes it an f-string (formatted string)
# It allows us to embed expressions inside string literals using {}
# Here it combines first_name and last_name into full_name
print(f"  Assalmualikum , {full_name.title()}")  # This will print: ammad uddin

formatted_name = f" Assalmualikum  again , {first_name} {last_name}"

print(formatted_name.title())

linked_in_url = "https://www.linkedin.com/feed/"

print(linked_in_url.removeprefix("https://"))

file_name = "python_notes.txt"

print(file_name.removesuffix(".txt"))







