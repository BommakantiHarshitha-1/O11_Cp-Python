import os,sys
sys.path.append(os.getcwd())
from friendsOfFriends import friendsOfFriends
import pytest


@pytest.mark.parametrize('d,result',[ 
    (
        {
            "jon": set(["arya", "tyrion"]),
            "tyrion": set(["jon", "jaime", "pod"]),
            "arya": set(["jon"]),
            "jaime": set(["tyrion", "brienne"]),
            "brienne": set(["jaime", "pod"]),
            "pod": set(["tyrion", "brienne", "jaime"]),
            "ramsay": set()
        }, {
            'tyrion': {'arya', 'brienne'}, 
            'pod': {'jon'}, 
            'brienne': {'tyrion'}, 
            'arya': {'tyrion'}, 
            'jon': {'pod', 'jaime'}, 
            'jaime': {'pod', 'jon'}, 
            'ramsay': set()
        }
    ), (
        {
            "jon": set(["arya"]),
            "tyrion": set(["jaime"]),
            "arya": set(["jon"]),
            "jaime": set(["tyrion"]),
            "brienne": set(["jaime"]),
            "pod": set(["brienne"]),
            "ramsay": set(["pod"])
        }, {
            'tyrion': set(), 
            'pod': {'jaime'}, 
            'brienne': {'tyrion'}, 
            'arya': set(), 
            'jon': set(), 
            'jaime': set(), 
            'ramsay': {"brienne"}
        }
    )
])

def test_friendsOfFriends(d,result):
    assert friendsOfFriends(d) == result