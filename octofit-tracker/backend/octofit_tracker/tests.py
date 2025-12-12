from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.assertEqual(str(team), 'Marvel')

    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC Team')
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team=team)
        self.assertEqual(str(user), 'clark@dc.com')

    def test_create_activity(self):
        team = Team.objects.create(name='X-Men', description='Mutants')
        user = User.objects.create(name='Logan', email='logan@xmen.com', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30, date='2025-12-12')
        self.assertIn('logan@xmen.com', str(activity))

    def test_create_workout(self):
        team = Team.objects.create(name='Avengers', description='Earth Heroes')
        workout = Workout.objects.create(name='Pushups', description='Upper body')
        workout.suggested_for.add(team)
        self.assertEqual(str(workout), 'Pushups')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Justice League', description='DC Heroes')
        user = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=team)
        lb = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertIn('bruce@dc.com', str(lb))
