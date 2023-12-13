import requests
import PySimpleGUI as sg
import webbrowser

# PySimpleGUI config
font_arial = 'Arial'
f_footer = (font_arial, 15)
f_small = (font_arial, 20)
f_medium = (font_arial, 30)
f_large = (font_arial, 50)
sgsize = (800, 400)

# 0x0 upload
def upload(file):
    url = "https://0x0.st"
    with open(file, "rb") as handler:
        post_data = {"file":handler}
        resp = requests.post(url, timeout = 10, files = post_data)
    return resp.text

# Visibility
def place(elem):
    return sg.Column([[elem]], pad = (0, 0))

# GUI
def main():
    layout = [
        [sg.Push(), sg.Text("0x0.st uploader", font = f_large), sg.Push()],
        [sg.VPush()],
        [sg.Input("", key = "-input-", expand_x = True, font = f_small, readonly = True)],
        [sg.VPush()],
        [sg.Push(), sg.FileBrowse(key = "-IN-", font = f_medium, enable_events = True, target="-input-"), sg.Push(), sg.Button("Upload", key = "-upload-", font = f_medium), sg.Push()],
        [sg.VPush()],
        [sg.Push(), place(sg.Button("", key = "-upload_url-", font = f_large, enable_events = True, visible = False)), sg.Push()],
        [sg.VPush()],
        [sg.HorizontalSeparator()],
        [sg.Push(), sg.VerticalSeparator(), sg.Push(), sg.Text("Made by:", font = f_footer),sg.Push(), sg.Text("Villers", font = f_footer), sg.Push(), sg.VerticalSeparator(), sg.Push()]
    ]

    window = sg.Window("0x0.st uploader", layout, resizable = False) # add size = sgsize if you want fix size for the windows

    url = None

    while True:
        event, value = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "-upload-":
            window["-upload_url-"].update(visible = True)
            if value["-IN-"] != "":
                url = upload(value["-IN-"]).strip()
                window["-upload_url-"].update(url)
            elif value["-IN-"] == "":
                window["-upload_url-"].update("No file selected")
        if event == "-upload_url-" and url != None:
            webbrowser.open(url, new = 2)
main()