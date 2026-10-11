from django.http import HttpResponse


def page(title, content):
    bootstrap = (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
        "/dist/css/bootstrap.min.css"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <link rel="stylesheet" href="{bootstrap}">
</head>
<body>
    <nav class="navbar navbar-expand navbar-dark bg-dark mb-4">
        <div class="container">
            <a class="navbar-brand" href="/">Учёт энергии</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/">Главная</a>
                <a class="nav-link" href="/objects/">Объекты</a>
                <a class="nav-link" href="/meters/">Счётчики</a>
                <a class="nav-link" href="/readings/">Показания</a>
            </div>
        </div>
    </nav>
    <main class="container">{content}</main>
</body>
</html>"""


def index(request):
    content = """
    <h1 class="display-4">Система учёта энергопотребления</h1>
    <p class="lead">
        Веб-интерфейс для сотрудников управляющей компании.
    </p>
    <p>
        На этом этапе отображаются данные предметной области,
        сохранённые после ПР3: объект, счётчик, показание и период.
    </p>
    <a href="/objects/" class="btn btn-primary me-2">Объекты</a>
    <a href="/meters/" class="btn btn-secondary me-2">Счётчики</a>
    <a href="/readings/" class="btn btn-outline-secondary">Показания</a>
    """
    return HttpResponse(page("Учёт энергопотребления", content))


def page_not_found(request, exception):
    content = """
    <h1 class="text-danger">404 – страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 – страница не найдена", content),
        status=404,
    )
