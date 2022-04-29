
from __future__ import annotations
from curses import keyname
from unittest import result
from flask import redirect, url_for
from psutil import users
from sklearn import preprocessing
import random
import csv
import io
import os
import datetime
import calendar
import time
from array import array
import math
import numpy as np
from crypt import methods
from urllib import response
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import json
from bson.json_util import dumps
import pymongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename

import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
print(MONGO_URI)


app_no_random = Flask(__name__)
CORS(app_no_random)


APP_ROOT = os.path.dirname(os.path.relpath(__file__))
print("APP_ROOT", APP_ROOT)


try:

    client = pymongo.MongoClient(MONGO_URI)
    print("database connected!")
    db = client.clients
    print(db)

except Exception as ex:

    print("ERROR - Cannot connect to db!", str(ex))


@app_no_random.route("/", methods=["GET"])
def home():
    return "hello world! "


@app_no_random.route("/user", methods=["POST"])
def create_user():

    try:

        user = request.json
        db.users.insert_one(user)
        return json.dumps({"message": "user created!"})

    except Exception as ex:

        print("something went wrong!!", str(ex))


@app_no_random.route("/users", methods=["GET"])
def get_users():

    try:

        users = list(db.users.find())
        print("***********  --user deatails--  ************", users[-1])
        # exec("/testing.py")
        for user in users:
            user["_id"] = str(user["_id"])
        return jsonify(users)

    except Exception as ex:

        print("something went wrong!", str(ex))


@app_no_random.route('/user/<id>')
def user(id):

    user = db.users.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp


@app_no_random.route("/user/<id>/image", methods=["POST"])
def post_image(id):

    try:

        target = os.path.join(APP_ROOT, 'user_images')  # folder path
        if not os.path.isdir(target):
            os.mkdir(target)
        if request.method == 'POST':
            upload = request.files.get("image")  # image handle
            filename = upload.filename
            destination = "/".join([target, filename])
            print(destination)
            # image_result = image_function(destination)
            # print(image_result)
            upload.save(destination)
            db.users.find_one_and_update({'_id': ObjectId(id)}, {
                                         "$set": {'image': destination}})  # insert image path into database

            return jsonify({"message": "image uploaded successfully"})

    except Exception as ex:

        print("OOP! something went wrong", str(ex))


lastClient: str = None
lastSymptoms: list[str] = None
clientArray: list[int] = None

array1 = np.array([
"Coscienza",
"Informazione",
"Energia",
"Materia"
])

# array2 = np.array([
# "Coscienza",
# "Informazione",
# "Energia",
# "Materia"
# ])

combinations = np.array([i for i in array1])


