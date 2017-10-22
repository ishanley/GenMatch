traits = {}
traits['romance'] = [
    'eye-color', 'weight', 'bmi', 'red-hair', 'black-hair', 'skin-pigmentation', 'male-pattern-baldness', 'freckles', 'red-wine-liking', 'white-wine-liking', 'endurance-performance'
]
traits['p-health'] = [
    'lung-cancer', 'colorectal-cancer', 'gastric-cencer', 'breast-cancer', 'liver-cancer', 'pancreatic-cancer', 'prostate-cancer', 'type-2-diabetes', 'myocardial-infarction'
]
traits['m-health'] = [
    'agreeablness', 'neuroticism', 'extraversion', 'conscientiousness', 'openness', 'depression', 'anger', 'reward-dependence', 'harm-avoidance', 'gambling', 'novelty-seeking'
]
traits['friend'] = [
    'beard-thickness', 'morning-person', 'red-hair', 'black-hair', 'motion-sickness', 'handedness', 'longevity', 'smell-sensitivity-for-malt', 'smoking-behavior', 'alcohol-drinking-behavior'
]
traits['work'] = [
    'agreeablness', 'openness', 'reward-dependence', 'harm-avoidance', 'gambling', 'novelty-seeking', 'childhood-intelligence', 'hearing-function', 'word-reading-ability', 'reading-and-spelling-ability'
]

def calculate_sim(p1, p2, trait_type):
    a = traits[trait_type]
    tot = len(a)
    for trait in a:
        tot -= abs(p1['summary']['score'] - p2['summary']['score'])
    return '{.2f} %'.format((tot/len(a)) * 100)

def get_reports(p, trait_type):
    # generate list of random users to query against
    users = [] # random list
    reports=[]
    
    for user in users:
        similarity = calculate_sim(p, user, trait_type)
        name
        reports.append({'name': name, 'similarity': similarity})
        
    return reports