from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Push Ups', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, activity='Running', duration=30)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Test User')
    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')
    def test_activity_str(self):
        self.assertIn('Running', str(self.activity))
    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Push Ups')
    def test_leaderboard_str(self):
        self.assertIn('Test User', str(self.leaderboard))
