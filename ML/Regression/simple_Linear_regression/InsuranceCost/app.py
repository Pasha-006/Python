from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the form
@app.route("/", methods=["GET", "POST"])
def insurance_form():
    
    return render_template("form.html")
@app.route("/submit",method=['GET','POST'])
def submit():
    if request.method == "POST":
            # Retrieve form data
            age = request.form.get("age")
            sex = request.form.get("sex")
            bmi = request.form.get("bmi")
            children = request.form.get("children")
            smoker = request.form.get("smoker")
            region = request.form.get("region")
            charges = request.form.get("charges")
            
            # Display the values (you can process or store them as needed)
            {sex}

if __name__ == "__main__":
    app.run(debug=True)
