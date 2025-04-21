from django.http import HttpResponse, JsonResponse



Books = {
    1:{
        "title":"Окрема реальність",
        "author":"Карлос Кастанеда",
        "price":200,
        "genre":"Magic",
        "link":"https://bookchef.ua/upload/resize_cache/iblock/daa/390_390_1/daa72f5804777e323706d9d4e1c7b07f.jpg"
    },
    2:{
        "title":"Скажи мені",
        "author":"Енн Фрейзер",
        "price":350,
        "genre":"Fantastic",
        "link":"https://bookchef.ua/upload/resize_cache/iblock/421/245_390_1/421ec853aa4f5030628724fda0e5337b.jpg"
    },
    3:{
        "title":"Багаття долі",
        "author":"Оділь Буе",
        "price":450,
        "genre":"Fantastic",
        "link":"https://bookchef.ua/upload/resize_cache/iblock/75d/390_390_1/75d5ce78abbbe841bc7871fb1ae8a113.png"
    },
    4:{
        "title":"Нічна зміна",
        "author":"М. Л. Ріо",
        "price":270,
        "genre":"Fantastic",
        "link":"https://bookchef.ua/upload/resize_cache/iblock/31d/390_390_1/31df656500113ca2eb28ab22d4b85c78.png"
    },
    5:{
        "title":"ChatGPT",
        "author":"Олександр Краковецький",
        "price":300,
        "genre":"Science",
        "link":"https://bookchef.ua/upload/resize_cache/iblock/b53/390_390_1/b535ed6bd1bf04168048a020df8cf8a5.jpg"
    },
}

def book_list(request):
    books = """
        <h1 style = "text-align: center; margin-top: 100px; margin-bottom: 100px;">Список книг</h1>
        <ul style = "display: flex; justify-content: center; list-style: none; gap: 100px;">
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/daa/390_390_1/daa72f5804777e323706d9d4e1c7b07f.jpg" width=200 alt="photo">
            <h2>Окрема реальність</h2>
            <h2>Карлос Кастанеда</h2>
            </li>
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/421/245_390_1/421ec853aa4f5030628724fda0e5337b.jpg" width=200 alt="photo">
            <h2>Скажи мені</h2>
            <h2>Енн Фрейзер</h2>
            </li>
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/75d/390_390_1/75d5ce78abbbe841bc7871fb1ae8a113.png" width=200 alt="photo">
            <h2>Багаття долі</h2>
            <h2>Оділь Буе</h2>
            </li>
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/31d/390_390_1/31df656500113ca2eb28ab22d4b85c78.png" width=200 alt="photo">
            <h2>Нічна зміна</h2>
            <h2>М. Л. Ріо</h2>
            </li>
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/b53/390_390_1/b535ed6bd1bf04168048a020df8cf8a5.jpg" width=200 alt="photo">
            <h2>ChatGPT</h2>
            <h2>Олександр Краковецький</h2>
            </li>
        </ul>
    """
    return HttpResponse(books)

def new_book(request):
    newBook = """
        <h1 style = "text-align: center; margin-top: 100px; margin-bottom: 100px;">Список нових книг</h1>
        <ul style = "display: flex; justify-content: center; list-style: none; gap: 100px;">
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/daa/390_390_1/daa72f5804777e323706d9d4e1c7b07f.jpg" width=200 alt="photo">
            <h2>Окрема реальність</h2>
            <h2>Карлос Кастанеда</h2>
            </li>
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/421/245_390_1/421ec853aa4f5030628724fda0e5337b.jpg" width=200 alt="photo">
            <h2>Скажи мені</h2>
            <h2>Енн Фрейзер</h2>
            </li>
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/75d/390_390_1/75d5ce78abbbe841bc7871fb1ae8a113.png" width=200 alt="photo">
            <h2>Багаття долі</h2>
            <h2>Оділь Буе</h2>
            </li>
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/31d/390_390_1/31df656500113ca2eb28ab22d4b85c78.png" width=200 alt="photo">
            <h2>Нічна зміна</h2>
            <h2>М. Л. Ріо</h2>
            </li>
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/b53/390_390_1/b535ed6bd1bf04168048a020df8cf8a5.jpg" width=200 alt="photo">
            <h2>ChatGPT</h2>
            <h2>Олександр Краковецький</h2>
            </li>
        </ul>
    """

    return HttpResponse(newBook)

def magic(request):
    magic = """
        <h1 style = "text-align: center; margin-top: 100px; margin-bottom: 100px;">Список книг за жанром</h1>
        <ul style = "display: flex; justify-content: center; list-style: none; gap: 100px;">
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/daa/390_390_1/daa72f5804777e323706d9d4e1c7b07f.jpg" width=200 alt="photo">
            <h2>Окрема реальність</h2>
            <h2>Карлос Кастанеда</h2>
            </li>
        </ul>
    """

    return HttpResponse(magic)

