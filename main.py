from wtforms import Form, StringField, SubmitField
from find_temperature import Temperature
from calorie_calculator import CalorieCalculator
from flask import Flask, render_template, request
from flask.views import MethodView

app = Flask(__name__)


class MainPage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()

        return render_template('calories_form_page.html',
                               caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(country=calories_form.country.data,
                                  city=calories_form.city.data).get()

        calorie = CalorieCalculator(weight=float(calories_form.weight.data),
                          height=float(calories_form.height.data),
                          age=float(calories_form.age.data),
                          temperature=temperature)

        calories = calorie.calculate_calories()

        return render_template('calories_form_page.html',
                               caloriesform=calories_form,
                               calories=calories,
                               result=True)


class CaloriesForm(Form):
    weight = StringField("Weight: ", default=90)
    height = StringField("Height: ", default=190)
    age = StringField("Age: ", default=42)
    country = StringField("Country: ", default='USA')
    city = StringField("City: ", default="San Francisco")
    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=MainPage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)
