from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("test.html")

@app.route("/therealshivgandhi")
def therealshivgandhi():
	return "Will the real Shiv Gandhi please stand up?"

if __name__ == "__main__":
	app.run(debug=True)