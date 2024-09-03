from django.db import models


class Breed(models.Model):

    SIZES = [
        ("tiny", "Tiny"),
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large"),
    ]

    VALUES_INT = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    name = models.CharField(max_length=30)
    size = models.CharField(max_length=8, choices=SIZES, blank=False, default="tiny")
    friendliness = models.PositiveIntegerField(
        choices=VALUES_INT, blank=False, default=1
    )
    trainability = models.PositiveIntegerField(
        choices=VALUES_INT, blank=False, default=1
    )
    shedding_amount = models.PositiveIntegerField(
        choices=VALUES_INT, blank=False, default=1
    )
    exercise_needs = models.PositiveIntegerField(
        choices=VALUES_INT, blank=False, default=1
    )

    def __str__(self) -> str:
        return self.name


class Dog(models.Model):

    GENDERS = {"M": "Male", "F": "Female"}

    name = models.CharField(max_length=70)
    age = models.PositiveIntegerField()
    breed = models.ForeignKey("Breed", on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=8, choices=GENDERS, blank=False, default="M")
    color = models.CharField(max_length=30)
    favorite_food = models.CharField(max_length=70)
    favorite_toy = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.name
