import os


dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    os.path.join("prediction_service", "model"),
    os.path.join("webapp", "static", "css"),
    os.path.join("webapp", "static", "script"),
    os.path.join("webapp", "templates"),
    "webapp",
    "notebooks",
    "saved_models",
    "src"
    "report"
    "tests"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init_.py"),
    "README",
    os.path.join("report", "params.json"),
    os.path.join("tests", "scores.json"),
    os.path.join("tests", "conftest.py"),
    os.path.join("tests", "test_config.py"),
    os.path.join("tests", "__init__.py"),
    os.path.join("prediction_service", "__init__.py"),
    "app.py",
    os.path.join("webapp", "static", "css", "main.css"),
    os.path.join("webapp", "static", "script", "index.js"),
    os.path.join("webapp", "templates", "index.html"),
    os.path.join("webapp", "templates", "404.html"),
    os.path.join("webapp", "templates", "base.html")
]

for file_ in files:
    with open(file_, "w") as f:
        pass
