from django.test import TestCase, Client

from .models import Team, Division, Conference

# Create your tests here.
class TeamTestCase(TestCase):
    
    def setUp(self):
        """Set up dummy teams, conferences and divisions in order to run tests"""
        # Create dummy Conferences.
        c1 = Conference.objects.create(name="West")
        c2 = Conference.objects.create(name="East")
        
        # Create dummy Divisions.
        d1 = Division.objects.create(name="newDiv1", conf_id=1)
        d2 = Division.objects.create(name="newDiv2", conf_id=2)

        # Create dummy teams.
        Team.objects.create(
            div=d1, 
            city="AAA", 
            fullName="AAA", 
            teamId=1, 
            nickname="AAA",
            allStar=0,
            logo="",
            shortName="AAA",
        )
        Team.objects.create(
            div=d2, 
            city="BBB", 
            fullName="BBB", 
            teamId=2, 
            nickname="BBB",
            allStar=-1,
            logo="",
            shortName="BBB",
        )

    def test_is_valid_team(self):
        """Test dummy teams - AAA should be valid, BBB should be invalid"""
        t1 = Team.objects.get(shortName="AAA")
        self.assertTrue(t1.is_valid_team())

        t2 = Team.objects.get(shortName="BBB")
        self.assertFalse(t2.is_valid_team())

    def test_index(self):
        """Test the index route response is working and dummy teams are received"""
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["teams"]), 2)
