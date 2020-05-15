import random

from model.player import Player


class ModelProviderPlayer(object):

    @staticmethod
    def get_new(id_team, lname, fname, date=None, comment=None):
        obj = Player(id_team, lname, fname, date, comment)
        return obj

    @staticmethod
    def get_zlatan(id_team):
        obj = Player(id_team, "Ibrahimovic", "Zlatan", "03/10/1981", "Suédois")
        return obj

    @staticmethod
    def get_kylian(id_team):
        obj = Player(id_team, "Mbappé", "Kylian", "20/12/1998", "Français")
        return obj

    @staticmethod
    def get_Lionel(id_team):
        obj = Player(id_team, "Messi", "Lionel", "24/06/1987", "Argentin")
        return obj

    @staticmethod
    def get_randomplayer(id_team):
        prenom = """
                iliess
                james
                ylea
                bathiste
                steline
                hidayet
                arno
                luc-antoine
                milady
                cassie
                kardiatou
                yerim
                marie-carmen
                eyal
                femi
                isiah
                myrto
                gwennina
                iliano
                intza
                leoncine
                tibalt
                lassina
                djazira
                franki
                cherazede
                suhayl
                stevenn
                dioni
                sadji
                """.split()
        nom = """
        Rodriguez
        Guichard
        Gillet
        Etienne
        Grondin
        Poulain
        Tessier
        Chevallier
        Collin
        Chauvin
        Da Silva
        Bouchet
        Gay
        Lemaitre
        Benard
        Marechal
        Humbert
        Reynaud
        Antoine
        Hoarau
        Perret
        Barthelemy
        Cordier
        Pichon
        Lejeune
        Gilbert
        Lamy
        Delaunay
        Pasquier
        Carlier
        Laporte
                    """.split()
        day = random.randrange(1, 28, 1)
        month = random.randrange(1, 12, 1)
        year = random.randrange(1975, 2002, 1)
        lprenom = prenom[random.randrange(1, len(prenom), 1)]
        lnom = nom[random.randrange(1, len(nom), 1)]
        obj = Player(id_team, lnom, lprenom, "{}/{}/{}".format(day, month, year), "Random Generated")
        return obj
