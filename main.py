#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Lee algorithm
# Лицензия: GNU GPL version 3.
import sys
import os

__license__ = 'GPLv3'
__author__ = __maintainer__ = 'Alex Sarum'
__email__ = 'rum.274.4@gmail.com'

VERBOSE = 0


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

    global VERBOSE

    for node in graph:
        graph[node] = {"nodes": graph[node], "wave": -1, "path": list()}

    old_front, new_front, time = [node_start, ], list(), 0
    graph[node_start]["wave"], graph[node_start]["path"] = 0, [node_start, ]

    while True:
        # Просмотр волны "старого фронта"
        for node_wave in old_front:
            # Просмотр смежных вершин
            for node_adjacent in graph[node_wave]["nodes"]:
                if graph[node_adjacent]["wave"] == -1:
                    graph[node_adjacent]["wave"] = time + 1
                    # Запоминаем путь каждой вершины
                    graph[node_adjacent]["path"] += graph[node_wave]["path"]
                    graph[node_adjacent]["path"].append(node_adjacent)
                    new_front.append(node_adjacent)
                if VERBOSE == 2:
                    print(node_adjacent, graph[node_adjacent]["wave"], new_front)

        assert new_front, "Пути от вершины {} до вершины {} не существует".format(node_start, node_goal)

        if VERBOSE:
            print()
            for node in sorted(graph):
                print("{}: nodes: {}\n\twave: {},\n\tpath: {}".format(
                    node, graph[node]["nodes"], graph[node]["wave"], graph[node]["path"]))

        if node_goal in new_front:
            return graph

        old_front, new_front = new_front, list()
        time += 1


def input_source():
    """
    Считывает файл и возвращает словарь вида: "вершина_0: вершина_1, вершина_2, вершина_3...",
    где вершина_1, вершина_2, вершина_3 - смежные вершины вершины_0.
    """

    global VERBOSE
    graph = dict()
    with open(sys.argv[1]) as file:
        for line in file:
            node1, node2 = line.split()
            if node1 not in graph:
                graph[node1] = set()
                graph[node1].add(node2)
            else:
                graph[node1].add(node2)
            if node2 not in graph:
                graph[node2] = set()
                graph[node2].add(node1)
            else:
                graph[node2].add(node1)

        if VERBOSE:
            for node in sorted(graph):
                print("{}: {}".format(node, graph[node]))
            print()

    return graph


def main():
    """
    Главная функция
    """

    global VERBOSE
    if "-v" in sys.argv:
        sys.argv.pop()
        VERBOSE = 1
    elif "-vv" in sys.argv:
        sys.argv.pop()
        VERBOSE = 2

    if len(sys.argv) < 4:
        print("Использовать: {} SOURCE_FILE(исходный файл) START_NODE(начальная вершина)"
              " GOAL_NODE(конечная вершина)\n-v, --verbose - для дополнительного вывода".format(
            sys.argv[0]))
        os._exit(2)

    input_graph = input_source()
    wave_graph = wave(input_graph.copy(), sys.argv[2], sys.argv[3])
    print(wave_graph[sys.argv[3]]["path"])


if __name__ == "__main__":
    main()
