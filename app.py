from flask import Flask, render_template

app = Flask(__name__)

app_name = "My Application Name is : Azizah Glitch's"

#1 App Route di Flask
@app.route("/")
def Bombayah():
    return "<p>Bombayah!</p>"

#2 App Route di Flask
@app.route("/aplikasi")
def aplikasi():
    return "<p>Welcome to my application</p>"

#3 App Route dengan HTML
@app.route("/about/")
def about():
    return render_template("about.html")

#4 App Route dengan HTML with bostrapp
@app.route("/about-bostrapp/")
def about_bostrapp():
     return render_template('about_with_bootstrapp.html')

#5 App Route Dinamis
@app.route('/nama/<string:nama>')
def getnama(nama):
    return "nama anda adalah {}".format(nama)

#6 App Route ID
@app.route('/user/<int:user_id>')  # Hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"

#7 App Route Variabel Global
@app.route('/variabel-gloal/')
def variabel_global():
    return f"Welcome {app_name}"

#8 App Route Variabel Dictionary
@app.route('/data')
def data():
    user = {"name": "Azizah Glitch's", "age": 19, "city": "Makassar"}
    return render_template('data.html', user=user)

#9 App Route Menandai Admin dalam Daftar User
@app.route('/users')
def users():
    user_list = [
        {"name": "Ali", "role": "admin"},
        {"name": "Budi", "role": "user"},
        {"name": "Citra", "role": "admin"},
        {"name": "Dewi", "role": "user"},
    ]
    return render_template('users.html', users=user_list)
if __name__ == "__main__":
    app.run(debug=True)