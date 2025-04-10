from django.http import HttpResponse

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

    return HttpResponse(tmp_name)
