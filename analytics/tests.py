# coding: utf-8

from django.test import TestCase

from .models import *
from content.models import *

from datetime import datetime
from decimal import Decimal
# Create your tests here.
class ModelTest(TestCase):
    #----------------------------------------------------------------------
    description='<img alt="" src="https://cdn0.vox-cdn.com/thumbor/hN4EeREv8bHNymHPOX4RO87efnc=/0x0:2100x1400/1310x873/cdn0.vox-cdn.com/uploads/chorus_image/image/53943747/rebel_haxd.0.jpg" /> <p id="SOvwwY">In April 2000, New Line Cinema released <em>Love &amp; Basketball</em>, the debut film of writer-director Gina Prince-Bythewood. It’s a refreshingly nuanced and original screen romance, a love story spanning more than a decade in the lives of two black basketball players, while encompassing details about gender, race, class, and culture that are clearly drawn from Prince-Bythewood’s personal experiences and observations. Two months later, in June, director John Singleton capped off a decade as one of the most successful black directors in Hollywood by watching his punchy remake of the blaxploitation classic <em>Shaft</em> become a solid box office hit. Those two movies arriving so closely together on the calendar represented a rare encouraging sign from an...</p> <p> <a href="http://www.theverge.com/2017/3/28/15089888/black-film-directors-new-tv-shows-shots-fired-rebel-bythewood-singleton">Continue reading&hellip;</a> </p>',    
    s1 = Source.objects.create(title='the_verge',
                                   url='http://www.theverge.com',
                                   rss='http://www.theverge.com/rss/index.xml')
    a1 = Article.objects.create(title='Our best black filmmakers are finding fresh opportunities on TV',
                                   url='http://www.theverge.com/2017/3/28/15089888/black-film-directors-new-tv-shows-shots-fired-rebel-bythewood-singleton',
                                   author='Noel Murray',
                                   source=s1,
                                   description=description,
                                   publication_time=datetime.now())
    a1.save()
    
  
    def test_model_creation(self, a1 = a1, s1 = s1):
        """test if models can be created"""
        k1 = Keyword.objects.create(name = "film")
        import pdb; pdb.set_trace()
        ka1 = KeywordAnalysis.objects.create(article = a1, keyword = k1, relevance = Decimal(0.5))
  
        return self.assertEqual(
            (Keyword.objects.get(id=k1.id), KeywordAnalysis.objects.get(id=ka1.id)), 
            (k1, ka1)
        )