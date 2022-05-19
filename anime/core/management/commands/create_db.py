"""
Command
"""

import csv
from core import models
from django.core.management.base import BaseCommand

def searchAndReturnAnimes():
    with open('anime_db.csv', 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)

        id = 0; type = 1; title = 2; synopsis = 3; score = 4; eps = 5; scored_by = 6; rank = 7; pop = 8; url = 9

        animes = {}
        for line in csv_reader:
                animes[line[id]] = line[type], line[title], line[synopsis], line[score], line[eps], line[scored_by], line[rank], line[pop], line[url]

        return animes


class Command(BaseCommand):
    help = 'Initialize data'

    def handle(self, *args, **params):
        """
        Entry point for the command.
        """
        #id = 0; type = 1; title = 2; synopsis = 3; score = 4; eps = 5; scored_by = 6; rank = 7; pop = 8; url = 9
        data = searchAndReturnAnimes()
        for i in data:
            # print(i)
            # print(data[i][0])
            # print(data[i][1])
            # print(data[i][2])
            # print(data[i][3])
            # print(data[i][4])
            # print(data[i][5])
            # print(data[i][6])
            # print(data[i][7])
            # print(data[i][8])
            # break
            if data[i][3] == '':
                episode = 0
            else:
                episode = data[i][3]

            if data[i][6] == '':
                rank = 0
            else:
                rank = data[i][6]

            if data[i][4] == '':
                score = 0
            else:
                score = data[i][4]

            if data[i][5] == '':
                scored_by = 0
            else:
                scored_by = data[i][5]


            models.Anime.objects.create(anime_id = int(i),
                                        type = data[i][0],
                                        title = data[i][1],
                                        synopsis = data[i][2],
                                        score = float(score),
                                        episodes = int(episode),
                                        scored_by = int(scored_by),
                                        rank = int(rank),
                                        popularity = int(data[i][7]),
                                        url = data[i][8]
                                        )