@app_no_random.route("/results", methods=["GET"])
def results():
    max_values_list = []
    def sixteen(combi):
        print(combi)
        final = ""
        user = list(db.users.find())
        date1 = user[-1]["date"]
        symptom1 = user[-1]["symptoms"]
        
        print("symptoms------->",[symptom1])

        symptom2 = symptom1 == "" and "" or symptom1
        print("symptom2------->",[symptom2])
        print(date1)
        date2 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        print(date2)

        path1 = user[-1]["image"]
        print(path1)

        # def readimage(path):
        #     count = os.stat(path).st_size / 2
        #     with open(path, "rb") as f:
        #         return bytearray(f.read())

        # def image_function(path1):

        #     if(bool(path1) or os.path.exists(path1)):
        #         bytes = readimage(path1)
        #         bytes_string = str(bytes)
        #         if(len(bytes_string) > 14):
        #             hash_code = str((hash((bytes_string)[0:15])))
        #             print(hash_code)
        #             return hash_code
        #     else:
        #         print("there is no image path")

        # h = image_function(path1)
        # return str(h)

        def get_client_eval_list(birth_date, day_count, days_list):

            def days_in_year(year=datetime.datetime.now().year):
                return 365 + calendar.isleap(year)

            year_days_total = days_in_year()

            day_of_year = datetime.datetime.now().timetuple().tm_yday
            birth_date_string_integers = list(map(int, list(
                str(str(birth_date.day) + str(birth_date.month) + str(birth_date.year)))))

            def sum_function(lst, fit):
                day_count = 0
                day_list = []
                while(day_count <= fit):
                    for i in lst:
                        day_count += i
                        day_list.append(day_count)
                        if day_list[-1] <= 365:
                            day_count = day_list[-1]
                        # print(day_list)
                            below_list = [x for x in day_list if x <= day_of_year]
                        # print(below_list)
                            day = len(
                                below_list) > 0 and below_list[-1] or round(abs(b_date.day_of_year / 10))
                        # print(day)
                            first_day_of_year = datetime.date(
                                datetime.date.today().year, 1, 1)
                        # print(first_day_of_year).
                            date_var = first_day_of_year + \
                                datetime.timedelta(days=day-1)
                        # print(date_var.year*10000000000 + date_var.month * 100000000 +
                        # date_var.day * 1000000)
                        stamp = round(time.mktime(date_var.timetuple()))
                        string_of_final = str(stamp)

                return string_of_final

            return sum_function(birth_date_string_integers, year_days_total)


    # b_date = datetime.date(2022, 3, 23)
    # # print(days_list = get_client_eval_list(b_date, 0, []))
    # birth_date = datetime.date(1995, 3, 16)
        if(bool(date2)):
            final_string_date = get_client_eval_list(date2, 0, [])
        # print(final_string_date)

        else:
            final_string_date = get_client_eval_list(b_date, 0, [])
        # print(final_string_date)
        # final = h + final_string_date
        # return final
        dictionary = [
            (' ', 0),
            ('.', 0),
            (',', 0),
            (';', 0),
            (':', 0),
            ('_', 0),
            ('-', 0),
            ('+', 0),
            ('@', 0),
            ('*', 0),
            ('#', 0),
            ('/', 0),
            ('1', 1),
            ('2', -1),
            ('3', 2),
            ('4', -2),
            ('5', 3),
            ('6', -3),
            ('7', 4),
            ('8', -4),
            ('9', 5),
            ('0', -5),
            ('A', 6),
            ('À', 6),
            ('Á', 6),
            ('A', 6),
            ('Ã', 6),
            ('Ä', 6),
            ('Å', 6),
            ('Æ', 6),
            ('Ā', 6),
            ('Ă', 6),
            ('Ą', 6),
            ('B', -6),
            ('C', 7),
            ('Ç', 7),
            ('Ĉ', 7),
            ('Ċ', 7),
            ('Č', 7),
            ('D', -7),
            ('Ð', -7),
            ('E', 8),
            ('È', 8),
            ('É', 8),
            ('Ê', 8),
            ('Ë', 8),
            ('F', -8),
            ('G', 9),
            ('H', -9),
            ('I', 10),
            ('Ì', 10),
            ('Î', 10),
            ('Ï', 10),
            ('Í', 10),
            ('J', -10),
            ('K', 11),
            ('L', -11),
            ('M', 12),
            ('N', -12),
            ('Ñ', -12),
            ('O', 13),
            ('Ò', 13),
            ('Ó', 13),
            ('Ô', 13),
            ('Õ', 13),
            ('Ö', 13),
            ('Ø', 13),
            ('P', -13),
            ('Q', 14),
            ('R', -14),
            ('S', 15),
            ('T', -15),
            ('U', 16),
            ('Ù', 16),
            ('Ú', 16),
            ('Û', 16),
            ('Ü', 16),
            ('V', -16),
            ('W', 17),
            ('X', -17),
            ('Y', 18),
            ('Ý', 18),
            ('Z', -18),
            ('a', 6),
            ('à', 6),
            ('á', 6),
            ('â', 6),
            ('ä', 6),
            ('å', 6),
            ('æ', 6),
            ('ā', 6),
            ('ă', 6),
            ('ą', 6),
            ('b', -6),
            ('c', 7),
            ('ć', 7),
            ('ĉ', 7),
            ('ċ', 7),
            ('č', 7),
            ('d', -7),
            ('e', 8),
            ('é', 8),
            ('ê', 8),
            ('ë', 8),
            ('è', 8),
            ('f', -8),
            ('g', 9),
            ('h', -9),
            ('i', 10),
            ('ì', 10),
            ('í', 10),
            ('î', 10),
            ('ï', 10),
            ('j', -10),
            ('k', 11),
            ('l', -11),
            ('m', 12),
            ('n', -12),
            ('ñ', -12),
            ('o', 13),
            ('ò', 13),
            ('ó', 13),
            ('ô', 13),
            ('õ', 13),
            ('ö', 13),
            ('ø', 13),
            ('p', -13),
            ('q', 14),
            ('r', -14),
            ('s', 15),
            ('t', -15),
            ('u', 16),
            ('ù', 16),
            ('ú', 16),
            ('û', 16),
            ('ü', 16),
            ('v', -16),
            ('w', 17),
            ('x', -17),
            ('y', 18),
            ('ý', 18),
            ('ÿ', 18),
            ('z', -18)
        ]
        mapping = dict(dictionary)

        def mapping11(name, place, field, image):
            string_list = list(name + place + field + image)
            print(string_list)
            string_list = name + place + field + image
    # return string_list
    # print(string_list)
            mapping_values = [mapping[x] for x in string_list]
            strings = [str(x) for x in mapping_values]
            string = ''.join(strings)
            return string

        result_mapping = mapping11(user[-1]["name"] + user[-1]["surname"],
                                user[-1]["place"],  combi, user[-1]["image"])
        print("result map", result_mapping)

        final = result_mapping + final_string_date
        # print(result)
        # return final

        def function(final):

            MaxLen = 201
            mapping = dict(dictionary)

            def fillArray(text: str) -> list[int]:
                if text is None or text == '':
                    return []

                textLen = min(len(text), MaxLen)
                array = [mapping.get(c, 1) for c in text[:textLen]]

        # print(array)

        # repeat until length over MaxLen and return until MaxLen
                while len(array) < MaxLen:
                    array += array

                return array[:MaxLen]

            def buildClientArray(client: str, symptoms: list[str]) -> list[int]:
                if client is None or client == '':
                    return []

                array = fillArray(client)
                # filter empty
                symptoms = [s for s in symptoms if s is not None and s != '']
                symptomCount = len(symptoms)
                maxLength = len(array)
        # print("maxlength", maxLength)

                if symptomCount > 0:
                    symptomData = [fillArray(s) for s in symptoms]

                    for sArray in symptomData:
                        sz = len(sArray)
                        if maxLength > sz:
                            maxLength = sz
                        for i in range(0, maxLength):
                            array[i] = array[i] * sArray[i]

                arrayAbsMax = max([abs(item) for item in array])
                dArray = [round((18 * item) / arrayAbsMax) for item in array]
                print(dArray)
                print(len(dArray))
                return dArray

            def TextToArray(text: str) -> list[int]:
                if text is None or text == '':
                    return []
                textLen = len(text)
                arraySize = MaxLen
                result = []
                offset = 0
                step = 5
                while (len(result) < arraySize):
                    offset += 1 if offset < len(text) else 0
                    to_add = []
                    for i in range(-1 + offset, textLen, step):
                        to_add.append(mapping.get(text[i], 1))

                    result += to_add

                return result[:arraySize]
            # ml_value = user[-1]["mult"]  
            # ml_value2 = ml_value == "" and 0.3 or ml_value  

            def CalculateValue(client: str, remedy: str, symptoms: list[str], goal: list[str], onlyPositive: bool) -> float:
                global lastClient, lastSymptoms, clientArray
                result = 0
                if client is None or client == '':
                    return result

                if goal is None:
                    goal = "1010"

        # prevent re-calculation

                if not (client == lastClient and symptoms and lastSymptoms and symptoms == lastSymptoms):
                    lastClient = client
                    lastSymptoms = symptoms.copy()
                    clientArray = buildClientArray(client, symptoms)

                goalArray = TextToArray(goal)

                remedyArray = TextToArray(remedy)

                list_result = []
                result_fin = 0

                for i in range(1, MaxLen):

                    result += remedyArray[i] * goalArray[i] * clientArray[i]

                # result += goalArray[i] * clientArray[i]

                # new_res = 0
                # for i in range(1, MaxLen):
                # result_fin += remedyArray[i] * result
                # ist_result.append(result_fin)
                # new_res = list_result[-1]

                x = abs(result) == 5000 and 1 or 10000 / abs(result - 5000)

                y = abs(result) == 0 and 1 or 10000 / result
                result = x > y and -x or y

                if(onlyPositive and result < 0):
                    result = - result

                # double rnd = Rnd.GetDouble();
                # double stDivMax = isTAM ? 0.15 : 0.3;
                # if (rnd > stDivMax) rnd *= stDivMax;

                # double mult = (stDivMax - rnd + Rnd.GetDouble() * rnd);

                # mult = 0.3

                # rnd = random.random()
                # stDivMax = 0.3
                # if (rnd > stDivMax):
                #     rnd *= stDivMax
                # mult = stDivMax - rnd + random.random() * rnd
                mult = 0.3
                result *= mult

                return result

            # client = final
            # print(client)
            goal = str(user[-1]["goal"] == "" and "1010"or user[-1]["goal"])
            print("empty", user[-1]["goal"] == "" and "1010"or user[-1]["goal"], type(user[-1]["goal"]))
            print("Goal----->", goal)
            onlypositive = eval(user[-1]["onlypositive"])
            print("onlypositive:", onlypositive)

            result_test = []
            results = []
            flv_re = []
            with open('csv_file/db.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                sound = None
                for flvl in csv_reader:
                    flv_re.append(flvl)
                    if line_count == 0:
                        print('Calculating...')
                    else:
                        remedy = ''.join(flvl)
                        result = CalculateValue(client=final,
                                                remedy=remedy,
                                                symptoms=[symptom2],
                                                goal=goal,
                                                onlyPositive=onlypositive)
                # print('Result for %s is %f' % (' '.join(flvl), result))

                        result_test.append(result)
                        results.append((flvl, result))

                    line_count += 1

            max_value = max(result_test)
            max_values_list.append((combi,max_value))
            min_value = min(result_test)
            print("max_value", max_value)
            max_abs = abs(max(max_value, -min_value))
            # print("abs max:", max_abs)

            # L=[1,2,3]
            # M=[4,5,6]
            # for a,b in zip(L,M):
            #     print(a,b)
            li = []
            abs_li = []
            def percent():

                for i in result_test[:]:
                    normalized = round((i/max_abs) * 100, 1)
                    li.append(normalized)
                    abs_li.append(abs(normalized))
                    i = i + 1
                # print("print LI:", li)

            percent()

            # print("print:", flv_re)
            final_list_results = []
            for a, b, c in zip(flv_re[1:], li, abs_li ):

                results_set = a,b,c 
                final_list_results.append(results_set)
                # print("*************** flvl and list of results **************:", results_set)

            final_list_results = sorted(final_list_results, key=lambda x: x[2], reverse=True)
            # print("*************** flvl and list of results **************:",final_list_results)
            # # print(max_abs)
            # # results_perc = [100 * x / max_abs for x in result_test]

            # # results_perc = [x / max_abs for x in results]
            # # print("Result_perc", results_perc)

            # # for res in results:
            # # result = res / max_abs

            # print("Max", max_value)
            # print("Min", min_value)
            # print("Results", result_test)

            # print('Processed {%d} lines.' % (line_count))

            # print('Results are displayed in ascending order.')
            # results = sorted(results, key=lambda x: x[1])

            # for res in results:

            #     print('Result for %s is %f' % (' '.join(res[0]), res[1]))

            return final_list_results
        rel = function(final)
        # print(rel)
        return json.dumps(rel)
    comni_list_results = []
    for combi in combinations:

        print(combi)
        fi = sixteen(combi)
        comni_list_results.append(fi)
    # print("comni_list-------->", comni_list_results)
    return json.dumps((max_values_list,comni_list_results))
    # return json.dumps(max_values_list)

if __name__ == "__main__":
    app_no_random.run(host='0.0.0.0', debug=False, port=int(os.environ.get("PORT", 5000)))
