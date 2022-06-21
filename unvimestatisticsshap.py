# instalamos las libreias que vamios a utilizar por ahora


import autosklearn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import shap
import warnings
warnings.filterwarnings('ignore')
# import mlxtend
from autosklearn.classification import AutoSklearnClassifier
from sklearn.model_selection import train_test_split
alumnos = pd.read_csv('unvime2020y2021v1.csv', encoding='ISO-8859-1', sep =',')
X = alumnos.drop("regular", axis=1)
y = alumnos.regular
import sklearn.metrics
from autosklearn.metrics import balanced_accuracy, precision, recall, f1


def error(solution, prediction):
    # custom function defining error
    return np.mean(solution != prediction)


def get_metric_result(cv_results):
    results = pd.DataFrame.from_dict(cv_results)
    results = results[results['status'] == "Success"]
    cols = ['rank_test_scores', 'param_classifier:__choice__', 'mean_test_score']
    cols.extend([key for key in cv_results.keys() if key.startswith('metric_')])
    return results[cols]
error_rate = autosklearn.metrics.make_scorer(
    name='custom_error',
    score_func=error,
    optimum=0,
    greater_is_better=False,
    needs_proba=False,
    needs_threshold=False
    )
# Dividimos los datos en entrenamiento y prueba
from sklearn.model_selection import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y,random_state=0)

# Definimos el modelo de autoML, especificamos el tiempo total de ejecuciòn y el tiempo por modelo
AutoMLmodel = AutoSklearnClassifier(time_left_for_this_task=100,
                              per_run_time_limit=60,
                              seed=1,
                              initial_configurations_via_metalearning=0,
                              ensemble_size=25, 
                              tmp_folder='/tmp/autosklearn_resampling_example_tmp29',
                              disable_evaluator_output=False,
                              resampling_strategy='cv',
                              resampling_strategy_arguments={'folds': 5},                             
                              scoring_functions=[balanced_accuracy, precision, recall, f1, error_rate],
                              #include = {'classifier': ["extra_trees","random_forest"]}
                              )

# Entrenamos el modelo con los datos Xtrain y ytrain
AutoMLmodel.fit(Xtrain, ytrain)

# Presentamos las estadísticas de la ejecución
print(AutoMLmodel.sprint_statistics())

AutoMLmodel.score(Xtest,ytest)

predictions = AutoMLmodel.predict(Xtest)
print("Accuracy score", sklearn.metrics.accuracy_score(ytest, predictions))

print("#" * 80)
print("Metric results")
print(get_metric_result(AutoMLmodel.cv_results_).to_string(index=False))

#from mlxtend.plotting import plot_confusion_matrix
#from sklearn.metrics import confusion_matrix

#ypred = AutoMLmodel.predict(Xtest)
#matriz = confusion_matrix(ytest,ypred)

#plot_confusion_matrix(conf_mat=matriz, figsize=(6,6), show_normed=False)
#plt.tight_layout()
explainer = shap.KernelExplainer(AutoMLmodel.predict_proba, shap.sample(Xtrain, 1))
shap_values = explainer.shap_values(X)
shap.summary_plot(shap_values, features=X, feature_names=X.columns, plot_type='bar')

