from book.models import Book

# exec(open(r'F:\python\my-projects\Django_Projects_new\LibraryProject\book\db_shell.py').read())

#print(Book.objects.get_active_objects())
#print(Book.objects.get_inactive_objects())

from datetime import datetime

Book.objects.using("secondary").create(title="Book5", author="Auth5",
                    pulication_date=datetime(2023,10,23), price=667)