def fantastic(request):
    fantast = """
        <h1 style = "text-align: center; margin-top: 100px; margin-bottom: 100px;">Список книг за жанром</h1>
        <ul style = "display: flex; justify-content: center; list-style: none; gap: 100px;">
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/421/245_390_1/421ec853aa4f5030628724fda0e5337b.jpg" width=200 alt="photo">
            <h2>Скажи мені</h2>
            <h2>Енн Фрейзер</h2>
            </li>
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/75d/390_390_1/75d5ce78abbbe841bc7871fb1ae8a113.png" width=200 alt="photo">
            <h2>Багаття долі</h2>
            <h2>Оділь Буе</h2>
            </li>
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/31d/390_390_1/31df656500113ca2eb28ab22d4b85c78.png" width=200 alt="photo">
            <h2>Нічна зміна</h2>
            <h2>М. Л. Ріо</h2>
            </li>
        </ul>
    """

    return HttpResponse(fantast)

def science(request):
    scien = """
        <h1 style = "text-align: center; margin-top: 100px; margin-bottom: 100px;">Список книг за жанром</h1>
        <ul style = "display: flex; justify-content: center; list-style: none; gap: 100px;">
            <li>
            <img src="https://bookchef.ua/upload/resize_cache/iblock/b53/390_390_1/b535ed6bd1bf04168048a020df8cf8a5.jpg" width=200 alt="photo">
            <h2>ChatGPT</h2>
            <h2>Олександр Краковецький</h2>
            </li>
        </ul>
    """

    return HttpResponse(scien)

def get_book_by_id(request, book_id):
    book = Books.get(book_id)
    if book:
        book_details = f"""
            <h1 style = "text-align: center; margin-top: 100px; margin-bottom: 20px;">Знайдені книги</h1>
            <ul style = "display: flex; justify-content: center; list-style: none; gap: 100px;">
                <li>
                    <img src="{ book["link"] }" width=200 alt="photo">
                    <h2 style = "text-align: center; margin-top: 20px; margin-bottom: 20px;">{ book["title"] }</h2>
                    <h2 style = "text-align: center; margin-top: 20px; margin-bottom: 20px;">{ book["author"]}</h2>
                    <p style = "text-align: center; margin-top: 20px; margin-bottom: 20px;">Ціна: { book["price"] }</p>
                    <p style = "text-align: center; margin-top: 20px; margin-bottom: 20px;">Опис: { book["genre"] }</p>
                </li>
            </ul>
        """
        return HttpResponse(book_details)
    else:
        return HttpResponse("<h2>Книга не знайдена</h2>", status=404)

def search_book(request, part_of_title):
    result = [
        book for book in Books.values()
        if part_of_title.lower() in book["title"].lower()
    ]
    if result:
        book_details = """<h1 style = "text-align: center; margin-top: 100px; margin-bottom: 20px;">Знайдені книги</h1>
            <ul style = "display: flex; justify-content: center; list-style: none; gap: 100px;">"""
        for book in result:
            book_details += f"""
                    <li>
                        <img src="{ book["link"] }" width=200 alt="photo">
                        <h2>{book["title"]}</h2>
                        <h2>{book["author"]}</h2>
                        <p>Ціна: {book["price"]}</p>
                        <p>Опис: {book["genre"]}</p>
                    </li>
                """
            book_details += "</ul>"
        return HttpResponse(book_details)
    else:
        return HttpResponse("<h2>Книга не знайдена</h2>", status=404)

def filter_book_by_price(request, min_price, max_price):
    result = [
        book for book in Books.values()
        if min_price <= book["price"] <= max_price
    ]
    if result:
        book_details = """<h1 style = "text-align: center; margin-top: 100px; margin-bottom: 20px;">Знайдені книги</h1>
            """
        for book in result:
            book_details += f"""
                            <ul style = "display: flex; justify-content: center; list-style: none; gap: 100px;">
                                <li>
                                    <img src="{ book["link"] }" width=200 alt="photo">
                                    <h2>{book["title"]}</h2>
                                    <h2>{book["author"]}</h2>
                                    <p>Ціна: {book["price"]}</p>
                                    <p>Опис: {book["genre"]}</p>
                                </li>
                            </ul>
                        """

        return HttpResponse(book_details)
    else:
        return HttpResponse("<h2>Книга не знайдена</h2>", status=404)


def error(request):
    err = """
        <h1 style = "text-align: center; margin-top: 100px; margin-bottom: 100px;">Помилка 404</h1>
        <h2 style = "text-align: center; margin-top: 100px; margin-bottom: 100px;">Така сторінка не знайдена</h2>
    """

    return HttpResponse(err)

def dynamic_page(request, page_name):
    if page_name == 'new':
        tmp_name = new_book(request)
    elif page_name == 'magic':
        tmp_name = magic(request)
    elif page_name == 'fantastic':
        tmp_name = fantastic(request)
    elif page_name == 'science':
        tmp_name = science(request)
    else:
        tmp_name = error(request)

    return tmp_name
