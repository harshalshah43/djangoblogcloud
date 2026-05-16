#!/bin/bash

set -e

echo "==============================="
echo "Starting Deployment..."
echo "==============================="

PROJECT_DIR="$HOME/djangoblogcloud"
REPO_URL="https://github.com/harshalshah43/djangoblogcloud.git"
VENV_DIR="$HOME/.virtualenvs/myenv"

echo ""
echo "Checking project repository..."

# Clone repo if missing
if [ ! -d "$PROJECT_DIR/.git" ]; then
    echo "Repository not found."
    echo "Cloning repository..."

    git clone -b dev "$REPO_URL" "$PROJECT_DIR"
else
    echo "Repository already exists."
fi

echo ""
echo "Moving into project directory..."
cd "$PROJECT_DIR"

echo ""
echo "Checking virtual environment..."

# Create virtualenv if missing
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtualenv not found."
    echo "Creating virtualenv..."

    python3.12 -m venv "$VENV_DIR"
else
    echo "Virtualenv already exists."
fi

echo ""
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo ""
echo "Pulling latest code..."
git pull origin dev

echo ""
echo "Checking dependencies..."

REQ_HASH_FILE=".requirements.hash"

if [ -f requirements.txt ]; then

    CURRENT_HASH=$(md5sum requirements.txt | awk '{print $1}')

    if [ -f "$REQ_HASH_FILE" ]; then
        OLD_HASH=$(cat "$REQ_HASH_FILE")
    else
        OLD_HASH=""
    fi

    if [ "$CURRENT_HASH" != "$OLD_HASH" ]; then
        echo "requirements.txt changed."
        echo "Installing dependencies..."

        pip install -r requirements.txt

        echo "$CURRENT_HASH" > "$REQ_HASH_FILE"
    else
        echo "requirements.txt unchanged."
        echo "Skipping dependency installation."
    fi

else
    echo "requirements.txt not found!"
fi

echo ""
echo "Applying migrations..."
python manage.py migrate

echo ""
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "Reloading application..."
touch /var/www/hns499_pythonanywhere_com_wsgi.py

echo ""
echo "==============================="
echo "Deployment Successful!"
echo "==============================="