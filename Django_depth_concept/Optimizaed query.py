






1) selected query :  use when fields relationship between oneToOne or oneToMany !

    from django.db.models import select_related, connection
    #without selected query
    book = Book.objects.all()
    for book in book:
        print(book.name)
        print(book.author.name)
        print(book.author.email)
        # select * from book
        # select * from author where id = book.author_id
    
    #with selected query
    book = Book.objects.select_related('author').all()
    for book in book:
        print(book.name)
        print(book.author.name)
        print(book.author.email)
        # select book.* , author.* from book INNER JOIN authorON book.author_id = author.id

2) Prefetch query : use when fields relationship between  manytomany or manytoone !
    #without Prefetch query
    book = Book.objects.all()
    for book in book:
        print(book.name)
        print(book.author.name)
        print(book.author.email)
        
        # select * from book
        # select * from author where id = book.author_id
        # select * from tag where id in book.tag_id

    #with selected query
    book = Book.objects.prefetch_related('tags')
    for book in book:
        print(book.name)
        print(book.author.name)
        print(book.author.email)
        for tag in book.tags.all():
           print(tag.name)








