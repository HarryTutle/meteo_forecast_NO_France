# meteo_forecast_NO_France
 a package (Meteo_data_shape_weather) to store Meteo-France weather data (findable in open office in kaggle) in a good shape for sklearn. Inside this package you have a class (Meteo_data_view) which use five parameters:
 
 -name, this is the name of our csv meteo-france file. It can be just 2016 year, 2016 and 2017 or all the three years available.
 
 -hours, default it's one hour but you can change it for 2, 3...24 hours. One hour means that your 
 dataset will keep all variables (humidity, temperature, wind speed...) per hour. 2 means per 2 hours etc...
 
 -days, default it's 1. It means that for our dataset one sample will include one day only. If you want 3 days in a sample you will have to fix it on 3.
 
 -dropping, default an empty list. In that list you can write variables you want to get rid of if you need a smaller dataset. But if you follow this way you will maybe decrease your model's accuracy.
 
 -view, default 12. This number is the hours in the future we want for our forecast model.If you need to predict in 6 hours, you will have to write 6.
 
 
 this class as methods:
 
 -object.stations_number: give stations number in our dataset.
 
 -object.dimensions: give our dataset's shape.
 
 -object.target_direction: give our data targets for sklearn supervised training. Here it's for wind direction prediction.
 
 -object.target_force: the same but for wind speed.
 
 -object.target_temperature: idem for tempearature.
 
 -object.target_pluie: the same but for the precipitations.
 
 -object.data_good_shape: this one give our transformed dataset ready for machine learning training.
 
 
 I have added up a file (using exemple) if yoy want to use it. Enjoy !
 
 
 Currently the best results i had is when i use all the 3 years, 3 days per sample, hours=1, no dropping with RandomForestClassifier machine learning model (this package store data for classification, not regression). With no max_depth, max_feature=default and n_estimators=300 you will find:
 
 -Direction: around 69 % on the score test.
 -Force: around 73 % on the score test.
 -Temperature: around 88% on the score test.
 -Rain: around 99% (but i'm not really confident on it...) 
