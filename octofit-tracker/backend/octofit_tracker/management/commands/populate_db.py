from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient, ASCENDING

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Collections
        users = db['users']
        teams = db['teams']
        activities = db['activities']
        leaderboard = db['leaderboard']
        workouts = db['workouts']

        # Clear collections
        users.delete_many({})
        teams.delete_many({})
        activities.delete_many({})
        leaderboard.delete_many({})
        workouts.delete_many({})

        # Create unique index on email
        users.create_index([('email', ASCENDING)], unique=True)

        # Teams
        marvel_id = teams.insert_one({'name': 'Marvel'}).inserted_id
        dc_id = teams.insert_one({'name': 'DC'}).inserted_id

        # Users
        marvel_heroes = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team_id': marvel_id},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'team_id': marvel_id},
            {'name': 'Black Widow', 'email': 'widow@marvel.com', 'team_id': marvel_id},
        ]
        dc_heroes = [
            {'name': 'Superman', 'email': 'superman@dc.com', 'team_id': dc_id},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team_id': dc_id},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team_id': dc_id},
        ]
        users.insert_many(marvel_heroes + dc_heroes)

        # Activities
        activities.insert_many([
            {'user_email': 'ironman@marvel.com', 'activity': 'Running', 'duration': 30},
            {'user_email': 'superman@dc.com', 'activity': 'Flying', 'duration': 60},
        ])

        # Workouts
        workouts.insert_many([
            {'name': 'Push Ups', 'difficulty': 'Medium'},
            {'name': 'Squats', 'difficulty': 'Easy'},
        ])

        # Leaderboard
        leaderboard.insert_many([
            {'user_email': 'ironman@marvel.com', 'score': 100},
            {'user_email': 'superman@dc.com', 'score': 120},
        ])

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
