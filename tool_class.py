import json
import os.path


class _ToolClass(object):
    def __init__(self):
        pass

    @staticmethod
    def return_html(file_name):
        path = os.path.join(os.path.join("static", "html"), file_name)
        with open(path, 'r', encoding="utf-8") as f:
            data = f.read()
        return data

    @staticmethod
    def return_xml(file_name):
        path = os.path.join(os.path.join("static", "xml"), file_name)
        with open(path, 'r', encoding="utf-8") as f:
            data = f.read()
        return data

    @staticmethod
    def return_json(file_name):
        path = os.path.join(os.path.join("static", "json"), file_name)
        with open(path, 'r', encoding="utf-8") as f:
            data = json.load(f)
        return data

    @staticmethod
    def return_text(file_name):
        path = os.path.join(os.path.join("static", "other"), file_name)
        with open(path, 'r', encoding="utf") as f:
            data = f.read()
        return data

    @staticmethod
    def return_css(file_name):
        path = os.path.join(os.path.join("static", "css"), file_name)
        with open(path, 'r', encoding="utf") as f:
            data = f.read()
        return data

    @staticmethod
    def return_javascript(file_name):
        path = os.path.join(os.path.join("static", "javascript"), file_name)
        with open(path, 'r', encoding="utf") as f:
            data = f.read()
        return data

    @staticmethod
    def return_image(file_name):
        path = os.path.join(os.path.join("static", "image"), file_name)
        with open(path, 'rb') as f:
            data = f.read()
        return data


def return_html(file_name):
    return _ToolClass.return_html(file_name)


def return_javascript(file_name):
    return _ToolClass.return_javascript(file_name)


def return_json(file_name):
    return _ToolClass.return_json(file_name)


def return_text(file_name):
    return _ToolClass.return_text(file_name)


def return_css(file_name):
    return _ToolClass.return_css(file_name)


def return_xml(file_name):
    return _ToolClass.return_xml(file_name)


def return_image(file_name):
    return _ToolClass.return_image(file_name)
