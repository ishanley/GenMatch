from names import get_full_name
from collections import namedtuple
from random import randint

traits = {}
traits['romance'] = [
    'eye-color', 'weight', 'bmi', 'red-hair', 'black-hair', 'skin-pigmentation', 'male-pattern-baldness', 'freckles', 'red-wine-liking', 'white-wine-liking', 'endurance-performance'
]
traits['p-health'] = [
    'lung-cancer', 'colorectal-cancer', 'gastric-cancer', 'breast-cancer', 'liver-cancer', 'pancreatic-cancer', 'prostate-cancer', 'type-2-diabetes', 'myocardial-infection'
]
traits['m-health'] = [
    'agreeableness', 'neuroticism', 'extraversion', 'conscientiousness', 'openness', 'depression', 'anger', 'reward-dependence', 'harm-avoidance', 'gambling', 'novelty-seeking'
]
traits['friend'] = [
    'beard-thickness', 'morning-person', 'red-hair', 'black-hair', 'motion-sickness', 'handedness', 'longevity', 'smell-sensitivity-for-malt', 'smoking-behavior', 'alcohol-drinking-behavior'
]
traits['work'] = [
    'agreeablness', 'openness', 'reward-dependence', 'harm-avoidance', 'gambling', 'novelty-seeking', 'childhood-intelligence', 'hearing-function', 'word-reading-ability', 'reading-and-spelling-ability'
]

def get_all_traits():
    s = set()
    for l in traits.values():
        for e in l:
            s.add(e.replace('-', '_'))
    return s

all_traits = get_all_traits()
TraitVector = namedtuple('TraitVector', all_traits)

def calculate_sim(p1, p2, trait_type):
    a = traits[trait_type]
    total = len(a) * 4
    tot = total
    for trait in a:
        t1 = get_api_data(p1, trait)
        t2 = get_api_data(p2, trait)
        tot -= abs(t1['summary']['score'] - t2['summary']['score'])
    return tot/total

def generate_random_users(n=20):
    users = []
    for i in range(n):
        user = {
            'traits': TraitVector._make((randint(0, 4) for _ in range(len(all_traits)))),
            'name': get_full_name()
        }
        users.append(user)
    return users
    


def get_api_data(user, trait):
    return {
        "summary": {
            "score": getattr(user['traits'], trait.replace('-', '_'))
        },
        "name": user['name']
    }


rand_users = generate_random_users()

def get_report(p1, p2, trait_type):
    return {'name': p2['name'], 'similarity': calculate_sim(p1, p2, trait_type)}

def get_reports(p, trait_type):
    return [get_report(p, user, trait_type) for user in rand_users]