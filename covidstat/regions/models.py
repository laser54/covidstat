from django.db import models

REGIONS = (
    ('novosib', 'Новосибирская область'),
    ('barnaul', 'Алтайский край'),
    ('omsk', 'Омская область'),
    ('tomsk', 'Томская область'),
    ('kemerovo', 'Кемеровская область'),
    ('krasnoyarsk', 'Красноярский край'),
    ('irkutsk', 'Иркутская область'),
    ('chita', 'Забайкальский край'),
    ('tyva', 'Республика Тыва'),
    ('buratia', 'Республика Бурятия'),
    ('altai', 'Республика Алтай'),
    ('khakasia', 'Республика Хакасия'),
    )


class Region(models.Model):
    pub_date = models.DateField()
    region = models.CharField(max_length=20, choices=REGIONS)
    sick = models.IntegerField()
    died = models.IntegerField()
    sick_today = models.IntegerField()
    died_today = models.IntegerField()

    def __str__(self):
        return f'{self.pub_date} {self.region}'
