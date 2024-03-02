'''0x0'''

import os
import webbrowser
import base64
import requests
import PySimpleGUI as sg

# PySimpleGUI config
FONT_ARIAL = 'Arial'
F_FOOTER = (FONT_ARIAL, 15)
F_SMALL = (FONT_ARIAL, 20)
F_MEDIUM = (FONT_ARIAL, 30)
F_LARGE = (FONT_ARIAL, 50)
SGSIZE = (800, 400)

sg.theme("BrownBlue")

icon_path = os.path.join(os.path.dirname(__file__), "img", "logo_tb.png")

icon = base64.b64encode(open(icon_path, "rb").read())

# 0x0 upload
def upload(file):
    '''uploads file to 0x0.st'''

    url = "https://0x0.st"
    with open(file, "rb") as handler:
        post_data = {"file":handler}
        resp = requests.post(url, timeout = 10, files = post_data)
    return resp.text

# Visibility
def place(elem):
    '''place element'''

    return sg.Column([[elem]], pad = (0, 0))

# GUI
def main():
    '''main (GUI)'''

    logo_img = os.path.join(os.path.dirname(__file__), "img", "logo.png")

    layout = [
        [sg.Image(logo_img), sg.Push(), sg.Button("0x0.st", key = "-0x0_buton-", font = F_LARGE, enable_events = True, size = 15)],
        [sg.VPush()],
        [sg.Input("", key = "-input-", expand_x = True, font = F_SMALL, readonly = True)],
        [sg.VPush()],
        [sg.Push(), sg.FileBrowse(key = "-IN-", font = F_MEDIUM, enable_events = True, target="-input-"), sg.Push(), sg.Button("Upload", key = "-upload-", font = F_MEDIUM), sg.Push()],
        [sg.VPush()],
        [sg.Push(), place(sg.Button("", key = "-upload_url-", font = F_LARGE, enable_events = True, visible = False)), sg.Push()],
        [sg.VPush()],
        [sg.HorizontalSeparator()],
        [sg.Push(), sg.VerticalSeparator(), sg.Push(), sg.Text("Made by", font = F_FOOTER),sg.Push(), sg.Text(":", font = F_FOOTER), sg.Push(), sg.Text("Villers", font = F_FOOTER), sg.Push(), sg.VerticalSeparator(), sg.Push()]
    ]

    window = sg.Window("0x0.st uploader", layout, finalize = True, resizable = False, icon = icon)
    window.bind("<Escape>", "-ESCAPE-")

    url = None

    while True:
        event, value = window.read()
        if event in ["Exit", sg.WIN_CLOSED, "-ESCAPE-"]:
            break
        if event == "-upload-":
            window["-upload_url-"].update(visible = True)
            if value["-IN-"] != "":
                url = upload(value["-IN-"]).strip()
                window["-upload_url-"].update(url)
            elif value["-IN-"] == "":
                window["-upload_url-"].update("No file selected")
        if event == "-upload_url-" and url is not None:
            webbrowser.open(url, new = 2)
        if event == "-0x0_buton-":
            webbrowser.open("https://0x0.st", new = 2)

if __name__ == "__main__":
    main()
