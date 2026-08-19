import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def read_contacts(request: Request):
    """
    Обрабатывает любые GET запросы и возвращает страницу контактов.

    :param request: Объект запроса от FastAPI.
    :return: Содержимое файла contacts.html.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_path = os.path.join(base_dir, "templates", "contacts.html")

    try:
        with open(template_path, mode="r", encoding="utf-8") as file:
            html_content = file.read()

        return HTMLResponse(content=html_content, status_code=200)

    except FileNotFoundError:
        return HTMLResponse("Файл не найден.", status_code=404)
