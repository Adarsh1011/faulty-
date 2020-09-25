from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PredictorForm
from django.contrib.auth.decorators import login_required

import pandas as pd
import joblib 

reloadModel = joblib.load('./models/diabetes.pkl')

def predict(request):
    if request.method == 'POST':
        form = PredictorForm(request.POST)
        temp = {}
        temp['pregnancies']=request.POST.get('pregnancies')
        temp['glucose'] = request.POST.get('glucose')
        temp['bp'] = request.POST.get('bp')
        temp['skin_thickness'] = request.POST.get('skin_thickness')
        temp['insulin'] = request.POST.get('insulin')
        temp['bmi'] = request.POST.get('bmi')
        temp['dpf'] = request.POST.get('dpf')
        temp['age'] = request.POST.get('age')

        testdata = pd.DataFrame({'x': temp}).transpose()
        score_val = reloadModel.predict(testdata)[0]
        context={
            'score_val': score_val,
            'form': form
        }
        # messages.success(request, f'Your account has been created! Please log in')
        return render(request, 'predictor/diabetes.html', context)
    else:
        form = PredictorForm()
    return render(request, 'predictor/diabetes.html', {'form': form})

# def predictMPG(request):
#     context = {
#         'form': form,
#         'a': 'Hello World'
#     }
#     return render(request, 'predictor/diabetes.html', context)