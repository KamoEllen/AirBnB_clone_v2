- **Project Overview:** 
  - The repository contains the initial stage of a student project to build a clone of the Airbnb website.
  - This stage implements a backend interface, or console, to manage program data.
  - Console commands allow the user to create, update, and destroy objects, as well as manage file storage.
  - Storage is persistent between sessions using a system of JSON serialization/deserialization.

- **Repository Contents by Project Task:**
  - **Task 0:** Authors/README File - [AUTHORS](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/AUTHORS)
  - **Task 1:** Pep8 - All code is pep8 compliant
  - **Task 2:** Unit Testing - [/tests](https://github.com/KamoEllen/AirBnB_clone_v2/tree/dev/tests)
  - **Task 3:** Make BaseModel - [/models/base_model.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/base_model.py)
  - **Task 4:** Update BaseModel w/ kwargs - [/models/base_model.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/base_model.py)
  - **Task 5:** Create FileStorage class - [/models/engine/file_storage.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/engine/file_storage.py), [/models/__init__.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/__init__.py), [/models/base_model.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/base_model.py)
  - **Task 6:** Console 0.0.1 - [console.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/console.py)
  - **Task 7:** Console 0.1 - [console.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/console.py)
  - **Task 8:** Create User class - [console.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/console.py), [/models/engine/file_storage.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/engine/file_storage.py), [/models/user.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/user.py)
  - **Task 9:** More Classes - [/models/user.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/user.py), [/models/place.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/place.py), [/models/city.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/city.py), [/models/amenity.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/amenity.py), [/models/state.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/state.py), [/models/review.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/review.py)
  - **Task 10:** Console 1.0 - [console.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/console.py), [/models/engine/file_storage.py](https://github.com/KamoEllen/AirBnB_clone_v2/blob/dev/models/engine/file_storage.py)

- **General Use:**
  1. Clone the repository.
  2. Locate the "console.py" file and run it.
  3. The prompt "(hbnb)" indicates you are in the "HBnB" console.
  4. Various commands are available:
     - create, destroy, show, all, update, quit
  5. Advanced syntax is available for some commands.

- **Examples:**
  - Primary Command Syntax Examples:
    - Creating an object: `create BaseModel`
    - Showing an object: `show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8`
    - Destroying an object: `destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8`
    - Updating an object: `update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"`

  - Alternative Syntax Examples:
    - Showing all User objects: `User.all()`
    - Destroying a User: `User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")`
    - Updating a User by attribute: `User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")`
    - Updating a User by dictionary: `User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})`