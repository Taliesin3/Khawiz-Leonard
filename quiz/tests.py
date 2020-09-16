from django.test import TestCase

from .models import Team, Division, Conference

# Create your tests here.
class TeamTestCase(TestCase):
    
    def setUp(self):
        # Creat Conferences.
        c1 = Conference.objects.create(name="West")
        c2 = Conference.objects.create(name="East")
        
        # Create Divisions.
        d1 = Division.objects.create(name="newDiv1", conf_id=1)
        d2 = Division.objects.create(name="newDiv2", conf_id=2)

        # Create teams.
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
        t1 = Team.objects.get(shortName="AAA")
        self.assertTrue(t1.is_valid_team())

        t2 = Team.objects.get(shortName="BBB")
        self.assertFalse(t2.is_valid_team())


