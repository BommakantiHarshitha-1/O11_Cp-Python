import os,sys
sys.path.append(os.getcwd())
from movie_awards import movie_awards
import pytest

@pytest.mark.parametrize('oscarResults,result',[ 
    (
        { 
            ("Best Picture", "The Shape of Water"), 
            ("Best Actor", "Darkest Hour"),
            ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
            ("Best Director", "The Shape of Water"),
            ("Best Supporting Actor", "Three Billboards Outside Ebbing, Missouri"),
            ("Best Supporting Actress", "I, Tonya"),
            ("Best Original Score", "The Shape of Water")
        },
        { 
            "Darkest Hour" : 1,
            "Three Billboards Outside Ebbing, Missouri" : 2,
            "The Shape of Water" : 3,
            "I, Tonya" : 1
        }
    ), (
        {
            ("Best Picture", "The Shape of Water"), 
            ("Best Actor", "Darkest Hour"),
            ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
            ("Best Director", "The Shape of Water"),
        }, {
            "Darkest Hour": 1,
            "Three Billboards Outside Ebbing, Missouri": 1,
            "The Shape of Water": 2
        }
    ), (
        {}, {}
    )
])

def test_movie_awards(oscarResults,result):
    assert movie_awards(oscarResults) == result