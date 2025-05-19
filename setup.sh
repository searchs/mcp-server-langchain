#!/bin/bash

PROJECT_NAME="mcp-server"

echo "Creating MCP Server project structure..."

mkdir -p $PROJECT_NAME/app/{routes,services,llm}
touch $PROJECT_NAME/{README.md,requirements.txt,run.sh}
touch $PROJECT_NAME/app/{__init__.py,config.py}
touch $PROJECT_NAME/app/main.py
touch $PROJECT_NAME/app/routes/{__init__.py,chat.py}
touch $PROJECT_NAME/app/services/{__init__.py,chat_service.py,redis_service.py}
touch $PROJECT_NAME/app/llm/{__init__.py,langchain_client.py}

echo "Done! Structure created:"
tree $PROJECT_NAME
