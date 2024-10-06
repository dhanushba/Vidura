import webbrowser
import subprocess

def open_website(website_name, mode=None):
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
    url_map = {
        "youtube": "https://www.youtube.com",
        "linkedin": "https://www.linkedin.com",
        "facebook": "https://www.facebook.com",
        "wikipedia": "https://www.wikipedia.org",
        "google": "https://www.google.com",
        "twitter": "https://www.twitter.com",
        "instagram": "https://www.instagram.com",
        "github": "https://www.github.com"
    }

    for site, url in url_map.items():
        if site in website_name:
            if mode == "incognito":
                subprocess.Popen([chrome_path, "--incognito", url])
                return
            elif mode == "developer":
                subprocess.Popen([chrome_path, "--auto-open-devtools-for-tabs", url])
                return
            else:
                webbrowser.open(url)
                return

    website_name = website_name.replace("open ", "").strip()
    url = f"https://{website_name}.com"
    try:
        if mode == "incognito":
            subprocess.Popen([chrome_path, "--incognito", url])
        elif mode == "developer":
            subprocess.Popen([chrome_path, "--auto-open-devtools-for-tabs", url])
        else:
            webbrowser.open(url)
    except Exception as e:
        print(f"Unable to open {website_name}. Error: {e}")
