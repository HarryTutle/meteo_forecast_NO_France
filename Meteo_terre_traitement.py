# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 18:16:02 2021

@author: Utilisateur
"""


""" On importe les packages utiles pour nous. """

from datetime import datetime
import numpy as np
import pandas as pd

""" cette fonction change les directions du vent en catégories."""

def cap(var):  
    
    if (var>337.5) and (var<=22.5):
        var=0
    elif (var>22.5) and (var<=67.5):
        var=45
    elif (var>67.5) and (var<=112.5):
        var=90
    elif (var>112.5) and (var<=157.5):
        var=135
    elif (var>157.5) and (var<=202.5):
        var=180
    elif (var>202.5) and (var<=247.5):
        var=225
    elif (var>247.5) and (var<=292.5):
        var=270
    else:
        var=315
        
    return var


""" celle fonction change la force du vent en catégories."""

def vent(var):   # change la force du vent en noeuds et en 7 catégories de force de vent.
    var=var*3600//1852
    if (var>=0) and (var<5):
        var=1
    
    elif (var>=5) and (var<10):
        var=2
        
    elif (var>=10) and (var<15):
        var=3
        
    elif (var>=15) and (var<20):
        var=4
        
    elif (var>=20) and (var<25):
        var=5
        
    elif (var>=25) and (var<30):
        var=6
        
    else:
        var=7
        
    return var


""" cette fonction change les précipitations en catégories."""

def flotte(var):
    
    if var==0:
        var=0
        
    elif var!=0:
        var=1
        
    return var

""" fonction pour changer les temperatures en catégories."""
        
def glagla(var):
    var=var-273.15
    if var<0:
        var=0
        
    elif (var>=0) and (var<5):
        var=1
        
    elif (var>=5) and (var<10):
        var=2
        
    elif (var>=10) and (var<15):
        var=3
        
    elif (var>=15) and (var<20):
        var=4
        
    elif (var>=20) and (var<25):
        var=5
        
    elif (var>=25) and (var<30):
        var=6
        
    elif var>=30:
        var=7
        
    return var

""" Cette classe permet de modifier le fichier d'origine pour avoir des données prêtes pour sikilearn. """


