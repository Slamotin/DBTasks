# -*- coding: utf-8 -*-
import argparse
import bson
from pymongo import MongoClient

parser = argparse.ArgumentParser(description='Process ...')

parser.add_argument('-m', "--manufacture", action = 'store', help = 'выводить число автомобилей и список всех автомобилей заданного производителя по команде')
parser.add_argument('-l', "--later_then", action='store', help = 'выводить все автомобили, выпущенные не раньше заданного года')
parser.add_argument('-o', '--optionsByID', action='store', help = 'выводить список опций по ID автомобиля')
        
#пример работы, ключ с 2мя тире и значение, если указано 2 ключа
#должно сработать оба(но не в одном запросе) 
#если они в той последовательности иначе сработает только один
#если удалить значение внутри скобок ниже, то будет работать 
#указание ключей через консольный запуск
#т.е. python имя_этого_файла --manufacture Acura
#иначе ключи можно указывать в квадратных скобках ниже как в примере
args = parser.parse_args(["--optionsByID", "604516897b852d414404c4c4"]) 

client=MongoClient('mongodb://localhost:27017/')
db = client['cars']
series_collection = db['cars']

if args.manufacture:
    result = series_collection.find({'manufacture':args.manufacture})
    print (result.count())
    for r in result:
        print(r)
if args.later_then:
    result = series_collection.find({'year':{'$gte':int(args.later_then)}})
    for r in result:
        print(r)
if args.optionsByID:
    result = series_collection.find({'_id':bson.objectid.ObjectId(args.optionsByID)},{'car_options': 1, '_id': 0})
    for r in result:
        print(r)

