from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def check_redirects(url):
    redirects = []

    try:
        response = requests.get(url, allow_redirects=True, timeout=10)

        for resp in response.history:
            redirects.append({
                "url": resp.url,
                "status": resp.status_code
            })

        redirects.append({
            "url": response.url,
            "status": response.status_code
        })

    except Exception as e:
        redirects.append({"url": "Error", "status": str(e)})

    return redirects


@app.route("/", methods=["GET", "POST"])
def index():
    redirects = None
    warning = False

    if request.method == "POST":
        url = request.form["url"]
        redirects = check_redirects(url)

        if len(redirects) - 1 > 3:
            warning = True

    return render_template("index.html", redirects=redirects, warning=warning)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)