### command line options:
```
  -h                show this help message and exit
  -a "text" "text"  adds a note. First part is "Title" second is "Body of the note"

  -e int            edits a note by "int" use -t "text" or/and -b "text" options
  -t text           defines "Title" text of the note
  -b text           defines "Body" text of the note

  -d int            deletes a note by "int"
  -s int            shows a note by "int"
  -l                lists notes
```
  <!-- -o (a/d)          Option sort (a/d) (Acsending/Descending) -->

___
### note structure
    index: int
    title: str
    notetext: str
    cmdate: float (timestamp from datetime)
___
### dbase class? am i need it?

