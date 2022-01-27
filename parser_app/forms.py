from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('FILM', 'FILM'),
        ('ANIME', 'ANIME'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]
    def parse_data(self):
        if self.data['media_type'] == 'FILM':
            film_parser = parser.parser()
            for i in film_parser:
                models.Film.objects.create(**i)
        elif self.data['media_type'] == 'ANIME':
            anime_parser = parser.parser()
            for i in anime_parser:
                models.Anime.objects.create(**i)


