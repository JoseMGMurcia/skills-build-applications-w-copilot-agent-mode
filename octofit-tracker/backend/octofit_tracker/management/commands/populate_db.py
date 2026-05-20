from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Crear usuarios
        tony = User.objects.create(email='tony@stark.com', username='IronMan', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', username='Batman', team=dc)
        clark = User.objects.create(email='clark@kent.com', username='Superman', team=dc)

        # Crear actividades
        Activity.objects.create(user=tony, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='cycle', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, type='fly', duration=120, date=timezone.now().date())

        # Crear workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training')
        w2 = Workout.objects.create(name='Agility Drills', description='Agility and speed')
        w1.suggested_for.add(marvel, dc)
        w2.suggested_for.add(marvel, dc)

        # Crear leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
