****NOTE**** 
I made changes to some of the html elements, python codes, changed database config and database properties to suit my understanding. so  read inbetween the lines to notice changes and refer changes to yours. Thank you.

   THINGS TO NOTE IN HTML

   {{todo.id}} | {{todo.title}} | {{todo.date}} #This displays a todo in todos based on its id, title,date
   the .id, .title and .date are the properties or atributes above each column. More like the heading of each column in your db.

#<input type="hidden" name="old_todo" value="{{ todo.title }}" >     
#<input type="text" name="edit_todo"  placeholder="Edit TO Do... ">
#<input class="btn" type="submit" value="Edit">
#Above are the inputs for the edit/upgrade function. The first line we include a hidden input. This section of the form will not be shown to our user, but we'll be able to access the value from our Python code.
