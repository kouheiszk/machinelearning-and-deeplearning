#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import pandas
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import cross_validation

linear = LinearRegression()


def main():
    csv = pandas.read_csv(os.path.dirname(os.path.abspath(__file__)) + "/../data/data.csv", sep=",")
    # csv = csv.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
    csv.head()

    data = csv.drop("TARGET", axis=1).as_matrix()
    teacher = csv['TARGET'].as_matrix()

    linear.fit(data, teacher)

    print(pandas.DataFrame({"ラベル": csv.drop("TARGET", axis=1).columns,
                            "係数": np.abs(linear.coef_)}))
    print(pandas.DataFrame({"ラベル": csv.drop("TARGET", axis=1).columns,
                            "係数": np.abs(linear.coef_)}).sort_values(by="係数"))
    print("誤差: {}".format(linear.intercept_))

    scores = cross_validation.cross_val_score(linear, data, teacher, cv=10)
    print(sum(scores) / 10)
    # print(np.mean(scores))


if __name__ == "__main__":
    main()
