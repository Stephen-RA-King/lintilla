FROM python:3.9-alpine
WORKDIR /apps/lintilla/
COPY src/lintilla/. .
COPY requirements/development.txt .
RUN ["pip", "install",  "--no-cache-dir", "-r", "development.txt"]
CMD ["python", "lintilla.py"]
