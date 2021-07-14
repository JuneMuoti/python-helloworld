# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8
LABEL maintainer="June Muoti"


# Install pip requirements
COPY . /app
WORKDIR  /app
RUN  pip install -r requirements.txt

CMD ["python", "app.py"]


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
