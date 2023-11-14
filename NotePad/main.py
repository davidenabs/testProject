import os
# store a note with the title and it content

# we use the title of the note as the name of the file

# we display all the note to the user

# user can search for a  note


def displayMessage():
    print('1. Add a note: ')
    print('2. Display all notes: ')
    print('3. Exit app: ')
def exitApp():
    print('Goodbye!')
    print('See you later.')

def displayAllNotes():
    files = os.listdir('Storage')
    return files


def createNoteFile(filename):
    filename = 'Storage/' + filename + '.txt'
    open(filename, 'x')
    return filename

def addNoteBodyToTheFile(filename, body):
    file = open(filename, 'a')
    file.write(body)
    file.close()

def addNote():
    print('Enter your note title:')
    note_title = input()

    # all the function to create the file that the note will be stored
    # the file is created based on the title the user provides
    filename = createNoteFile(note_title)

    print('Enter the body of the note:')
    note_body = input()

    # this function add the note body to the file that was created
    addNoteBodyToTheFile(filename, note_body)

    print('Note added successfully!')
    print()

# main app
while True:
    displayMessage()

    userResponse = input()

    if userResponse == '1':
        addNote()
    elif userResponse == '2':
        files = displayAllNotes()

        for i, file in enumerate(files):
            print(f'{i+1} {file}')
        print()

        print('Enter a number:')

    elif userResponse == '3':
        exitApp()
        break
    else:
        print('Invalid input!')
        print('Select either 1 or 2')
        print()
