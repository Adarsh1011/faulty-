from django import forms

class PredictorForm(forms.Form):
    pregnancies = forms.IntegerField(label='Number of Pregnancies')
    glucose = forms.IntegerField(label='Plasma glucose concentration a 2 hours in an oral glucose tolerance test')
    bp = forms.IntegerField(label='BloodPressure(mm Hg)')
    skin_thickness = forms.IntegerField(label='SkinThickness(mm)')
    insulin = forms.IntegerField(label='Insulin(mu U/ml)')
    bmi = forms.FloatField(label='BMI(weight in kg/(height in m)^2)')
    dpf = forms.FloatField(label='DiabetesPedigreeFunction')
    age = forms.IntegerField(label='Age', initial=30)

    class Meta:
        fields = ["pregnancies", 'glucose', 'bp', 'skin_thickness', 'insulin', 'bmi', 'dpf', 'age']