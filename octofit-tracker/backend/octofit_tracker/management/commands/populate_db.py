from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Batman', email='batman@dc.com', team=dc),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        activities = [
            Activity(user=users[0], type='Running', duration=30, date='2025-12-01'),
            Activity(user=users[1], type='Cycling', duration=45, date='2025-12-02'),
            Activity(user=users[2], type='Swimming', duration=60, date='2025-12-03'),
            Activity(user=users[3], type='Yoga', duration=50, date='2025-12-04'),
        ]
        for activity in activities:
            activity.save()

        workouts = [
            Workout(name='Hero Workout', description='Intense training for heroes', suggested_for='Marvel'),
            Workout(name='Justice Workout', description='Strength and agility for DC heroes', suggested_for='DC'),
        ]
        for workout in workouts:
            workout.save()

        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
