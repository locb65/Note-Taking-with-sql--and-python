# import peewee
from peewee import *
from datetime import datetime
import argparse

# set up db connection

db = PostgresqlDatabase('notes', user = '<your_username>', password = '<your_password>', host = 'localhost', port = 5432)

db.connect()

# create model with peewee

class basic_model(Model):
    class Meta:
        database = db

class notes(basic_model):
    title = CharField()
    note_content = TextField()
    # sets date note made to date time stamp
    create_date = DateTimeField(default=datetime.now())

# db.create_tables([notes])

# note_1 = notes(title = "Test Note 1", note_content ="This is a test note to make sure a note can be created")
# note_1.save()

# made new relation of notes.

# db.drop_tables([notes])
# db.create_tables([notes])


# need to define functions for create notes, list notes, and select/view specific notes

def create_notes():
    # prompts users for note input
    title = input('Enter a title for your note. ')
    content = input('What is your note? ')

    # sets new note to the columns in postgresql
    new_note = notes(title = title, note_content = content)
    new_note.save()
    # prints create message to console
    print(f'Note {new_note.title} created successfully!')

# view notes

def view_notes():
    # prompts user for note id they wish to see
    note_id = input('Enter a note ID you wish to view. ')
    
    # sets get method to a new variable 
    view_note = notes.get(id = note_id)
    
    # prints the data for view_note to console
    print(f'Title: {view_note.title}')
    print(f'Content: {view_note.note_content}')
    print(f'Create_Date: {view_note.create_date}')

# function for listing all notes
# will iterate through each note and print data listed to console
# will return no notes found if there are no notes in db

def list_notes():
    list_notes = notes.select()
    if notes:
        for note in notes:
            print(f'ID: {note.id} | Title: {note.title} | Created_Date: {note.create_date}')
    else:
        print('No notes found...')

# need to implement argparse

if __name__ == '__main__':
    # sets up application name
    parser = argparse.ArgumentParser(description="Note Taker")
    # need to implement a way to have actions in console like create_note, view_note, list_notes
    # add parser argument
    # sets up actions available using parser.add_argument()

    parser.add_argument('actions', choices = ['create_note', 'view_note', 'list_notes'], help='Actions available to Note Taking')

    # using the arguments

    args = parser.parse_args()

    # conditions for actions and which function to invoke

    if args.actions == 'create_note':
        create_notes()
    elif args.actions == 'view_note':
        view_notes()
    elif args.actions == 'list_notes':
        list_notes()

