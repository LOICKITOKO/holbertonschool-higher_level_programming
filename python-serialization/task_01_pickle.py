#!/usr/bin/python3


import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Initialisation de la classe CustomObject avec les attributs name, age et is_student.
        
        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
            is_student (bool): Si la personne est étudiante ou non.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet dans un format lisible.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'instance actuelle et la sauvegarde dans un fichier.

        Args:
            filename (str): Le nom du fichier dans lequel sérialiser l'objet.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise une instance à partir d'un fichier.

        Args:
            filename (str): Le nom du fichier à partir duquel désérialiser l'objet.

        Returns:
            CustomObject: L'instance désérialisée de la classe CustomObject.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"Deserialization error: {e}")
            return None
