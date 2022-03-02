from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

@app.route("/")
@app.route("/home", methods=['POST', 'GET'])
def home():
    return render_template("/about.html")


@app.route("/about", methods = ['POST', 'GET'])
def about():
    output = request.form.to_dict()
    print(output)
    name = output["name"]
    print(name)

    return render_template("/about.html", name=name)

if __name__ == "__main__":
    app.debug = True
    app.run()
