# Note-Taking-with-sql--and-python

This CLI application will prompt users to create, view, or list notes that are stored in a PostgreSQL database.

### Languages Frameworks and Database
------

* Python 3
* PeeWee
* PostgreSQL

### The breakdown
------

To use this CLI application, Fork and Clone this repository. Navigate to the src directory and run python main.py <action to perform here> from the terminal.

* There are three actiions users can perform
    * create_note
    * view_note
    * list_notes
* The first two actions listed will prompt users for some input. Examples provided below:

* For create_note: run `python main.py create_note`
    * example input and output:
        ```
        Enter a title for your note. Test note 100
        What is your note? This is a demo note for presentation!
        Note Test note 100 created successfully!
        ```
* for view_note: run `python main.py view_note`

    * example input and output:
        ```
        Enter a note ID you wish to view. 4
        Title: Test note 100
        Content: This is a demo note for presentation!
        Create_Date: 2023-04-15 21:38:51.707209
        ```
* for list_notes: run `python main.py list_notes`
    * example input and output:

        ```
        ID: 1 | Title: Hi | Created_Date: 2023-04-15 21:22:31.973857
        ID: 2 | Title: hi | Created_Date: 2023-04-15 21:23:44.325030
        ID: 3 | Title: Test | Created_Date: 2023-04-15 21:24:28.480230
        ID: 4 | Title: Test note 100 | Created_Date: 2023-04-15 21:38:51.707209
        ```

This application represents a simple note input and output where users can create and view notes. 

## Future implementations

* an update and delete feature for notes 
* a UI feature for notes
* a implementation for notes from CLI to a front end application using django.

## URLs

Repository URL: https://github.com/locb65/Note-Taking-with-sql--and-python