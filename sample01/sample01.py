#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import os
import random

ANSWER_GEN_MAX = 100000


def read_csv(data=False, teacher=False):
    result = []
    with open(os.path.dirname(os.path.abspath(__file__)) + "/data.csv", "r") as f:
        reader = csv.reader(f)
        _ = next(reader)

        for row in reader:
            number_row = [n for n in map(int, row)]
            if data and teacher:
                result.append(number_row)
            elif data:
                result.append(number_row[:len(number_row) - 1])
            elif teacher:
                result.append(number_row[-1:][0])

    return result


def calc_score(data, teacher, answer):
    score = 0

    for i in range(len(data)):
        data_size = len(data[i])
        point = 0
        for j in range(len(data[i])):
            if answer[j] == 2 or answer[j] == data[i][j]:
                point += 1

        if point == data_size and teacher[i] == 1:
            score += 1
        elif point != data_size and teacher[i] == 0:
            score += 1

    return score


def main():
    data = read_csv(data=True)
    teacher = read_csv(teacher=True)

    col_num = len(data[0])

    best_score = 0
    best_answer = [2, ] * col_num

    for i in range(ANSWER_GEN_MAX):
        # 2はワイルドカードを表している
        answer = [random.randint(0, 2) for _ in range(col_num)]
        # スコアを計算
        score = calc_score(data, teacher, answer)

        if score > best_score:
            best_score = score
            best_answer = answer

            print("{} score={}".format(answer, score))

    print("最適解:")
    print("{} score={}".format(best_answer, best_score))


if __name__ == "__main__":
    main()
