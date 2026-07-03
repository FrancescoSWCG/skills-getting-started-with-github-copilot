"""
Tests for the /activities endpoint (GET).

Verifies that the activities endpoint returns correct structure, data, and required fields.
"""

import pytest


class TestGetActivities:
    """Test suite for GET /activities endpoint."""

    def test_get_activities_returns_dict(self, client):
        """Test that /activities returns a dictionary."""
        response = client.get("/activities")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_get_activities_returns_nine_activities(self, client):
        """Test that /activities returns all 9 pre-loaded activities."""
        response = client.get("/activities")
        activities = response.json()
        assert len(activities) == 9

    def test_get_activities_contains_expected_activity_names(self, client):
        """Test that response contains all expected activity names."""
        expected_activities = {
            "Chess Club",
            "Programming Class",
            "Gym Class",
            "Basketball Team",
            "Tennis Club",
            "Art Studio",
            "Drama Club",
            "Debate Team",
            "Science Club"
        }
        response = client.get("/activities")
        activities = response.json()
        assert set(activities.keys()) == expected_activities

    def test_activity_has_required_fields(self, client):
        """Test that each activity has all required fields."""
        required_fields = {"description", "schedule", "max_participants", "participants"}
        response = client.get("/activities")
        activities = response.json()

        for activity_name, activity_data in activities.items():
            assert isinstance(activity_data, dict), f"Activity {activity_name} is not a dictionary"
            assert set(activity_data.keys()) == required_fields, \
                f"Activity {activity_name} missing required fields"

    def test_activity_description_is_string(self, client):
        """Test that each activity's description is a string."""
        response = client.get("/activities")
        activities = response.json()

        for activity_name, activity_data in activities.items():
            assert isinstance(activity_data["description"], str), \
                f"Activity {activity_name} description is not a string"
            assert len(activity_data["description"]) > 0, \
                f"Activity {activity_name} description is empty"

    def test_activity_schedule_is_string(self, client):
        """Test that each activity's schedule is a string."""
        response = client.get("/activities")
        activities = response.json()

        for activity_name, activity_data in activities.items():
            assert isinstance(activity_data["schedule"], str), \
                f"Activity {activity_name} schedule is not a string"
            assert len(activity_data["schedule"]) > 0, \
                f"Activity {activity_name} schedule is empty"

    def test_max_participants_is_positive_integer(self, client):
        """Test that max_participants is a positive integer for each activity."""
        response = client.get("/activities")
        activities = response.json()

        for activity_name, activity_data in activities.items():
            max_participants = activity_data["max_participants"]
            assert isinstance(max_participants, int), \
                f"Activity {activity_name} max_participants is not an integer"
            assert max_participants > 0, \
                f"Activity {activity_name} max_participants is not positive"

    def test_participants_is_list(self, client):
        """Test that participants is a list for each activity."""
        response = client.get("/activities")
        activities = response.json()

        for activity_name, activity_data in activities.items():
            assert isinstance(activity_data["participants"], list), \
                f"Activity {activity_name} participants is not a list"

    def test_participants_contains_strings(self, client):
        """Test that each participant in participants list is an email string."""
        response = client.get("/activities")
        activities = response.json()

        for activity_name, activity_data in activities.items():
            for participant in activity_data["participants"]:
                assert isinstance(participant, str), \
                    f"Activity {activity_name} has non-string participant: {participant}"
                assert "@" in participant, \
                    f"Activity {activity_name} has participant without @ sign: {participant}"

    def test_participants_count_within_limits(self, client):
        """Test that current participant count does not exceed max_participants."""
        response = client.get("/activities")
        activities = response.json()

        for activity_name, activity_data in activities.items():
            participant_count = len(activity_data["participants"])
            max_participants = activity_data["max_participants"]
            assert participant_count <= max_participants, \
                f"Activity {activity_name} has {participant_count} participants " \
                f"but max is {max_participants}"

    def test_chess_club_has_correct_initial_state(self, client):
        """Test Chess Club specific initial state."""
        response = client.get("/activities")
        activities = response.json()

        chess = activities["Chess Club"]
        assert chess["max_participants"] == 12
        assert len(chess["participants"]) == 2
        assert "michael@mergington.edu" in chess["participants"]
        assert "daniel@mergington.edu" in chess["participants"]

    def test_programming_class_has_correct_initial_state(self, client):
        """Test Programming Class specific initial state."""
        response = client.get("/activities")
        activities = response.json()

        prog = activities["Programming Class"]
        assert prog["max_participants"] == 20
        assert len(prog["participants"]) == 2
        assert "emma@mergington.edu" in prog["participants"]
        assert "sophia@mergington.edu" in prog["participants"]

    def test_gym_class_has_room_for_more_participants(self, client):
        """Test that Gym Class has room for more participants."""
        response = client.get("/activities")
        activities = response.json()

        gym = activities["Gym Class"]
        current = len(gym["participants"])
        max_capacity = gym["max_participants"]
        assert current < max_capacity, "Gym Class should have room for more participants"
