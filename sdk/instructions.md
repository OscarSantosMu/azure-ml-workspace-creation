# Instructions

Create a virtualenv

```console
python -m venv venv
```

For Windows
```
venv\Scripts\activate
```

For Linux or macOS
```
source venv/bin/activate
```

Install the Azure Machine Learning SDK by running the following command in your terminal or command prompt:

```console
pip install -r requirements.txt
```

Create a .env file like the .env.example and replace the values of these variables with your subscription and resource group.

Run the Python script named create_workspace.py

```python
python create_workspace.py
```