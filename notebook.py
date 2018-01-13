#!/usr/bin/python3
import pickle

class Note():
    def __init__(self, text, tags):
        self.text = text
        self.tags = tags
        
    def __str__(self):
        return self.text

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='text for new note', nargs='*')
    parser.add_argument('--type', choices=['note','todo'], default=['note'], nargs=1, help='choose to create a note or a todo list item; defaults to note')
    parser.add_argument('-t', '--tags', type=str, nargs='+')
    parser.add_argument('-l', '--list', action='store_true')
    parser.add_argument('-w', '--with-tags', dest='with_tags', action='store_true', help='list notes with tags')
    args = parser.parse_args()
        
    if args.type[0] == 'note':
        if args.list:
            notes = []
            notebook = open('pynotebook', 'rb')
            while True:
                try:
                    item = pickle.load(notebook)
                    if type(item == Note):
                        notes.append(item)
                except EOFError:
                    break
            for note in notes:
                print(note)
                if args.with_tags:
                    tags = ' '.join(note.tags)
                    print('tags: {}\n'.format(tags))
        else:
            if type(args.text) == list:
                text = ' '.join(args.text)
            else:
                text = args.text
            if args.tags == None:
                tags = []
            else:
                tags = args.tags
            new_note = Note(text, tags)
            notebook = open('pynotebook', 'ab')
            pickle.dump(new_note, notebook)
            notebook.close()