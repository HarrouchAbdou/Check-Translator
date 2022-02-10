import re
import math
import time

import translators as ts
from collections import Counter


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    word = re.compile(r'\w+')
    words = word.findall(text)
    return Counter(words)


def get_result(content_a, content_b):
    text1 = content_a
    text2 = content_b

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine_result = get_cosine(vector1, vector2)
    return cosine_result


def SearchByCos(name_1, name_2):
    file_2 = open(name_2, "r", encoding="utf-8")
    outputfile_2 = file_2.readlines()
    file_Result = open("Francais_Translate.txt", 'w')
    i=0
    for sentence in outputfile_2:
        print(i+1)
        i = i+1
        translatedSentence = ts.google(sentence, to_language='fr')
        accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â','-','_',"'",',']
        sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a',' ',' ',' ',' ']
        j = 0
        while j < len(accent):
            translatedSentence = translatedSentence.replace(accent[j], sans_accent[j])
            j += 1
        file_Result.write(translatedSentence + '\n')
    print("Fin de traduction")
    file_2.close()
    file_Result.close()
    time.sleep(5)

    file_1 = open(name_1, "r")
    outputfile_1 = file_1.readlines()
    file_3 = open("Francais_Translate.txt", "r")
    outputfile_3 = file_3.readlines()

    longueur = len(outputfile_3)
    resultatFinalForIndexs = []
    list_indexation = []
    list_Resultat_Total = []
    Resultat = []
    for i in range(longueur):
        cos = 0
        index = 0
        list_Resultat_line = []
        for j in range(longueur):
            value = get_result(outputfile_1[i], outputfile_3[j])
            list_Resultat_line.append(value)
            if value > cos:
                cos = value
                index = j
            else:
                continue
        list_indexation.append([i + 1, index + 1])

        list_Resultat_Total.append(list_Resultat_line)

    for element in range(0, len(list_Resultat_Total)):
        A = [element]
        list_max = max3(list_Resultat_Total[element])
        indexForlist_max = []
        for u in list_max:
            indexForlist_max.append(list_Resultat_Total[element].index(u))
        A.append(indexForlist_max)
        resultatFinalForIndexs.append(A)

    for x in resultatFinalForIndexs:
        fr = outputfile_2[x[0]].rstrip("\n")
        frTr1 = outputfile_3[x[1][0]].rstrip("\n")
        frTr2 = outputfile_3[x[1][1]].rstrip("\n")
        frTr3 = outputfile_3[x[1][2]].rstrip("\n")
        to_post = [fr, [frTr1, frTr2, frTr3]]
        Resultat.append(to_post)

    file_1.close()
    file_3.close()
    return Resultat


def max3(liste):
    listCopy = liste.copy()
    listCopy.sort(reverse=True)
    resultat = listCopy[:3]
    return resultat

