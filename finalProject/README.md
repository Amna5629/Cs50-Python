Title : Birthstone Explorer

Video Demo: https://youtu.be/C1eR3LSOnyM

Description:
A Python program titled Birthstone Explorer was built to provide users the opportunity to find out better about their birthstones. Users are able to find out the name of their birthstone, a thorough description of it, famous individuals who share it, and a character description related to the gemstone by providing their name and birth month.

Project Overview:


This project allows users to interact with the program in a user-friendly manner..Users can access more detail about their birthstone after entering their details. In addition to displaying relevant details, the program allows users to save their birthstone information and personal information in a customized JSON file.

The project is structured to include several key functions:

read_birthstone_data(): This function reads the birthstone data from a CSV file and stores it in a dictionary format. Each month's birthstone, its description, famous people, and character traits are loaded for use in the program.

get_birthstone_character(birthstone_data): This function retrieves the character description associated with the user's birthstone from the birthstone data.

display_birthstone_info(stone_name, info, famous_people, character): This function displays all the detailed information about the user's birthstone, including the name, description, famous people, and character traits.

save_user_info(name, month, birthstone_data): This function saves the user's details and their birthstone information to a JSON file named after the user.

Files:

birthstones.csv: This CSV file contains the birthstone data for each month, including the birthstone's name, description, famous people associated with it, and a character description.

project.py: This is the main program file containing all the functions and the main logic to interact with the user.

README.md: The file you are currently reading. It serves as a comprehensive guide to the project, explaining its purpose, functionality, and structure.

test_project.py: This file contains the test cases for the functions in the project. It uses the pytest framework to ensure each function performs as expected.

Design Choices:
Ensuring user-friendliness was the primary  goal for this project. Users could easily interact with the program because of its design, which includes clear prompts and a smooth error handling system. Keeping the data accessible and well-organized was another reason for choosing to store birthstone data in a CSV file.

The choice to include a feature that lets users save customized data was also very important. Allowing users to record their birthstone and related information improves their overall experience.

Testing:
A vital step in the development process was testing. A series of test cases are part of the project that is designed to confirm that every important part functions as planned. To provide a reliable and secure user experience, the tests make sure the program can handle various kinds of inputs .

Conclusion:
The Birthstone Explorer is a comprehensive tool that offers users a deep dive into the world of gemstones and their meanings.
The project provides a smooth and educational experience for users who are curious about their birthstones by utilizing Python's capabilities.

