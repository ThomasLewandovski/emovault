import streamlit.web.cli as stcli
import sys
import os

def resolve_path(path):
    resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path

if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("app/main.py"),  # 替换为您的主应用路径
        "--global.developmentMode=false",
    ]
    stcli.main()
