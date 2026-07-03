"""
Shared pytest fixtures for FastAPI application tests.

Provides TestClient and sample data fixtures for testing the Mergington High School API.
"""

import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """
    Provides a FastAPI TestClient for making requests to the application.
    Creates a fresh client for each test to ensure test isolation.
    """
    return TestClient(app)


@pytest.fixture
def sample_activities():
    """
    Provides sample activity data matching the app's in-memory database structure.
    Useful for assertions and test setup.
    """
    return {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball team for all skill levels",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["james@mergington.edu", "lucas@mergington.edu"]
        },
        "Tennis Club": {
            "description": "Tennis training and tournaments",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["avery@mergington.edu", "jordan@mergington.edu"]
        },
        "Art Studio": {
            "description": "Painting, drawing, and sculpture techniques",
            "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["isabella@mergington.edu", "sophia@mergington.edu"]
        },
        "Drama Club": {
            "description": "Theater performances and acting classes",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 25,
            "participants": ["mason@mergington.edu", "charlotte@mergington.edu"]
        },
        "Debate Team": {
            "description": "Competitive debate and argumentation skills",
            "schedule": "Mondays and Fridays, 3:30 PM - 4:30 PM",
            "max_participants": 16,
            "participants": ["alexander@mergington.edu", "abigail@mergington.edu"]
        },
        "Science Club": {
            "description": "Hands-on experiments and scientific exploration",
            "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
            "max_participants": 22,
            "participants": ["benjamin@mergington.edu", "mia@mergington.edu"]
        }
    }
