FROM python:3.13.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/
#memasukkan aplikasi uv ke dalam image docker yang akan dibuat

WORKDIR /code 
#perintah workdir itu seperti cd, yang mana berarti beralih ke folder code

ENV PATH="/code/.venv/bin:$PATH"
#env yang berfungsi mengarahkan instalasi depedensi yang ada di dalam folder /.venv/
#depedensi adalah library atau packager pihak ketiga

COPY pyproject.toml .python-version uv.lock ./
#copy file yang ada di pipeline ke dalam sebuah folder code

RUN uv sync --locked
#menjalankan instalasi depedensi yang ada di pyproject.toml

COPY pipeline.py .
#sama seperti di atas yang copy ke folder code

ENTRYPOINT [ "python", "pipeline.py" ]
#Entry poin hanya menjalankan file/script yang ada di dalam list