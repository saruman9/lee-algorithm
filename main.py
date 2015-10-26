#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Lee algorithm
# Лицензия: GNU GPL version 3.
__license__ = 'GPLv3'
__author__ = __maintainer__ = 'Alex Sarum'
__email__ = 'rum.274.4@gmail.com'


import sys
import os


def wave(graph, node_start, node_goal):
    """
    Находит наикратчайший путь между двумя заданными вершинами.
    :param graph: Граф, в котором проводится поиск
    :type graph: dict
    :param node_start: Наименование стартовой вершины
    :type node_start: str
    :param node_goal: Наименование конечной вершины
    :type node_goal: str
    """
    for node in graph:
        graph[node] = {"nodes": graph[node], "wave": -1}

    OldFront, NewFront, time = list(node_start), list(), 0
    graph[node_start]["wave"] = 0

    return graph


def input_source():
    """
    Считывает файл и возвращает словарь вида: "вершина_0: вершина_1, вершина_2, вершина_3...",
    где вершина_1, вершина_2, вершина_3 - смежные вершины вершины_0.
    """
    graph = dict()
    with open(sys.argv[1]) as file:
        for line in file:
            node1, node2 = line.split()
            if node1 not in graph:
                graph[node1] = set(node2)
            else:
                graph[node1].add(node2)
            if node2 not in graph:
                graph[node2] = set(node1)
            else:
                graph[node2].add(node1)


    return graph


def main():
    """
    Главная функция
    """
    verbose = False
    if "-v" in sys.argv or "--verbose" in sys.argv:
        sys.argv.pop()
        verbose = True

    if len(sys.argv) < 4:
        print("Использовать: {} SOURCE_FILE START_NODE GOAL_NODE\n-v, --verbose - для дополнительного вывода".format(sys.argv[0]))
        os._exit(2)


    input_graph = input_source()
    wave_graph = wave(input_graph.copy(), sys.argv[2], sys.argv[3])

    if verbose:
        for node in sorted(input_graph):
            print("{}: {}".format(node, input_graph[node]))
        print()
        for node in sorted(wave_graph):
            print("{}: nodes: {}\n\twave: {}".format(node, wave_graph[node]["nodes"], wave_graph[node]["wave"]))


if __name__ == "__main__":
    main()
