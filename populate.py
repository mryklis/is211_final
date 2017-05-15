import sqlite3

DATABASE = 'blog.db'
conn = sqlite3.connect(DATABASE)
c = conn.cursor()


# c.execute('''insert into POSTS (TITLE, PDATE, AUTHOR, BLOG) values ('TEST','2017-05-10', 'Maxim Ryklis',
# 'Mauris neque quam, fermentum ut nisl vitae, convallis maximus nisl. Sed mattis nunc id lorem euismod placerat.
# Vivamus porttitor magna enim, ac accumsan tortor cursus at. Phasellus sed ultricies mi non congue ullam corper.
# Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida
# diam non fringilla.')''')
# c.execute('''insert into POSTS (TITLE, PDATE, AUTHOR, BLOG) values ('TEST2','2017-05-11', 'Maxim Ryklis',
# 'Mauris neque quam, fermentum ut nisl vitae, convallis maximus nisl. Sed mattis nunc id lorem euismod placerat.
# Vivamus porttitor magna enim, ac accumsan tortor cursus at. Phasellus sed ultricies mi non congue ullam corper.
# Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida
# diam non fringilla.')''')
# c.execute('''insert into POSTS (TITLE, PDATE, AUTHOR, BLOG) values ('TEST3','2017-05-12', 'Maxim Ryklis',
# 'Mauris neque quam, fermentum ut nisl vitae, convallis maximus nisl. Sed mattis nunc id lorem euismod placerat.
# Vivamus porttitor magna enim, ac accumsan tortor cursus at. Phasellus sed ultricies mi non congue ullam corper.
# Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida
# diam non fringilla.')''')
# c.execute('''insert into POSTS (TITLE, PDATE, AUTHOR, BLOG) values ('TEST4','2017-05-13', 'Maxim Ryklis',
# 'Mauris neque quam, fermentum ut nisl vitae, convallis maximus nisl. Sed mattis nunc id lorem euismod placerat.
# Vivamus porttitor magna enim, ac accumsan tortor cursus at. Phasellus sed ultricies mi non congue ullam corper.
# Praesent tincidunt sed tellus ut rutrum. Sed vitae justo condimentum, porta lectus vitae, ultricies congue gravida
# diam non fringilla.')''')
# conn.commit()

c.execute('''select * from POSTS''')
print(c.fetchall())