class Meteo_Data_View:
    
    
    def __init__(self, name, heures=1, jours=1, var_corbeille=[], vue=12, cible='direction'):
        self.name=name
        numb_vars=7
        stations_meteo=[]
        stations_meteo_2=[]
        stations_meteo_3=[]
        
        data_good_shape=[]
        target=[]
        compteur=[]
        
        indexage_heures=list(pd.date_range('2016-01-01 00:00:00', '2018-12-31 23:00:00', freq=str(heures)+'h'))
        time_heures=pd.DataFrame({'temps': indexage_heures}) 
        time_heures=time_heures.set_index('temps') 
        
        indexage_jours=list(pd.date_range('2016-01-01', '2018-12-31', freq='d'))
        time_jours=pd.DataFrame({'temps': indexage_jours})
        
        if cible=='direction':
            ci=3
        elif cible=='force':
            ci=4
        elif cible=='pluie':
            ci=5
        elif cible=='température':
            ci=8
    
        for station in self.name['number_sta']:
            
           station_data=self.name.loc[self.name['number_sta']==station]
           station_data=station_data.sort_values(['date'],ascending=True)
           station_data=station_data.set_index('date')
           station_data.index=pd.to_datetime(station_data.index)
           station_data=station_data.resample(str(heures)+'H').mean()
           station_data=time_heures.join(station_data, how='outer')
           station_data["dd"]=station_data["dd"].map(lambda x: cap(x))
              
           
            
           station_data['number_sta']=station_data['number_sta'].apply(lambda x: int(x) if np.isnan(x)==False else x)
           station_data['lat']=station_data['lat'].apply(lambda x: int(x*100) if np.isnan(x)==False else x)
           station_data['lon']=station_data['lon'].apply(lambda x:int(x*100) if np.isnan(x)==False else x)
           station_data['height_sta']=station_data['height_sta'].apply(lambda x:int(x) if np.isnan(x)==False else x)
           station_data['dd']=station_data['dd'].apply(lambda x:int(x) if np.isnan(x)==False else x)
           station_data['ff']=station_data['ff'].apply(lambda x:int(round(x)) if np.isnan(x)==False else x)
           station_data['hu']=station_data['hu'].apply(lambda x:int(round(x)) if np.isnan(x)==False else x)
           station_data['precip']=station_data['precip'].apply(lambda x:int(round(x)) if np.isnan(x)==False else x)
           station_data['psl']=station_data['psl'].apply(lambda x:int(x/100) if np.isnan(x)==False else x)
           station_data['td']=station_data['td'].apply(lambda x:int(round(x)) if np.isnan(x)==False else x)
           station_data['t']=station_data['t'].apply(lambda x:int(round(x)) if np.isnan(x)==False else x)
           
           if station_data['number_sta'].mean() not in compteur:
               
              stations_meteo.append(station_data)
           
           else: break
       
           compteur.append(station_data['number_sta'].mean())
        
                
        for station_data in stations_meteo:
            
            station_data=station_data.dropna(axis=1, how='all')
            station_data=station_data.dropna(axis=0, how='any')
            station_data=time_heures.join(station_data, how='outer')
            
            if (station_data.shape[1]==11):
                
                stations_meteo_2.append(station_data)
                
        for station_data in stations_meteo_2:
            
            liste_heures=[station_data[station_data.index.hour==i] for i in range(0,24,heures)]
            station_data=np.concatenate(liste_heures,axis=1)
            station_data=pd.DataFrame(station_data)
            station_data.columns=list(np.arange(0, station_data.shape[1]))
            
            
            station_data=station_data.drop([0+(i*11) for i in range(int(24/heures))],axis=1) 
            station_data=station_data.drop([12+(i*11) for i in range(int(23/heures))],axis=1) 
            station_data=station_data.drop([13+(i*11) for i in range(int(23/heures))],axis=1) 
            station_data=station_data.drop([14+(i*11) for i in range(int(23/heures))],axis=1) 
            
            station_data=time_jours.join(station_data)
            station_data=station_data.set_index('temps')
            station_data['mois']=station_data.index.month
            
            
            liste_jours=[station_data[i:-jours+i:jours] for i in range(jours)]      
            station_data=np.concatenate(liste_jours, axis=1)
            station_data=pd.DataFrame(station_data)
            
            
            
            
                
            lat=[(((24/heures)*7+4)*n) for n in range(1,jours)]
            lon=[(((24/heures)*7+4)*n)+1 for n in range(1,jours)]
            hei=[(((24/heures)*7+4)*n)+2 for n in range(1,jours)]
            mon=[((24/heures)*7+4)*n-1 for n in range(1,jours)]
                
            station_data=station_data.drop(lat, axis=1)
            station_data=station_data.drop(lon, axis=1)
            station_data=station_data.drop(hei, axis=1)
            station_data=station_data.drop(mon, axis=1)
                
            
            
            station_data.columns=list(np.arange(0, station_data.shape[1]))
            
            liste_decalage_jours_station=[]
            for jour in range(jours):
                station_data=station_data.iloc[jour::jours]
                liste_decalage_jours_station.append(station_data)
                
            
            for station_data in liste_decalage_jours_station:
            
            
              liste_decalage_heures_station=[]
              for decalage in range(int(24/heures)):
                  part_1=station_data.iloc[0:(station_data.shape[0]-1),0:3].reset_index(drop=True)
                  part_2=station_data.iloc[0:(station_data.shape[0]-1),3+numb_vars*decalage:-1].reset_index(drop=True)
                  part_3=station_data.iloc[1:(station_data.shape[0]),3:3+numb_vars*decalage].reset_index(drop=True)
                  part_4=station_data.iloc[1:(station_data.shape[0]),-1].reset_index(drop=True)
                  total=part_1.join(part_2)
                  total=total.join(part_3)
                  total=total.join(part_4)
                  total.columns=list(np.arange(0,total.shape[1]))
                  liste_decalage_heures_station.append(total)
                
              stations_meteo_3.append(liste_decalage_heures_station)
            
      
        for station_data in stations_meteo_3:
            
            for station_decalage in station_data:
                
                station_decalage=station_decalage.reset_index(drop=True)
                                  
                for val in range(station_decalage.shape[0]-1):
                        
                    row=station_decalage.iloc[val,:]
                    row2=station_decalage.iloc[val+1,numb_vars*heures*(jours-1)+ci+numb_vars*vue]
                    
                    
                    if (np.isnan(row).sum()==0) and (np.isnan(row2).sum()==0):
                        
                        data_good_shape.append(row)
                        target.append(row2)
                            
                        
                            
                    
                    else:
                        continue
        
        data_good_shape=pd.DataFrame(data_good_shape)
        
        for name in var_corbeille:
                              
                if name.find("force")!=-1:
                    data_good_shape=data_good_shape.drop([4+i*numb_vars for i in range(0,jours*24)], axis=1)
                
                elif name.find("direction")!=-1:
                    data_good_shape=data_good_shape.drop([3+i*numb_vars for i in range(0,jours*24)], axis=1)
                  
                elif name.find("pluie")!=-1:
                    data_good_shape=data_good_shape.drop([5+i*numb_vars for i in range(0, jours*24)], axis=1)
                    
                elif name.find("humidité")!=-1:
                    data_good_shape=data_good_shape.drop([6+i*numb_vars for i in range(0,jours*24)], axis=1)
                    
                elif name.find("point_rosée")!=-1:
                    data_good_shape=data_good_shape.drop([7+i*numb_vars for i in range(0,jours*24)], axis=1)
                    
                elif name.find("température")!=-1:
                    data_good_shape=data_good_shape.drop([8+i*numb_vars for i in range(0,jours*24)], axis=1)
                    
                elif name.find("pression")!=-1:
                    data_good_shape=data_good_shape.drop([9+i*numb_vars for i in range(0,jours*24)], axis=1)
                    
                elif name.find("latitude")!=-1:
                    data_good_shape=data_good_shape.drop([0], axis=1)
                    
                elif name.find("longitude")!=-1:
                    data_good_shape=data_good_shape.drop([1], axis=1)
                    
                elif name.find("temps")!=-1:
                    data_good_shape=data_good_shape.drop([3+24*numb_vars*jours], axis=1)
        
                elif name.find("altitude")!=-1:
                    data_good_shape=data_good_shape.drop([2], axis=1)
        
            
                    
        target=np.transpose(target) 
        data_good_shape=np.array(data_good_shape)
        self.debug=stations_meteo_3
        target_2=[]
        if cible=='force':
            for val in target:
                val2=vent(val)
                target_2.append(val2)
            target=target_2
        elif cible=='pluie':
            for val in target:
                val2=flotte(val)
                target_2.append(val2)
            target=target_2
            
        elif cible=='température':
            for val in target:
                val2=glagla(val)
                target_2.append(val2)
            target=target_2
        
        
        target=np.array(target)
        target=target.astype('int32')
        data_good_shape=data_good_shape.astype('int32')
        
       
        
        
        self.dimensions=data_good_shape.shape
        self.target=target   
        self.data_good_shape=data_good_shape
        
        
        
        
       
      
    
    
    
    
    
    